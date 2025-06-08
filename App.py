import os
import streamlit as st

# For async stuff
import nest_asyncio
nest_asyncio.apply()

# Loading API key
os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]

st.title("Ask & Summarize Research Papers with RAG")

file_choice = st.selectbox("Choose a paper:", ["attention.pdf", "gpt3.pdf"])
query = st.text_input("Ask a question about the paper:", placeholder="e.g. What is the model architecture?")

if query and file_choice:
    with st.spinner("Processing..."):

        #loading and splitting document into nodes
        from llama_index.core import SimpleDirectoryReader
        from llama_index.core.node_parser import SentenceSplitter

        docs = SimpleDirectoryReader(input_files=[f"./papers/{file_choice}"]).load_data()
        splitter = SentenceSplitter(chunk_size=2000, chunk_overlap=20)
        nodes = splitter.get_nodes_from_documents(docs)

        #Setting Up model
        from llama_index.core import Settings
        from llama_index.llms.groq import Groq
        from llama_index.embeddings.huggingface import HuggingFaceEmbedding

        Settings.llm = Groq(model="llama-3.1-8b-instant")
        Settings.embed_model = HuggingFaceEmbedding()

        #Creating Indexes
        from llama_index.core import SummaryIndex, VectorStoreIndex

        summary_index = SummaryIndex(nodes)
        vector_index = VectorStoreIndex(nodes)

        #Search Engines
        summary_query_engine = summary_index.as_query_engine(
            response_mode="tree_summarize", use_async=True
        )
        vector_query_engine = vector_index.as_query_engine()

        #Tool wrappers of both engines to help decide routerllm
        from llama_index.core.tools import QueryEngineTool

        summary_tool = QueryEngineTool.from_defaults(
            query_engine=summary_query_engine,
            description="Useful for summarization of the given context"
        )
        vector_tool = QueryEngineTool.from_defaults(
            query_engine=vector_query_engine,
            description="Useful for retrieving specific context based on the question"
        )

        #Employing router query engine to use a specific tool
        from llama_index.core.query_engine.router_query_engine import RouterQueryEngine
        from llama_index.core.selectors import LLMSingleSelector

        Ask = RouterQueryEngine(
            selector=LLMSingleSelector.from_defaults(),
            query_engine_tools=[summary_tool, vector_tool],
            verbose=True
        )

        #Output display
        response = Ask.query(query)
        st.subheader("Answer :")
        st.write(response.response)

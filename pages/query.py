import streamlit as st
import os
from menu import menu
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage
from llama_index.core.memory import ChatMemoryBuffer

st.set_page_config(page_title="Query", page_icon="🦙")
menu()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

gen_prompt = "Leverage your chatbot abilities to answer some given questions on a specific topic by only using the context provided, not using any prior knowledge, making sure to avoid repetitions in the informations and write the answers in such a way that all the answers must follow the flow and together can be used to form a report."


project_name = st.sidebar.selectbox("Select Project:", options=st.session_state.projects)
st.sidebar.write(f"Selected Project: {project_name}")
if os.path.exists(f'index/{project_name}'):
    if os.path.exists(f"{st.session_state.role}/{project_name}"):
        files = os.listdir(f"{st.session_state.role}/{project_name}")
        if files:
            for file in files:
                st.sidebar.write(file)
        else:
            st.sidebar.write("The project is empty.")
else:
    docs = SimpleDirectoryReader(f"{st.session_state.role}/{project_name}").load_data()
    index = VectorStoreIndex.from_documents(docs)
    index.storage_context.persist(f'index/{project_name}')



def query():
    query = st.chat_input(f"Enter Query:")
    if query:
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message(f"{st.session_state.role}"):
                st.markdown(query)
        storage_context = StorageContext.from_defaults(persist_dir=f'index/{project_name}')
        index = load_index_from_storage(storage_context)
        chat_engine = index.as_chat_engine(
            chat_mode="context",
            memory=ChatMemoryBuffer.from_defaults(token_limit=16000),
            system_prompt=(
                f"{gen_prompt}\n"
                "Only use the given context, do not add any prior knowledge."
                "the given context : {context_str}"
            ),
            )
        # response = chat_engine.chat(query)
        with st.chat_message("assistant"):
            response = chat_engine.chat(query)
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})



if __name__ == "__main__":
    query()
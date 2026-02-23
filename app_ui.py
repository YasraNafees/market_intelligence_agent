import streamlit as st
from engin import agent_executor 
from langchain_community.callbacks import StreamlitCallbackHandler

# 1. UI Configuration
st.set_page_config(page_title="AI Market Intelligence Agent", layout="wide")
st.title("🚀 Business Intelligence Agent")
st.markdown("Analyze competitors, hiring trends, and tech projects in real-time.")

# 2. Sidebar for Info
with st.sidebar:
    st.header("Agent Status")
    st.success("Brain: Groq (Llama-3.3)")
    st.success("Search: Tavily AI")
    st.info("RAM Optimized: 4GB Mode")

# 3. Chat Interface
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help with your business research today?"}]

# Display chat history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 4. User Input & Agent Action
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        # YEH HAI MAGIC: Agent ki thinking screen par nazar aaye gi
        st_callback = StreamlitCallbackHandler(st.container())
        
        response = agent_executor.invoke(
            {"input": prompt},
            {"callbacks": [st_callback]}
        )
        
        answer = response["output"]
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.write(answer)

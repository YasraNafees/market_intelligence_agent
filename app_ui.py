import streamlit as st
import asyncio 
from engin import run_research 
import json

# 1. UI Configuration
st.set_page_config(page_title="AI Market Intelligence Agent", layout="wide", page_icon="📊")
st.title("🚀 Business Intelligence Agent")
st.markdown("Analyze competitors, hiring trends, and tech projects in real-time.")

# 2. Sidebar
with st.sidebar:
    st.header("🤖 Agent Status")
    st.success("Brain: Groq (Llama-3.1-8b)")
    st.success("Search: Tavily AI")
    st.info("Mode: Structured JSON Output")
    
    if st.button("🧹 Clear Chat History"):
        from engin import agent_executor
        agent_executor.memory.clear()
        st.session_state["messages"] = [{"role": "assistant", "content": "History cleared! How can I help now?"}]
        st.rerun() 

# 3. Chat Session State
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help with your business research today?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 4. User Input & Async Agent Action
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        # --- THINKING INDICATOR ---
        thinking_text = st.empty() # Placeholder for "Thinking..."
        thinking_text.markdown("*(Thinking... 🤔)*")
        
        try:
            # --- STATUS STEPS ---
            with st.status("🔍 Agent is working...", expanded=True) as status:
                st.write("📡 Accessing Tavily Search Engine...")
                st.write("⏳ Waiting for Rate Limit cooldown (30s)...")
                
                # Actual research call
                result = asyncio.run(run_research(prompt))
                
                st.write("🧠 Processing and Formatting JSON...")
                status.update(label="✅ Research Complete!", state="complete", expanded=False)
            
            # Remove "Thinking..." once data is ready
            thinking_text.empty()

            # --- DATA DISPLAY LOGIC ---
            data = result if isinstance(result, dict) else (result.dict() if hasattr(result, "dict") else None)

            if data:
                st.markdown(f"### 📊 BI Report: {data.get('company_name', 'N/A')}")
                
                col1, col2 = st.columns(2)
                with col1:
                    st.info("🚀 **Latest AI Initiatives**")
                    projects = data.get('latest_project', [])
                    if isinstance(projects, list):
                        for p in projects:
                            st.write(f"🔹 {p}")
                    else:
                        st.write(projects)
                
                with col2:
                    st.info("📈 **Hiring Trends**")
                    st.write(data.get('hiring_trends', 'N/A'))
                
                st.success("💡 **Strategic Advice**")
                st.markdown(data.get('strategic_advice', 'N/A'))
                
                final_display = f"✅ Report generated for {data.get('company_name')}"
            else:
                st.warning("⚠️ Could not parse structured data. Showing raw output:")
                st.write(str(result))
                final_display = str(result)

            st.session_state.messages.append({"role": "assistant", "content": final_display})

        except Exception as e:
            thinking_text.empty() # Clear thinking on error
            st.error(f"⚠️ Agent Error: {str(e)}")

# 🚀 Autonomous Market Intelligence Agent

A professional AI Agent built with **Python 3.10.11**, designed to solve real-world business problems by performing live competitor research and hiring trend analysis.

## 🌟 Key Features
- **Autonomous Reasoning:** Uses the **ReAct (Reasoning + Acting)** pattern for transparent decision-making.
- **Real-Time Data:** Integrated with **Tavily AI** for live web-grounded research (No outdated static data).
- **High-Speed Inference:** Powered by **Llama-3.3-70B** via **Groq Cloud**.
- **Cloud-Native & Resource-Light:** Optimized for low-end hardware (4GB RAM) using a serverless API-first architecture.
- **Enterprise Ready:** Fully **Dockerized** and monitored via **LangSmith**.

## 🛠️ Tech Stack
- **Framework:** [LangChain](https://python.langchain.com)
- **LLM Engine:** [Groq Cloud](https://console.groq.com)
- **Search Tool:** [Tavily AI](https://tavily.com)
- **API/UI:** [FastAPI](https://fastapi.tiangolo.com) & [Streamlit](https://streamlit.io)
- **Observability:** [LangSmith](https://smith.langchain.com)

## 🚀 How to Run Locally
1. Clone the repo: `git clone https://github.com`
2. Create `.env` and add your API Keys (`GROQ`, `TAVILY`, `LANGCHAIN`).
3. Install requirements: `pip install -r requirements.txt`
4. Run Streamlit UI: `streamlit run app_ui.py`

## 📦 Deployment
This project is **Docker-ready** for deployment on  **Railway**.

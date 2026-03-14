# 🚀 Autonomous Market Intelligence Agent

![Python](https://img.shields.io/badge/Python-3.10.11-blue) ![LangChain](https://img.shields.io/badge/LangChain-Enabled-green) ![Groq](https://img.shields.io/badge/Groq-LLaMA3.3--70B-orange) ![Docker](https://img.shields.io/badge/Docker-Ready-blue) ![License](https://img.shields.io/badge/License-MIT-yellow)

### Real-Time Research | ReAct Pattern | Enterprise-Ready

An autonomous AI agent built with Python 3.10.11, designed to solve real-world business problems by performing **live competitor research** and **hiring trend analysis** — fully grounded in real-time web data.

---

## 🎬 Demo

[![Watch Demo](https://img.youtube.com/vi/swxae0VgGYI/maxresdefault.jpg)](https://youtu.be/swxae0VgGYI)

> Click the thumbnail to watch the full demo on YouTube.

---

## ✨ Key Features

- **Autonomous Reasoning:** Uses the ReAct (Reasoning + Acting) pattern for transparent, step-by-step decision-making.
- **Real-Time Data:** Integrated with Tavily AI for live web-grounded research — no outdated static data.
- **Intelligent Rate-Limit Handling:** Automatically detects Groq API cooldowns and retries with backoff — zero manual intervention needed.
- **High-Speed Inference:** Powered by Llama-3.3-70B via Groq Cloud for enterprise-grade reasoning.
- **Cloud-Native & Resource-Light:** Optimized for low-end hardware (4GB RAM) using a serverless API-first architecture.
- **Enterprise Ready:** Fully Dockerized and monitored via LangSmith for full observability.

---

## 🛠️ Tech Stack & Design Decisions

| Component | Tool | Why |
|---|---|---|
| Framework | LangChain | Modular agent orchestration with ReAct support |
| LLM Engine | Groq Cloud (LLaMA 3.3-70B) | Ultra-fast inference, enterprise-grade reasoning |
| Search Tool | Tavily AI | Real-time web search built for LLM agents |
| Backend | FastAPI | Scalable async API layer |
| UI | Streamlit | Rapid, lightweight frontend for agent interaction |
| Observability | LangSmith | Full trace monitoring and debugging |
| Deployment | Docker | Portable, reproducible environment |

---

## 🏗️ Architecture Flow
```
User Query
      ↓
ReAct Agent (LangChain)
      ↓
Reasoning Step → Tool Decision
      ↓
Tavily AI (Live Web Search)
      ↓
Observation → Next Reasoning Step
      ↓
Rate-Limit Cooldown Handler (if needed)
      ↓
Final Grounded Answer → FastAPI → Streamlit UI
      ↓
LangSmith (Full Trace Monitoring)
```

---

## 🚀 Quick Start

**1. Clone the repo:**
```bash
git clone https://github.com/YasraNafees/market_intelligence_agent.git
cd market_intelligence_agent
```

**2. Set environment variables:**

Create a `.env` file:
```
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
LANGCHAIN_API_KEY=your_langsmith_key
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run the app:**
```bash
streamlit run app_ui.py
```

---

## 📦 Docker Deployment
```bash
docker build -t market-intelligence-agent .
docker run -p 8501:8501 market-intelligence-agent
```

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

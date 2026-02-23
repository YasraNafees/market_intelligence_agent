from fastapi import FastAPI, Query
from engin import agent_executor # Aapki engin.py file se executor le raha hai
import uvicorn

app = FastAPI(title="Market Intelligence Agent API")

@app.get("/")
def home():
    return {"status": "Active", "message": "Business Intelligence Agent is Ready"}

@app.get("/research")
def research(query: str = Query(..., description="Query to research")):
    """
    Endpoint to run business research.
    Usage: http://127.0.0.1 AI projects
    """
    try:
        # send the agent query
        response = agent_executor.invoke({"input": query})
        return {
            "input": query,
            "business_report": response["output"]
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

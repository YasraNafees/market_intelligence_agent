from fastapi import FastAPI, Query, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from engin import run_research, agent_executor
import uvicorn

app = FastAPI(
    title="Market Intelligence Agent",
    description="Professional Business Intelligence Agent solving the 'Time-to-Insight' problem.",
    version="1.0.0"
)

# --- 1. Response Models ---
class BIReportSchema(BaseModel):
    company_name: str
    latest_project: List[str]
    hiring_trends: str
    strategic_advice: str

class BIResponse(BaseModel):
    status: str
    query: str
    business_report: Optional[BIReportSchema] 

# 2. Health Check
@app.get("/", tags=["Health"])
async def home():
    return {"status": "Active", "message": "Business Intelligence Agent is Ready"}

# 3. Research Endpoint
@app.get("/research", response_model=BIResponse, tags=["Agent"])
async def research(query: str = Query(..., description="Query to research")):
    try:
        result = await run_research(query) 
        
        if result and hasattr(result, "dict"):
            report_data = result.dict()
        elif isinstance(result, dict):
            report_data = result
        else:
            return BIResponse(
                status="Partial Success", 
                query=query,
                business_report=None 
            )

        return BIResponse(
            status="Success",
            query=query,
            business_report=report_data
        )

    except Exception as e:
        # Proper Error Handling
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail=f"Agent Processing Error: {str(e)}"
        )
@app.post("/clear-history", tags=["Admin"])
async def clear_history():
    """Purani research history ko saaf karne ke liye"""
    try:
        agent_executor.memory.clear()
        return {"status": "Success", "message": "Chat history cleared!"}
    except Exception as e:
        return {"status": "Error", "message": str(e)}
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

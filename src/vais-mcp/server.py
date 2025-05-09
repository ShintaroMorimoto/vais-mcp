from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

from .vais import call_vais

app = FastAPI()


@app.get("/")
async def search(
    search_query: str,
    google_cloud_project_id: str,
    vais_engine_id: str,
    vais_location: str = "global",
    page_size: int = 5,
    max_extractive_segment_count: int = 2,
) -> dict[str, str]:
    response = call_vais(
        search_query=search_query,
        google_cloud_project_id=google_cloud_project_id,
        vais_engine_id=vais_engine_id,
        vais_location=vais_location,
        page_size=page_size,
        max_extractive_segment_count=max_extractive_segment_count,
    )
    return {"response": response}


mcp = FastApiMCP(
    app, name="Vertex AI Search MCP", description="Vertex AI Search MCP server"
)
mcp.mount()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

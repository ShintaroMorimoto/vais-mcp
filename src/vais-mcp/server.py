import os

from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

from .vais import call_vais

google_cloud_project_id = os.environ.get("GOOGLE_CLOUD_PROJECT_ID")
if not google_cloud_project_id:
    raise ValueError(
        "GOOGLE_CLOUD_PROJECT_ID is not set. Make sure to set it in the environment variables."
    )

vais_engine_id = os.environ.get("VAIS_ENGINE_ID")
if not vais_engine_id:
    raise ValueError(
        "VAIS_ENGINE_ID is not set. Make sure to set it in the environment variables."
    )

vais_location = os.environ.get("VAIS_LOCATION")
if not vais_location:
    vais_location = "global"


app = FastAPI()


@app.get("/")
async def search(
    search_query: str,
    page_size: int = 5,
    max_extractive_segment_count: int = 2,
) -> dict[str, list[str]]:
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

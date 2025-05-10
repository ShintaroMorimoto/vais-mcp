from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

from .config import settings
from .vais import call_vais

app = FastAPI()


@app.get("/")
async def search(
    search_query: str,
) -> dict:
    response_data = call_vais(
        search_query=search_query,
        google_cloud_project_id=settings.GOOGLE_CLOUD_PROJECT_ID,
        impersonate_service_account=settings.IMPERSONATE_SERVICE_ACCOUNT,
        vais_engine_id=settings.VAIS_ENGINE_ID,
        vais_location=settings.VAIS_LOCATION,
        page_size=settings.PAGE_SIZE,
        max_extractive_segment_count=settings.MAX_EXTRACTIVE_SEGMENT_COUNT,
    )
    return {"response": response_data}


mcp = FastApiMCP(
    app, name="Vertex AI Search MCP", description="Vertex AI Search MCP server"
)
mcp.mount()


def main():
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()

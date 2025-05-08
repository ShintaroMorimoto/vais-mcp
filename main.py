from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI()


@app.get("/")
async def search(query: str):
    return {"query": query}


mcp = FastApiMCP(
    app, name="Vertex AI Search MCP", description="Vertex AI Search MCP server"
)
mcp.mount()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

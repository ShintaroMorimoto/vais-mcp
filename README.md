# MCP server for Vertex AI Search

## Tools

- `search`: Search.

## Prerequisite

- Google Cloud Project
- Vertex AI Search App

## Configuration

Add to server config (preferred)

```json
{
  "mcp-obsidian": {
    "command": "uvx",
    "args": ["vais-mcp"],
    "env": {
      "GOOGLE_CLOUD_PROJECT_ID": "<your_google_cloud_project_id>",
      "VAIS_ENGINE_ID": "<your_vais_engine_id>"
    }
  }
}
```

Create a `.env` file in the working directory with the following required variable:

```
GOOGLE_CLOUD_PROJECT_ID=your_google_cloud_project_id
VAIS_ENGINE_ID=your_vais_engine_id
```

Note: You can find the key in the Obsidian plugin config.

## Development

### Building

To prepare the package for distribution:

1. Sync dependencies and update lockfile:

```bash
uv sync
```

### Debugging

Since MCP servers run over stdio, debugging can be challenging. For the best debugging experience, we strongly recommend using the MCP Inspector.

You can launch the MCP Inspector via npm with this command:

```bash
npx @modelcontextprotocol/inspector uv --directory /path
```

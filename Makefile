# Optional variables with default values.
VAIS_LOCATION ?= global
PAGE_SIZE ?= 5
MAX_EXTRACTIVE_SEGMENT_COUNT ?= 2

# For any additional arguments to pass to the 'uv run vais-mcp' command
# (similar to "$@" in entrypoint.sh).
# Example: make run ARGS="--reload"
# Note: The 'vais-mcp' script in pyproject.toml is 'uvicorn vais_mcp.server:app --host 0.0.0.0 --port 8000'.
# Additional ARGS will be appended after the application-specific CLI arguments.
ARGS ?=

.PHONY: run
run:
	@if [ -z "$(GOOGLE_CLOUD_PROJECT_ID)" ]; then \
		echo "Error: GOOGLE_CLOUD_PROJECT_ID is not set. Please set it as an environment variable or pass it as an argument."; \
		exit 1; \
	fi
	@if [ -z "$(VAIS_ENGINE_ID)" ]; then \
		echo "Error: VAIS_ENGINE_ID is not set. Please set it as an environment variable or pass it as an argument."; \
		exit 1; \
	fi
	@echo "--- Starting Vertex AI Search MCP (local) ---"
	@echo "Configuration:"
	@echo "  GOOGLE_CLOUD_PROJECT_ID         : $(GOOGLE_CLOUD_PROJECT_ID)"
	@echo "  VAIS_ENGINE_ID                  : $(VAIS_ENGINE_ID)"
	@echo "  VAIS_LOCATION                   : $(VAIS_LOCATION)"
	@echo "  PAGE_SIZE                       : $(PAGE_SIZE)"
	@echo "  MAX_EXTRACTIVE_SEGMENT_COUNT    : $(MAX_EXTRACTIVE_SEGMENT_COUNT)"
	@echo "  Additional ARGS to uv run       : $(ARGS)"
	@echo "---"
	# Set environment variables (these can be picked up by os.environ in Python).
	# Then, run the command, passing parameters also as CLI arguments (as in entrypoint.sh).
	PYTHONPATH=src \
	GOOGLE_CLOUD_PROJECT_ID="$(GOOGLE_CLOUD_PROJECT_ID)" \
	VAIS_ENGINE_ID="$(VAIS_ENGINE_ID)" \
	VAIS_LOCATION="$(VAIS_LOCATION)" \
	PAGE_SIZE="$(PAGE_SIZE)" \
	MAX_EXTRACTIVE_SEGMENT_COUNT="$(MAX_EXTRACTIVE_SEGMENT_COUNT)" \
	uv run -m vais-mcp.server \
	    --google-cloud-project-id "$(GOOGLE_CLOUD_PROJECT_ID)" \
	    --vais-engine-id "$(VAIS_ENGINE_ID)" \
	    --vais-location "$(VAIS_LOCATION)" \
	    --page-size "$(PAGE_SIZE)" \
	    --max-extractive-segment-count "$(MAX_EXTRACTIVE_SEGMENT_COUNT)" \
	    $(ARGS)

# Example usage:
#   make run GOOGLE_CLOUD_PROJECT_ID=my-project VAIS_ENGINE_ID=my-engine
#   export GOOGLE_CLOUD_PROJECT_ID=my-project; export VAIS_ENGINE_ID=my-engine; make run
#   make run GOOGLE_CLOUD_PROJECT_ID=my-project VAIS_ENGINE_ID=my-engine ARGS="--reload" (Uvicorn's --reload flag)

.PHONY: help
help:
	@echo "Available targets:"
	@echo "  run       - Run the Vertex AI Search MCP application with current configuration."
	@echo "              Mandatory: GOOGLE_CLOUD_PROJECT_ID, VAIS_ENGINE_ID (set via env or arg)."
	@echo "              Override optional variables: make run VAR=value"
	@echo "              Pass additional args: make run ARGS=\\"--option\\""
	@echo "  help      - Show this help message."

# Set 'help' as the default target
.DEFAULT_GOAL := help 
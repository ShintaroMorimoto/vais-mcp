#!/bin/sh

# Check for mandatory environment variables
if [ -z "$GOOGLE_CLOUD_PROJECT_ID" ]; then
  echo "Error: GOOGLE_CLOUD_PROJECT_ID environment variable is not set." >&2
  exit 1
fi

if [ -z "$VAIS_ENGINE_ID" ]; then
  echo "Error: VAIS_ENGINE_ID environment variable is not set." >&2
  exit 1
fi

# Optional environment variables with defaults for the script's execution logic
# These are passed as arguments to the final command
_VAIS_LOCATION="${VAIS_LOCATION:-global}"
_PAGE_SIZE="${PAGE_SIZE:-5}"
_MAX_EXTRACTIVE_SEGMENT_COUNT="${MAX_EXTRACTIVE_SEGMENT_COUNT:-2}"

# The exec command will replace the shell process with the uv run command.
# Environment variables (like GOOGLE_CLOUD_PROJECT_ID) are inherited by the new process.
exec uv run vais-mcp \ 
    --google-cloud-project-id "$GOOGLE_CLOUD_PROJECT_ID" \ 
    --vais-engine-id "$VAIS_ENGINE_ID" \ 
    --vais-location "$_VAIS_LOCATION" \ 
    --page-size "$_PAGE_SIZE" \ 
    --max-extractive-segment-count "$_MAX_EXTRACTIVE_SEGMENT_COUNT" "$@" 
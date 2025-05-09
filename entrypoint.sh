#!/bin/sh

# 環境変数が設定されていなければデフォルト値を使用
GOOGLE_CLOUD_PROJECT_ID="${GOOGLE_CLOUD_PROJECT_ID:-default_project_id}"
VAIS_ENGINE_ID="${VAIS_ENGINE_ID:-default_engine_id}"
VAIS_LOCATION="${VAIS_LOCATION:-global}"
PAGE_SIZE="${PAGE_SIZE:-5}"
MAX_EXTRACTIVE_SEGMENT_COUNT="${MAX_EXTRACTIVE_SEGMENT_COUNT:-2}"

exec uv run vais-mcp \ 
    --google-cloud-project-id "$GOOGLE_CLOUD_PROJECT_ID" \ 
    --vais-engine-id "$VAIS_ENGINE_ID" \ 
    --vais-location "$VAIS_LOCATION" \ 
    --page-size "$PAGE_SIZE" \ 
    --max-extractive-segment-count "$MAX_EXTRACTIVE_SEGMENT_COUNT" "$@" 
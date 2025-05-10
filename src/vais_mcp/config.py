from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GOOGLE_CLOUD_PROJECT_ID: str
    IMPERSONATE_SERVICE_ACCOUNT: str | None = None

    VAIS_ENGINE_ID: str
    VAIS_LOCATION: str = "global"
    PAGE_SIZE: int = 5
    MAX_EXTRACTIVE_SEGMENT_COUNT: int = 2

    MCP_PORT: int = 8000
    MCP_HOST: str = "0.0.0.0"

    model_config = SettingsConfigDict(extra="ignore")


# Auto-validation of required fields
settings = Settings()

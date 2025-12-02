from pydantic_settings import BaseSettings
from typing import List
from pydantic import Field


class Settings(BaseSettings):
    """Application settings and configuration."""
    
    # API Metadata
    app_name: str = "ECW API"
    app_description: str = "ECW Development API"
    app_version: str = "1.0.0"
    
    # Server Configuration
    host: str = "0.0.0.0"
    port: int = 8000
    
    # CORS Configuration
    # In .env file, use JSON array format: ALLOWED_ORIGINS=["*"] or ["http://localhost:3000", "https://example.com"]
    allowed_origins: List[str] = Field(default=["*"])
    
    # Database Configuration (add as needed)
    # database_url: str = "sqlite:///./ecw.db"
    
    # JWT/Auth Configuration (add as needed)
    # secret_key: str
    # algorithm: str = "HS256"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


# Global settings instance
settings = Settings()

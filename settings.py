from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Manages application settings by loading them from a .env file.
    """
    db_user: str
    db_password: str
    db_tns_name: str

    # This tells Pydantic to look for a .env file
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# Create a single, reusable instance of the settings
settings = Settings()
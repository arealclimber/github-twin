from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8")

    MONGO_DATABASE_HOST: str = (
        "mongodb://mongo1:27017,mongo2:27018,mongo3:27019/"
        # ?replicaSet=my-replica-set
    )
    MONGO_DATABASE_NAME: str = "scrabble"

    GITHUB_ORG: str
    GITHUB_USER: str
    GITHUB_TOKEN: str

    # # Optional LinkedIn credentials for scraping your profile
    # LINKEDIN_USERNAME: str | None = "Shirley"
    # LINKEDIN_PASSWORD: str | None = "Shirley"


settings = Settings()

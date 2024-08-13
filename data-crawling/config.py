from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8")

    MONGO_DATABASE_HOST: str = (
        "mongodb://localhost:27017"
        # "mongodb://mongo1:30001,mongo2:30002,mongo3:30003/?replicaSet=my-replica-set"
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

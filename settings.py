from pydantic import BaseSettings


class DeckAppConfig(BaseSettings):
    DECK_CODE = ""

    class Config:
        env_file = ".env"
        env_prefix = "DK_"


settings = DeckAppConfig()

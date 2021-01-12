from pydantic import BaseSettings


class Settings(BaseSettings):
    GITLAB_URL: str = 'https://gitlab.olxbr.io/'
    GITLAB_GROUP: str = 'messaging'
    GITLAB_TOKEN: str
    GITLAB_PER_PAGE: int = 100

    OUTPUT_PATH: str = "output/"

    MAX_CONCURRENCY: int = 4

    @property
    def pagination_config(self):
        return dict(per_page=self.GITLAB_PER_PAGE)


settings = Settings()
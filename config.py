import os
from typing import Literal
from pydantic_settings import BaseSettings

BASE_DIR = os.path.dirname(__file__)


class Config(BaseSettings):
    login: str
    password: str
    browser_url: str
    context: Literal['local', 'remote'] = 'local'
    browser_name: Literal['chrome', 'firefox'] = 'chrome'
    base_url: str = "https://innowise-group.com/"
    window_width: int = 1900
    window_height: int = 1000
    headless: bool = False


config = Config(_env_file=os.path.join(BASE_DIR, '.env'))

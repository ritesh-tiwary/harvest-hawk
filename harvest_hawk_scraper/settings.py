import json
import configparser
from typing import ClassVar
from pydantic import Field, validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    config_parser: ClassVar[configparser.ConfigParser] = configparser.ConfigParser()
    config_parser.read("scrapy.cfg")
    urls_config: str = config_parser.get("env", "URLS_CONFIG", fallback=None)
    urls: list = Field(default_factory=list)    

    @validator("urls", pre=True, always=True)
    def load_urls(cls, v):
        if isinstance(v, dict): return v
        with open(cls.__fields__["urls_config"].default) as f:
            return json.load(f)

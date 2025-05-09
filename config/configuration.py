import configparser
from os.path import abspath, dirname, join
from pydantic import BaseModel


class DBConfig(BaseModel):
    host: str
    port: int
    user: str
    password: str


config = configparser.RawConfigParser()
config.read(join(abspath(dirname(__file__)), 'conf'), encoding='utf-8')

postgres = DBConfig(**config["db"])

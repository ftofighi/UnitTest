# """
# This is the Django project setting file
# """
# from functools import lru_cache
# from pydantic import BaseSettings

# class Settings(BaseSettings):
#     prject_name: str = "Job Board"
#     project_version: str = "1.0.0"
    
#     postgres_user: str
#     postgres_password: str
#     postgres_server: str
#     postgres_port: str
#     postgres_db: str

#     class Config:
#         env_file = "/.env"
        
        
# @lru_cache()
# def get_settings():
#     return Settings()


# settings = get_settings()
    
    
# """
# Creating new object from class Setting
# """
# settings = Settings()

import os
from functools import lru_cache
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
    POSTGRES_DB : str = os.getenv("POSTGRES_DB")
    
@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
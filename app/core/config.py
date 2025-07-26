from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    API_KEY = os.getenv("API_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")
    ZENO_PAY_API = os.getenv("ZENO_PAY_API")
    ZENO_PAY_WEBHOOK = os.getenv("ZENO_PAY_WEBHOOK")

settings = Settings()

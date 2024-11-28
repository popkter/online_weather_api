from dotenv import load_dotenv
import os

load_dotenv()

CHAT_API_KEY = os.getenv("CHAT_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

WEATHER_PORT = 10011

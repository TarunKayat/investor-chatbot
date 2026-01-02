import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("API"))

model = genai.GenerativeModel("gemini-2.5-flash")

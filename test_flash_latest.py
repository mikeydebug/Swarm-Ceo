import asyncio
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv('backend/.env')
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-latest")

async def test():
    try:
        response = await model.generate_content_async("Say hello")
        print("Success:", response.text)
    except Exception as e:
        print("Error:", e)

asyncio.run(test())

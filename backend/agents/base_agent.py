import google.generativeai as genai
import os
import json
import logging
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(
    "gemini-1.5-flash",
    generation_config={"response_mime_type": "application/json"}
)

async def call_gemini(prompt: str) -> dict:
    try:
        response = await model.generate_content_async(prompt)
        text = response.text.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        return json.loads(text.strip())
    except Exception as e:
        import traceback
        traceback.print_exc()
        logging.error(f"Error calling Gemini: {e}")
        return {}

async def call_gemini_text(prompt: str) -> str:
    try:
        text_model = genai.GenerativeModel("gemini-flash-latest")
        response = await text_model.generate_content_async(prompt)
        return response.text
    except Exception as e:
        logging.error(f"Error calling Gemini text: {e}")
        return ""

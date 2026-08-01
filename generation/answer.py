import google.generativeai as genai
import os
from dotenv import load_dotenv
from config import GEMINI_MODEL_NAME

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(GEMINI_MODEL_NAME)


def generate_answer(query , retreived_chunks):

    context_lines = [f"[{i+1}] {chunk}" for i , chunk in enumerate(retreived_chunks)]
    context = "\n".join(context_lines)

    prompt = f"""You are answering questions using ONLY the provided context.
        If the answer isn't in the context, say so clearly instead of guessing.

        Context:
        {context}

        Question: {query}

        Answer the question, and mention which context number(s) you used to answer."""

    response = model.generate_content(prompt)
    return response.text



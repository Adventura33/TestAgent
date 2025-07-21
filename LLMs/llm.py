import os
from dotenv import load_dotenv

# Исправленный импорт
from langchain_ollama import ChatOllama

load_dotenv()

# Использовать локальный LLM через Ollama
LLM = ChatOllama(
    model="Nemo-12B-q8",  # или "llama3", "mistral", "gemma", "kaz-mistral" и т.д. Nemo-12B-q8
    temperature=0.0
)

# LLM = ChatOpenAI(model="gpt-4o-2024-08-06",
#                         temperature=0)


# LLM = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash-exp-0827",
#     temperature=0,
#     )


# FIREWORKS_LLM = ChatFireworks(model="accounts/fireworks/models/llama-v3-70b-instruct")

# OLLAMA_LLM = ChatOllama(model="llama3.1",
#                         temperature=0,
#                         # format="json"
#                         )

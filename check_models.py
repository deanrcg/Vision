from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize the client with API key from .env
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Get list of available models
models = client.models.list()

# Print each model ID
print("Available models:")
print("----------------")
for model in models.data:
    print(model.id) 
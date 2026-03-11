import os
from strands.models.gemini import GeminiModel


def get_model():
    return GeminiModel(
        client_args={"api_key": os.environ["GEMINI_API_KEY"]},
        model_id="gemini-2.5-pro",
        params={"temperature": 0.2, "max_output_tokens": 1024},
    )

import os
from strands.models.gemini import GeminiModel

MODEL_ID = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")


def get_model():
    return GeminiModel(
        client_args={"api_key": os.environ["GEMINI_API_KEY"]},
        model_id=MODEL_ID,
        params={"temperature": 0.2, "max_output_tokens": 1024},
    )

from ollama import AsyncClient

from app.core.config import get_settings


class LLMClient:
    def __init__(self):
        settings = get_settings()

        self.model = settings.ollama_model

        self.client = AsyncClient(
            host=settings.ollama_base_url
        )

    async def generate(self, prompt: str) -> str:
        response = await self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]

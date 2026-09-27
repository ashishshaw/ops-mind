from app.services.llm.client import LLMClient


class ChatService:
    def __init__(self):
        self.llm = LLMClient()

    async def ask(self, message: str) -> str:
        return await self.llm.generate(message)

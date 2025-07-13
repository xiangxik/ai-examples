import asyncio

from llama_index.llms.lmstudio import LMStudio
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.core.workflow import Context

async def main():
    llm = LMStudio(
        model_name="mlx-community/Llama-3.2-3B-Instruct-4bit",
        base_url="http://192.168.101.110:1234/v1",
        temperature=0.7,
    )

    agent = FunctionAgent(llm=llm)
    ctx = Context(agent)

    while True:
        text_input = input("User: ")
        if text_input == "exit":
            break
        response = await agent.run(text_input, ctx=ctx)
        print(f"Agent: {response}")

if __name__ == "__main__":
    asyncio.run(main())
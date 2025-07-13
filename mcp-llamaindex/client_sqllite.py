import asyncio

from llama_index.llms.lmstudio import LMStudio
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.core.workflow import Context
from llama_index.tools.mcp import BasicMCPClient, McpToolSpec

async def main():
    llm = LMStudio(
        model_name="mlx-community/Qwen2.5-7B-Instruct-GGUF",
        base_url="http://192.168.101.110:1234/v1",
        temperature=0.7,
    )

    mcp_client = BasicMCPClient("http://127.0.0.1:8000/sse")
    mcp_tools = McpToolSpec(client=mcp_client) # you can also pass list of allowed tools

    tools = await mcp_tools.to_tool_list_async()
    for tool in tools:
        print(tool.metadata.name, tool.metadata.description)

    agent = FunctionAgent(tools=tools, llm=llm)
    ctx = Context(agent)
    while True:
        text_input = input("User: ")
        if text_input == "exit":
            break
        response = await agent.run(text_input, ctx=ctx)
        print(f"Agent: {response}")

if __name__ == "__main__":
    asyncio.run(main())
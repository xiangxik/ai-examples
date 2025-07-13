import asyncio
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

load_dotenv()

async def main():
    model = ChatOpenAI(base_url="http://192.168.101.110:1234/v1",
        model="mlx-community/Qwen2.5-7B-Instruct-GGUF",
        api_key="not-needed")
    
    client = MultiServerMCPClient(
        {
            "Weather": {
                "url": "http://127.0.0.1:8000/sse",
                "transport": "sse",
            },
            "Math": {
                "url": "http://127.0.0.1:8001/sse",
                "transport": "sse",
            }
        }
    )
    agent = create_react_agent(
        model,
        await client.get_tools()
    )

    weather_response = await agent.ainvoke({"messages": [{"role": "user", "content": "What is the weather in New York?"}]})
    print("Weather Response: ", weather_response["messages"])

if __name__ == "__main__":
    asyncio.run(main())
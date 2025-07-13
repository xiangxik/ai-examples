import asyncio
from llama_index.tools.mcp import BasicMCPClient

async def main():
    # Connect to an MCP server using different transports
    http_client = BasicMCPClient("https://example.com/mcp")  # Streamable HTTP
    # sse_client = BasicMCPClient("http://127.0.0.1:8000/sse")  # Server-Sent Events
    #local_client = BasicMCPClient("python", args=["server.py"])  # stdio

    # List available tools
    tools = await http_client.list_tools()
    print("Available tools:")
    for tool in tools.tools:
        print(f"- {tool.name}: {tool.description}")

    # Call a tool
    result = await http_client.call_tool("add_data", {"name": "John Doe", "age": 30, "profession": "Engineer"})
    print(f"Result of tool call: {result}")

    # List available resources
    resources = await http_client.list_resources()
    print("Available resources:")
    for resource in resources:
        print(f"- {resource.metadata.name}: {resource.metadata.description}")

    # Read a resource
    content, mime_type = await http_client.read_resource("config://app")
    print(f"Content of resource 'config://app': {content} (MIME type: {mime_type})")

    # List available prompts
    prompts = await http_client.list_prompts()
    print("Available prompts:")
    for prompt in prompts:
        print(f"- {prompt.name}: {prompt.description}")

    # Get a prompt
    prompt_result = await http_client.get_prompt("greet", {"name": "World"})
    print(f"Prompt result: {prompt_result}")

if __name__ == "__main__":
    asyncio.run(main())
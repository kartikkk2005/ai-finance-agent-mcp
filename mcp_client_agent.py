import asyncio

from mcp.client.stdio import stdio_client
from mcp.client.session import ClientSession
from mcp import StdioServerParameters


async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["mcp_server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("\n✅ Connected to Finance MCP Server!\n")

            tools = await session.list_tools()
            print("🧰 Available tools:")
            for t in tools.tools:
                print("-", t.name)

            result = await session.call_tool(
                "get_summary",
                {"file_path": "data/bank_export.csv"}
            )

            print("\n📊 Summary from MCP tool:\n")
            print(result)


if __name__ == "__main__":
    asyncio.run(main())

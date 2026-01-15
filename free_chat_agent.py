import asyncio
import json
import ollama

from mcp.client.stdio import stdio_client
from mcp.client.session import ClientSession
from mcp import StdioServerParameters

MODEL = "llama3.2:3b"

async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["mcp_server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("\n✅ FREE Finance Agent ready (Ollama + MCP)")
            print("Ask question (type exit to stop)\n")

            while True:
                q = input("You: ").strip()
                if q.lower() in ["exit", "quit"]:
                    break

                tool_prompt = f"""
You are a finance assistant.
User question: {q}

Choose ONE tool:
- get_summary(file_path)
- get_savings_tips(file_path)
- load_and_categorize(file_path)

Respond ONLY JSON like:
{{"tool":"get_summary","args":{{"file_path":"data/bank_export.csv"}}}}
"""

                tool_choice = ollama.chat(
                    model=MODEL,
                    messages=[{"role": "user", "content": tool_prompt}]
                )["message"]["content"]

                try:
                    decision = json.loads(tool_choice)
                    tool_name = decision["tool"]
                    tool_args = decision["args"]

                    tool_result = await asyncio.wait_for(
                    session.call_tool(tool_name, tool_args),
                    timeout=20
)


                    final_prompt = f"""
User asked: {q}

Tool used: {tool_name}
Tool output: {tool_result.content}

Now explain simply and give advice.
"""

                    final = ollama.chat(
                        model=MODEL,
                        messages=[{"role": "user", "content": final_prompt}]
                    )["message"]["content"]

                    print("\nAgent:", final, "\n")

                except Exception:
                    print("\n⚠️ Tool selection failed.")
                    print("Model output:\n", tool_choice, "\n")

if __name__ == "__main__":
    asyncio.run(main())

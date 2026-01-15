from mcp.server.fastmcp import FastMCP
from tools.expense_reader import read_expenses
from tools.categorizer import categorize_expense
from tools.analyzer import analyze_expenses
from tools.savings_planner import suggest_savings

mcp = FastMCP("finance-agent")

@mcp.tool()
def load_and_categorize(file_path: str = "data/bank_export.csv"):
    expenses = read_expenses(file_path)
    for e in expenses:
        e["category"] = categorize_expense(e)
    return expenses

@mcp.tool()
def get_summary(file_path: str = "data/bank_export.csv"):
    expenses = read_expenses(file_path)
    for e in expenses:
        e["category"] = categorize_expense(e)
    summary = analyze_expenses(expenses)
    return summary

@mcp.tool()
def get_savings_tips(file_path: str = "data/bank_export.csv"):
    expenses = read_expenses(file_path)
    for e in expenses:
        e["category"] = categorize_expense(e)
    summary = analyze_expenses(expenses)
    tips = suggest_savings(summary)
    return tips

if __name__ == "__main__":
    mcp.run()

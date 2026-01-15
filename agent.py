from tools.expense_reader import read_expenses
from tools.categorizer import categorize_expense
from tools.analyzer import analyze_expenses
from tools.savings_planner import suggest_savings

expenses = read_expenses("data/bank_export.csv")

for e in expenses:
    e["category"] = categorize_expense(e)

summary = analyze_expenses(expenses)
tips = suggest_savings(summary)

print("\n✅ Categorized Transactions:\n")
for e in expenses:
    print(e)

print("\n📊 Summary:\n")
for k, v in summary.items():
    print(f"{k}: {v}")

print("\n💡 Savings Tips:\n")
for t in tips:
    print("-", t)

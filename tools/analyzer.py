def analyze_expenses(expenses):
    summary = {}

    for e in expenses:
        category = e["category"]
        amount = float(e["amount"])
        summary[category] = summary.get(category, 0) + amount

    return summary

def categorize_expense(expense):
    description = expense["description"].lower()

    if "swiggy" in description or "zomato" in description:
        return "Food"
    if "uber" in description or "ola" in description:
        return "Transport"
    if "bill" in description or "electricity" in description:
        return "Utilities"
    if "amazon" in description or "flipkart" in description:
        return "Shopping"
    if "netflix" in description or "subscription" in description:
        return "Subscriptions"
    if "salary" in description:
        return "Income"

    return "Others"

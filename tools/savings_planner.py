def suggest_savings(summary):
    tips = []

    food = summary.get("Food", 0)
    shopping = summary.get("Shopping", 0)
    subs = summary.get("Subscriptions", 0)

    if food > 3000:
        tips.append("Reduce food delivery spending (Swiggy/Zomato).")

    if shopping > 3000:
        tips.append("Limit shopping and impulse purchases.")

    if subs > 1000:
        tips.append("Review subscriptions and cancel unused ones.")

    tips.append("Try to follow 50/30/20 rule: Needs/Wants/Savings.")

    return tips

def performance_indicator(score):
    if score >= 75:
        return "Excellent"
    elif score >= 65:
        return "Very Good"
    elif score >= 55:
        return "Good"
    elif score >= 45:
        return "Average"
    else:
        return "Below Average"

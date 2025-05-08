def get_suggestions(disease_name):
    # Simple example suggestions (you can expand this)
    suggestions = {
        0: "Use anti-inflammatory cream. Apply thrice a day.",
        1: "Try applying hydrocortisone ointment for relief.",
        2: "Keep the area moisturized. Avoid scratching.",
        3: "Consult a dermatologist for proper diagnosis.",
        4: "Use antifungal powder and avoid wet areas."
    }
    
    return suggestions.get(disease_name, "No suggestions available.")

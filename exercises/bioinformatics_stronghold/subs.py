def substring_match(text, substr):
    """Find all locations of a substring in a string."""
    return [i+1 for i in range(len(text)) if text[i:i+len(substr)] == substr]
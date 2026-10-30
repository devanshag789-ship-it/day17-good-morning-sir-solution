def get_greeting(hour):
    """Return a greeting based on the hour of the day."""

    if not isinstance(hour, int) or not 0 <= hour <= 23:
        raise ValueError("Hour must be an integer between 0 and 23.")

    if hour < 12:
        return "Good Morning Sir"
    elif hour < 16:
        return "Good Afternoon Sir"
    elif hour < 21:
        return "Good Evening Sir"
    else:
        return "Good Night Sir"

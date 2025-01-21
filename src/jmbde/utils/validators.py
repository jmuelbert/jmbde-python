import re


def validate_email(email: str) -> bool:
    """
    Validate email format.

    Args:
    ----
        email: Email address to validate

    Returns:
    -------
        bool: True if email is valid

    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """
    Validate phone number format.

    Args:
    ----
        phone: Phone number to validate

    Returns:
    -------
        bool: True if phone number is valid

    """
    pattern = r"^\+?[\d\s-]{10,}$"
    return bool(re.match(pattern, phone))

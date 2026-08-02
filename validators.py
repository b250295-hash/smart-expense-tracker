def validate_amount(amount):
    """
    Validate the expense amount.
    Returns True if valid, otherwise False.
    """
    try:
        amount = float(amount)
        return amount > 0
    except (ValueError, TypeError):
        return False


def validate_category(category):
    """
    Validate the expense category.
    """
    return isinstance(category, str) and category.strip() != ""


def validate_description(description):
    """
    Validate the expense description.
    Description is optional but should not exceed 200 characters.
    """
    if description is None:
        return True

    return len(description.strip()) <= 200


def validate_expense(date, category, amount, description):
    """
    Validate all expense fields.
    Returns (True, "Valid") if all fields are valid.
    """
    if not validate_category(category):
        return False, "Please select a valid category."

    if not validate_amount(amount):
        return False, "Amount must be greater than 0."

    if not validate_description(description):
        return False, "Description should not exceed 200 characters."

    return True, "Valid"
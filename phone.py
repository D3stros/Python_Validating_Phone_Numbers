import re

# Returns the first phone number


def extract_phone(input):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

# Returns all phone numbers in a list


def extract_all_phones(input):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    return phone_regex.findall(input)

# Checking if entire string is valid phone number


def is_valid_phone(input):
    phone_regex = re.compile(r"^\d{3} \d{3}-\d{4}$")
    match = phone_regex.search(input)
    if match:
        return True
    return False

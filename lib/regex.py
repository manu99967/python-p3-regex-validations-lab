import re

# Name regex:
# - Start with uppercase, then lowercase letters
# - Allow optional parts with space, hyphen, or apostrophe followed by capitalized word
# - Handles "John Cena", "Anya Taylor-Joy", "D'Angelo"
name_regex = re.compile(
    r"^[A-Z][a-z]*(?:[ -][A-Z][a-z]+|['’][A-Z][a-z]+)*$"
)

# Phone regex:
# Matches:
#   5555555555
#   555-555-5555
#   (555) 555-5555
phone_regex = re.compile(
    r"^(?:\(\d{3}\)\s?|\d{3}-?)\d{3}-?\d{4}$"
)

# Email regex:
# - Starts with a letter
# - Allows letters, digits, and dots before @
# - Requires @ + domain + TLD
email_regex = re.compile(
    r"^[A-Za-z][A-Za-z0-9.]*@[A-Za-z]+\.[A-Za-z]+$"
)

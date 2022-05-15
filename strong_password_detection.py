import re


def is_strong_password(password: str) -> bool:
    lower_case_alpha = re.compile(r'([a-z]+)')
    upper_case_alpha = re.compile(r'([A-Z]+)')
    digits = re.compile(r'([0-9]+)')
    special_chars = re.compile(r'([@#$%^&*!]+)')
    regTup = (lower_case_alpha, upper_case_alpha, digits, special_chars)
    if len(password) >= 8:
        for regexp in regTup:
            if not regexp.findall(password):
                return False
        return True
    return False


print(is_strong_password('Aabaaaaaaa123sssss'))

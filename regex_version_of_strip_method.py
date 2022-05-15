import re


def strip_string(string: str, chars='') -> bool:
    if chars:
        string = string.strip()
        string_regex = re.compile(chars)
        return string_regex.sub('', string)
    strip_regex = re.compile(r'\S[\d\w\s]*\S')
    match_obj = strip_regex.findall(string)

    return ''.join(match_obj)


print(strip_string(' ab c',"c"))

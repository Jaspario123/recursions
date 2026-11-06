import string

def is_palindrome(text: str) -> bool:
    def _is_palindrome_recursive(clean_text: str) -> bool:
        if len(clean_text) <= 1:
            return True
        if clean_text[0] != clean_text[-1]:
            return False
        return _is_palindrome_recursive(clean_text[1:-1])
    allowed_chars = set(string.ascii_lowercase + string.digits)
    cleaned = "".join(char for char in text.lower() if char in allowed_chars)
    return _is_palindrome_recursive(cleaned)
print(is_palindrome("racecar"))
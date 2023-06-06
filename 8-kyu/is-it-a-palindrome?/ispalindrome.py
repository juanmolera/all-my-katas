def is_palindrome(s):
    return 1 if s.lower() == s.lower()[::-1] else 0
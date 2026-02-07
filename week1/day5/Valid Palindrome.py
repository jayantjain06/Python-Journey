def isPalindrome(s):
    s=s.lower()
    clean=""
    for ch in s:
        if ch.isalnum():
            clean = clean+ch

    return clean == clean[::-1]

print(isPalindrome(s = "race a car"))

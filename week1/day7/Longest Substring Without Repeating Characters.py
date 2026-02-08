def lengthOfLongestSubstring(s):
    L=0
    max_len=0
    seen=set()
    for R in range(len(s)):
        while s[R] in seen:
            seen.remove(s[L])
            L+=1
        seen.add(s[R])
        max_len=max(max_len , R-L+1)

    return max_len

print(lengthOfLongestSubstring(s = "abcabcbb"))
from collections import defaultdict

def groupAnagrams(strs):
    groups = defaultdict(list)

    for word in strs:
        count = [0] * 26
        
        for ch in word:
            count[ord(ch) - ord('a')] += 1
        
        key = tuple(count)
        groups[key].append(word)

    return list(groups.values())
print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
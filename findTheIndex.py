#Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""
Finds the index of the first occurrence of the needle in the haystack.

        Args:
            haystack: The larger string to search within.
            needle: The smaller string to search for.

        Returns:
            The index of the first occurrence of the needle in the haystack,
            or -1 if the needle is not found.
"""
class findTheIndex:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        for i in range(len(haystack) + 1 -len(needle)):
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i 
        return -1
index = findTheIndex()


haystack = "sadbutsad"
needle = "sad"
results = index.strStr(haystack, needle)
print(results)  # Output: 0

haystack = "leetcode"
needle = "leeto"
results = index.strStr(haystack, needle)
print(results)  # Output: -1
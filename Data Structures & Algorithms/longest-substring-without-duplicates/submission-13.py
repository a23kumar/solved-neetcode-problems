class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # neet to have a way to track chars in substring

        # we can create a for loop that iterates through the entire string
        # when we reach a duplicate char, we truncate the end chars untill no duplicate
        seen = set()
        l = 0
        max_len = 0

        for r, c in enumerate(s):
            if c in seen:
                while True:
                    left_char = s[l]
                    l += 1
                    if left_char == c:
                        break
                    seen.remove(left_char)
            else:
                seen.add(c)
                max_len = max(max_len, r - l + 1)

        return max_len
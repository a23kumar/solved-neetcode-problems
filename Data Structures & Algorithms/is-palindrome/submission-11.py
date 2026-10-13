class Solution:
    def isPalindrome(self, s: str) -> bool:
        # a string of even length is a palindrone if starting at the center two and expanding outwards with left and right
        # pointers is the same char at each expansion
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        print(s)
        mid = len(s) // 2
        if len(s) % 2 == 0:
            print('hi')
            l, r = mid - 1, mid
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    return False
        else:
            print('bye')
            l, r = mid, mid
            while l >= 0 and r <= len(s) - 1:
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    return False
        return True
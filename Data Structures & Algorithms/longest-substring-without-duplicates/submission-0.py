class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_len = 0
        
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
                
            char_set.add(s[r])
            current_len = r - l + 1
            if current_len > max_len:
                max_len = current_len
                
        return max_len
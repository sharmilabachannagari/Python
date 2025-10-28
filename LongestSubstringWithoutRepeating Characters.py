class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}  # Stores the last seen index of characters
        left = 0  # Left pointer of the sliding window
        max_len = 0  # Result

        for right in range(len(s)):
            if s[right] in char_index and char_index[s[right]] >= left:
                # If character is repeated and inside the window, move left pointer
                left = char_index[s[right]] + 1

            char_index[s[right]] = right  # Update the last seen index
            max_len = max(max_len, right - left + 1)  # Update max length

        return max_len

        

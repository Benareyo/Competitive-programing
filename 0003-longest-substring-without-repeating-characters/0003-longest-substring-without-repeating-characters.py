class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize pointers and variables
        left = 0
        max_length = 0
        char_set = set()
        
        # Traverse the string with the right pointer
        for right in range(len(s)):
            # If the character is in the set, remove characters from the left until it's not
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # Add the current character to the set
            char_set.add(s[right])
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
        
        return max_length

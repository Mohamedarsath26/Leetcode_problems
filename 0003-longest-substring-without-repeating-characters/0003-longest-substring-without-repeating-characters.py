class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = 0
        max_length = 0
        st = [] 

        for i in range(len(s)):
            while s[i] in st:
                st.remove(st[0])  # Remove the first character
            st.append(s[i])  # Add the new character
            max_length = max(max_length, len(st))  # Update max length
        
        return max_length  

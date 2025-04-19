class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]

        res = ''

        for i in range(len(prefix)):
            current_char = prefix[i]

            for word in strs[1:]:
                if i >= len(word) or word[i] != current_char:
                    return res

            res += current_char
        
        return res

    


            



        
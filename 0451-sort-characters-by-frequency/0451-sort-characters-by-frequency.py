class Solution:
    def frequencySort(self, s: str) -> str:

        list_str = []
        
        dict_char = {}

        for char in s:
            if char in dict_char:
                dict_char[char] += 1
            else:
                dict_char[char] = 1
        
        des_char = dict(sorted(dict_char.items() ,key = lambda item: item[1],reverse=True))

        for char,count in des_char.items():
            list_str.append(char*count)
        return ''.join(list_str)

        
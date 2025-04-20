class Solution:
    def frequencySort(self, s: str) -> str:

        list_str = []

        sorted_char = Counter(s).most_common() ## returns the tuple of char and count

        for char,count in sorted_char:
            list_str.append(char*count)
        return ''.join(list_str)

        
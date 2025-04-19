class Solution:
    def reverseWords(self, s: str) -> str:
        reverse = ' '.join(s.strip().split()[::-1])
        return reverse

        
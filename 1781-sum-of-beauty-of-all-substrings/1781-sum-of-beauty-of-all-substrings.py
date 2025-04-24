class Solution:
    def sum_of_beauty(self,s):
        dict_ = {}
        for i in range(len(s)):
            dict_[s[i]] = dict_.get(s[i],0)+1
        
        max_ = max(dict_,key=dict_.get)
        max_ = dict_[max_]

        min_ = min(dict_,key=dict_.get)
        min_ = dict_[min_]

        beauty = max_ - min_

        return beauty

    def beautySum(self, s: str) -> int:
        high = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                high += self.sum_of_beauty(s[i:j+1])

        return high
    

                

        
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        for ele in nums:
            if ele in dic:
                dic[ele] += 1
            else:
                dic[ele] = 1
        for ele in dic:
            if dic[ele] == 1:
                return ele
        
        

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #nums = ''
        #for i in digits: nums+=str(i)
        nums = ''.join(str(i) for i in digits)
        nums = str(int(nums) + 1)
        return list(nums)
        
        
        
        
        
class Solution:
    '''
    Time : O (N)
    Space: O(1)
    '''
    def singleNumber(self, nums: List[int]) -> int:
        bitmask = 0 
        for num in nums:
            bitmask = bitmask^num
        return bitmask

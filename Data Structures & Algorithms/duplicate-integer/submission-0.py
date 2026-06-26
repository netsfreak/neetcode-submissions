class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cont_dict = {}
        for num in nums:
            if num in cont_dict.keys():
                return True 
            else:
                cont_dict[num] = 1

        return False
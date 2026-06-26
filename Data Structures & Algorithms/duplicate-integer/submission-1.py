class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dic = {}
        for val in nums:
            if val in count_dic.keys():
                return True
            else:
                count_dic[val] =+ 1

        return False
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray = []
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                subarray.append(s)
        subarray.sort()
        return (sum(subarray[left-1:right]) % ((10 ** 9) + 7))
        
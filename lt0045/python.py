class Solution:
    def jump(self, nums: List[int]) -> int:
        visited = ret = cur = 0
        while len(nums) - 1 > cur:
            ret += 1
            tmp = cur
            for n in range(visited, cur + 1):
                tmp = max(n + nums[n], tmp)
            visited, cur = cur, tmp
        return ret
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # have one pointer start on the left
        # another start on the right

        # if the sum of the two pointers is less than the target, move left pointer right
        # if the sum of the two pointer is greater than the target, move right pointer left
        l, r = 0, len(numbers) - 1
        while l < r:
            cur_sum = numbers[l] + numbers[r]

            if cur_sum == target:
                return [l + 1, r + 1]

            if cur_sum < target:
                l += 1
            else:
                r -= 1

        
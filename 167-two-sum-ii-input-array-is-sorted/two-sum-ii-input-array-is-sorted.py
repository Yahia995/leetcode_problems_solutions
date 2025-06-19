class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        ptr1, ptr2 = 0, len(numbers) - 1
        while numbers[ptr1] + numbers[ptr2] != target:
            if numbers[ptr1] + numbers[ptr2] > target:
                ptr2 -= 1
            if numbers[ptr1] + numbers[ptr2] < target:
                ptr1 += 1
        return [ptr1 + 1, ptr2 + 1]
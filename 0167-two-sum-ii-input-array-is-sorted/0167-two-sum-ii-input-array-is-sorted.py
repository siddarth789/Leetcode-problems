from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while True:  # loop until we return
            s = numbers[i] + numbers[j]
            if s == target:
                return [i + 1, j + 1]
            if s > target:
                j -= 1
            else:
                i += 1



        
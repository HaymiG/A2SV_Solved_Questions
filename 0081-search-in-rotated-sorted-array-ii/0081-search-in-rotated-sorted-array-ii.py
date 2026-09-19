import numpy as np
class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        signal = np.array(nums, dtype=np.int32)
        mask = (signal == target)
        return bool(np.any(mask))
        
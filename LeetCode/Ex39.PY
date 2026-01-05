from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:


    """
    res = []
    
    def permute(arr, index, total):
        if total == 0:
            res.append(arr[:])
            return
        if total < 0 or index >= len(candidates):
            return
        arr.append(candidates[index])
        permute(arr, index, total- candidates[index])
        arr.pop()
        permute(arr, index+1, total)
    
    permute([], 0, target)
    return res
    """

candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))

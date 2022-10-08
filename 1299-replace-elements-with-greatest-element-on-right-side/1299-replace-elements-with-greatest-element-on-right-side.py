class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        for i in reversed(range(len(arr))):
            arr_i = arr[i]
            arr[i] = max_val
            max_val = max(max_val, arr_i)
        
        return arr
            
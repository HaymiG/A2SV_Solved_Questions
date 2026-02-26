class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        def flip(k):
            left = 0 
            right = k - 1
            while left < right:
                arr[left],arr[right] = arr[right],arr[left]
                left += 1
                right -= 1
        for sort in  range(n, 1 ,-1):
            max_num = max(arr[:sort])
            index_m = arr.index(max_num)
            if index_m == sort - 1 :
                continue

            if index_m != 0:
                result.append(index_m + 1)
                flip(index_m + 1)

            result.append(sort)
            flip(sort)

        return result
            
            
        
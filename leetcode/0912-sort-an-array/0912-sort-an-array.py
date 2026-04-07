class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left , right):
            ans=  []
            i , j = 0 , 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    ans.append(left[i])
                    i += 1
                else :
                    ans.append(right[j])
                    j += 1
            ans.extend(left[i:])
            ans.extend(right[j:])
            return ans


        def sorting(nums , left , right):
           
            if right == left :
                return [nums[left]]
            

            mid = left +(right - left) // 2
            left_p = sorting(nums,left,mid)
            right_p= sorting(nums,mid + 1 , right)
            return merge(left_p, right_p)

            
        return sorting(nums , 0 , len(nums)-1)

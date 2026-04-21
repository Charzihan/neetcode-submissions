class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest_right = 0
        for i in range(len(arr)):
            greatest_right = 0
            if i != len(arr)-1:
                for j in range (i+1, len(arr)):
                    if arr[j] > greatest_right:
                        greatest_right = arr[j]
                arr[i] = greatest_right
            else:
                arr[i] = -1
        
        return arr
            
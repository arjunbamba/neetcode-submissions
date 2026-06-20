class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr)):
            if i == len(arr)-1:
                res.append(-1)
                break
            search = arr[i+1:]
            maxElem = max(search)
            res.append(maxElem)

        return res
from typing import List

#Build an Array With Stack Operations
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        insertArr = []

        for i in range(1, n + 1, 1):
            if result == target:
                return insertArr
            elif len(result) > 0 and result[-1] not in target:
                insertArr.append("Pop")
                result.pop()
                result.append(i)
                insertArr.append("Push")
            elif len(result) == len(target):
                insertArr.append("Pop")
                result.pop()
                result.append(i)
                insertArr.append("Push")
            else:
                insertArr.append("Push")
                result.append(i)

        return insertArr


Sol = Solution()
Result = Sol.buildArray([1,2,3,5,6,7,8], 8)
print(Result)
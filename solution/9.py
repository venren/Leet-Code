from typing import List


class Solution:
    def hIndexOrderOfNSolution(self, citations: List[int]) -> int:

        citations = sorted(citations)
        currentCitation = 0
        maxCitation = 0

        if len(citations) == 1 and citations[0] > 0:
            return 1

        for i in range(0,len(citations),1):
            if citations[i] != 0:
                currentCitation = min(len(citations) - i, citations[i])

            if currentCitation > maxCitation:
                maxCitation = currentCitation

        return maxCitation

    def hIndexOrderOfLogNSolution(self, citations: List[int]) -> int:

        citations = sorted(citations)
        currentCitation = 0
        maxCitation = 0

        if len(citations) == 1 and citations[0] > 0:
            return 1

        for i in range(len(citations)-1,-1,-1):

            if citations[i] < maxCitation:
                return maxCitation

            if citations[i] != 0:
                currentCitation = min(len(citations) - i, citations[i])

            if currentCitation > maxCitation:
                maxCitation = currentCitation

        return maxCitation


Sol = Solution()
print(Sol.hIndexOrderOfLogNSolution([3, 0, 6, 1, 5]))  # 3
print(Sol.hIndexOrderOfLogNSolution([1, 100, 1]))  # 1
print(Sol.hIndexOrderOfLogNSolution([10]))  # 1
print(Sol.hIndexOrderOfLogNSolution([0]))  # 0
print(Sol.hIndexOrderOfLogNSolution([11, 15]))  # 2
print(Sol.hIndexOrderOfLogNSolution([0,1,0]))  # 1

from typing import List

# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

#According to the definition of h-index on Wikipedia:
# The h-index is defined as the maximum value of h such that the given researcher has published at least h
# papers that have each been cited at least h times.

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

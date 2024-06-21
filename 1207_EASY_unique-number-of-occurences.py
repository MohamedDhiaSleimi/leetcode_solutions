class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        from collections import defaultdict
        occurences = defaultdict(int)
        for i in arr :
            occurences[i] += 1
        occurences.values()
        temp : list[int] = []
        for i in occurences:
            if occurences[i] in temp:
                return False
            else :
                temp.append(occurences[i])
        return True

arr = [-3,0,1,-3,1,1,1,-3,10,0]
Solution = Solution()
print(arr)
print(Solution.uniqueOccurrences(arr))
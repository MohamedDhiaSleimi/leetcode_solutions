class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        return sum([abs(seats[i]-students[i]) for i in range(len(seats))])

Solution  = Solution()
test_cases : list[list[list[int]]] = [
    [[3,1,5]  ,[2,7,4]  ],
    [[4,1,5,9],[1,3,2,6]],
    [[2,2,6,6],[1,3,2,6]]
]
for i in test_cases:
    print(i,Solution.minMovesToSeat(i[0],i[1]))

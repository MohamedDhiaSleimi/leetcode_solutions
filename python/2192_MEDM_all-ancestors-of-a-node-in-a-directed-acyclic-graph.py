class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        parents: list[list[int]] = [[] for _ in range(n)]
        for parent, child in edges:
            parents[child].append(parent)
        parents_list: list[list[int]] = []
        for i in range(n):
            res: list[int] = []
            visited: set[int] = set()
            self.getparents(i, parents, visited)
            for node in range(n):
                if node in visited and node != i:
                    res.append(node)
            parents_list.append(res)

        return parents_list

    def getparents(self, current, parents, visited_nodes) -> None:
        visited_nodes.add(current)
        for neighbour in parents[current]:
            if neighbour not in visited_nodes:
                self.getparents(neighbour, parents, visited_nodes)


a: Solution = Solution()
test_cases: list[list] = [
    [
        8,
        [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]],
        [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]],
    ],
]
warn_list: list[str] = []
print("_________________________________\n")
for test in test_cases:
    res = a.getAncestors(test[0], test[1])
    print("_________________________________\n")
    print(
        test[-1],
        "\n",
        res,
        " =>",
        res == test[-1],
    )
    print("_________________________________\n")
    if not (res == test[-1]):
        warn_list.append(f"there is an error in \n {test}")

print("_________________________________\n")
if len(warn_list) > 0:
    for warn in warn_list:
        print(warn)
    print("_________________________________\n")

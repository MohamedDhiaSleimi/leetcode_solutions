class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        class unionFind:
            def __init__(self, n: int) -> None:
                self.rep = list(range(n + 1))
                self.comp_size = [1] * (n + 1)
                self.comp = n

            def findRep(self, x: int) -> int:
                if self.rep[x] == x:
                    return x
                self.rep[x] = self.findRep(self.rep[x])
                return self.rep[x]

            def union(self, x: int, y: int) -> int:
                x = self.findRep(x)
                y = self.findRep(y)

                if x == y:
                    return 0

                if self.comp_size[x] > self.comp_size[y]:
                    self.comp_size[x] += self.comp_size[y]
                    self.rep[y] = x
                else:
                    self.comp_size[y] += self.comp_size[x]
                    self.rep[x] = y

                self.comp -= 1
                return 1

            def isConnected(self) -> bool:
                return self.comp == 1

        alice_graph: unionFind = unionFind(n)
        bob_graph: unionFind = unionFind(n)
        needed_edges: int = 0

        for node_type, fro_node, to_node in edges:
            if node_type == 3:
                needed_edges += alice_graph.union(fro_node, to_node) | bob_graph.union(
                    fro_node, to_node
                )

        for node_type, fro_node, to_node in edges:
            if node_type == 1:
                needed_edges += alice_graph.union(fro_node, to_node)
            elif node_type == 2:
                needed_edges += bob_graph.union(fro_node, to_node)

        if alice_graph.isConnected() and bob_graph.isConnected():
            return len(edges) - needed_edges

        return -1


a: Solution = Solution()
test_cases: list[list] = [
    [
        4,
        [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]],
        2,
    ],
    [
        4,
        [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]],
        0,
    ],
    [
        4,
        [[3, 2, 3], [1, 1, 2], [2, 3, 4]],
        -1,
    ],
]
warn_list: list[str] = []
print("_________________________________\n")
for test in test_cases:
    res: int = a.maxNumEdgesToRemove(test[0], test[1])
    print(
        test,
        'got "',
        res,
        '" =>',
        res == test[-1],
    )
    if not (res == test[-1]):
        warn_list.append(f"there is an error in {test}")

print("_________________________________\n")
if len(warn_list) > 0:
    for warn in warn_list:
        print(warn)
    print("_________________________________\n")

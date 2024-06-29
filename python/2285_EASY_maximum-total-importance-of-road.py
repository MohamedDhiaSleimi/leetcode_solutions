class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        values: list[list] = [[i, 0] for i in range(n)]
        for road in roads:
            for node in road:
                values[node][1] += 1
        values.sort(key=lambda x: x[1])
        tempval: dict = {}
        res_counter: int = 1
        for city in values:
            tempval[city[0]] = res_counter
            res_counter += 1
        res_counter = 0
        for road in roads:
            for node in road:
                res_counter += tempval[node]
        return res_counter


# written using my phone gaze upon the most horrendous code you  ever saw hahaha

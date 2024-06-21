class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        n : int = len(bin(max(a,b,c))[2:])
        bin_dict : dict[str:str] = {
            "a" : (bin(a)[2:]).zfill(n) ,
            "b" : (bin(b)[2:]).zfill(n) ,
            "c" : (bin(c)[2:]).zfill(n)
        }
        res : int = 0
        for i in range(n):
            if not int(bin_dict["c"][i]):
                res += int(bin_dict["a"][i]) + int(bin_dict["b"][i])
            else:
    r           if not(int(bin_dict["a"][i]) or int(bin_dict["b"][i])):
                    res += 1
        return res

 
        



a = Solution()
test_cases: list[list[int]] = [[2, 6, 5], [4, 2, 7], [1, 2, 3]]
for i in test_cases:
    print(i, a.minFlips(i[0], i[1], i[2]))

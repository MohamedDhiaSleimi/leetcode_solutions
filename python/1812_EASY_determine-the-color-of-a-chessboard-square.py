class Solution:
    convert : dict[str:int] = {"a" : 1,"b" : 2,"c" : 3,"d" : 4,"e" : 5,"f" : 6,"g" : 7,"h" : 8}
    def squareIsWhite(self, coordinates: str) -> bool:
        x , y = self.convert[coordinates[0]], int(coordinates[1])
        return (x+y)%2 != 0

Solution = Solution()
print(Solution.squareIsWhite("a2"))
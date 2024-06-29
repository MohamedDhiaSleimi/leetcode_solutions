class Solution:
    def firstUniqChar(self, s: str) -> int:
        non_repeats:list = []
        repeat: list = []
        for i in s:
            if i not in repeat:
                if i in non_repeats:
                    non_repeats.remove(i)
                    repeat.append(i)
                else:
                    non_repeats.append(i)
        if non_repeats:
            return s.index(non_repeats[0])
        else :
            return -1

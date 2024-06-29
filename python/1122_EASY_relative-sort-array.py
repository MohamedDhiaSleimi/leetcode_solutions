import random

"""_summary_
it takes two array 
order the element of the first array according to the second array
order the remaining elements in acsending aorder at the end
restrictions:
    all element in thhe second array exist in the first one 
    the second array elements are non repeating
"""

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        res :list[int] = []
        for i in arr2 :
            while i in arr1 :
                res.append(i)
                arr1.remove(i)
        arr1.sort()
        res.extend(arr1)
        return res

        
def generate_arrays(size_arr2, size_arr1, range_min, range_max):
    if size_arr2 > size_arr1:
        raise ValueError("size_arr2 must be less than or equal to size_arr1")
    
    arr2 = random.sample(range(range_min, range_max + 1), size_arr2)
    
    arr1 = arr2.copy()
    
    additional_elements_needed = size_arr1 - size_arr2
    arr1.extend(random.choices(range(range_min, range_max + 1), k=additional_elements_needed))
    
    random.shuffle(arr1)
    
    return arr1, arr2

arr1, arr2 = generate_arrays(size_arr2=5, size_arr1=10, range_min=1, range_max=20)
print("arr1:", arr1)
print("arr2:", arr2)

Solution = Solution()
print(Solution.relativeSortArray(arr1,arr2))
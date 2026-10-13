from typing import List, Tuple
from functools import reduce

def sum_3_integers(triplet: List[int]) -> int:
    return reduce(lambda result, current: result + current, triplet)


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    x, y, z = box_dimensions
    return x * y * z
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))

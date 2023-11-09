import random
from typing import List


def d(d_faces: int) -> int:

    return random.randint(1, d_faces)

# POO d6 = new d(6)
d6 = lambda: d(6)


def generate_n_d(n: int, d_faces: int) -> List[int]:

    return [d(d_faces) for _  in range(0, n)]


def sum_n_d(n, d_faces):

    return sum(generate_n_d(n, d_faces))


def greatest_from_n_d(n, d_faces):

    return max(generate_n_d(n, d_faces))

def calculate_probability_for_faces_of_greater_in_n():
    pass

def calculate_probability_for_faces_of_least_in_n():
    pass

def least_from_n_d(n, d_faces):

    return min(generate_n_d(n, d_faces))



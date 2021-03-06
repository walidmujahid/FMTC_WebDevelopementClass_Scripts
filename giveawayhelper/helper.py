"""TODO: Docstring"""
from random import sample


def tokenise_students(students: list):
    """Returns a dict where a unique random number is assigned to a student."""
    population_of_class = sample(range(1, len(students)+1), len(students))

    return dict(zip(population_of_class, students))


if __name__ == '__main__':
    pass

"""TODO: Docstring"""
from random import sample


def tokenise_students(students: list):
    """Returns a dict where a unique random number is assigned to a student."""
    return dict(zip(sample(range(1, len(students)+1), len(students)), students))


if __name__ == '__main__':
    pass
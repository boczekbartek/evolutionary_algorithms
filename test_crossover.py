import crossover
import pytest


@pytest.mark.parametrize(
    "parent1,parent2,child1,child2", [
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [9, 3, 7, 8, 2, 6, 5, 1, 4],
            [1, 3, 7, 4, 2, 6, 5, 8, 9],
            [9, 2, 3, 8, 5, 6, 7, 1, 4],
        )
    ]
)
def test_cycle(parent1, parent2, child1, child2):
    _child1, _child2 = crossover.cycle(parent1, parent2)
    assert _child1 == child1
    assert _child2 == child2
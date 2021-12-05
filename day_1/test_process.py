import pytest
from . import process



@pytest.mark.parametrize(
    "input_numbers, expected",
    [
        ([1, 2, 3, 4, 5], 4),
        ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 7),
        ([4, 3, 5, 7, 6], 2),
        ([1, 1, 1, 1], 0),
        ([5, 4, 3, 2, 1], 0),
        ([1, 2, 3, 4, 5], 4)
    ]
)
def test_increases_count(input_numbers, expected):
    assert process.get_increases_count(input_numbers) == expected


@pytest.mark.parametrize(
    "input_numbers, expected",
    [
        ([1, 2, 3, 4, 5], [6, 9, 12]),
        ([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], [607, 618, 618, 617, 647, 716, 769, 792])
    ]
)
def test_offset_sums(input_numbers, expected):
    assert process.offset_sums(input_numbers, 3) == expected

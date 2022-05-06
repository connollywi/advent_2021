import pytest
from pathlib import Path
from . import binary_diagnostic


@pytest.fixture
def test_report():
    with open(f"{Path(__file__).parent}/test_input.txt", "r") as test_input_file:
        test_report = test_input_file.readlines()
    return [entry.strip('\n') for entry in test_report]


@pytest.mark.parametrize(
    "n,expected",
    [
        (0, "011110011100"),
        (1, "010001010101"),
        (2, "111111110000"),
        (3, "011101100011"),
        (4, "000111100100")
    ]
)
def test_nth_bits(n, expected, test_report):
    bdc = binary_diagnostic.BinaryDiagnostic(test_report)
    actual = bdc.nth_bits(bdc.binary_report, n)
    assert actual == expected


def test_epsilon_gamma_rate(test_report):
    bdc = binary_diagnostic.BinaryDiagnostic(test_report)
    gamma_rate = bdc.gamma_rate
    epsilon_rate = bdc.epsilon_rate
    assert gamma_rate == 22
    assert epsilon_rate == 9
    assert bdc.power_consumption == 198


def test_oxygen_generator_rating(test_report):
    bdc = binary_diagnostic.BinaryDiagnostic(test_report)
    oxygen_generator_rating = bdc.oxygen_generator_rating
    assert oxygen_generator_rating == 23


def test_co2_scrubber_rating(test_report):
    bdc = binary_diagnostic.BinaryDiagnostic(test_report)
    co2_scrubber_rating = bdc.co2_scrubber_rating
    assert co2_scrubber_rating == 10

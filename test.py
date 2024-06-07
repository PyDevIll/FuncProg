from main import process_numbers


def test_process_numbers():
    assert process_numbers([1, 2, 3, 4, 5, -2, -4]) == 20
    assert process_numbers([]) == 0
    assert process_numbers([0]) == 0
    assert process_numbers([1]) == 0
    assert process_numbers([1, 3, 5, 7]) == 0
    assert process_numbers([-2, -4, -6, -8]) == 0

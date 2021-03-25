import sys
import pytest
from is_prime import is_factor, is_prime, count_prime_factors


def test_is_factor():
    message = "{} is{} divisible by {}. Your function returned {}."

    true_tests = ((5412, 123), (4823, 371), (6975, 75), (624, 48), (9681, 3227), (4362, 3), (8502, 4251),
                  (5104, 4), (462, 7), (7110, 90), (3128, 4), (9610, 31), (3030, 101), (7644, 294),
                  (1990, 398), (1745, 1), (5577, 11), (4318, 2159), (2220, 12), (2543, 1))

    for a, b in true_tests:
        assert is_factor(a, b), message.format(a, "", b, False)

    false_tests = ((6890, 5059), (2259, 8304), (2697, 3094), (7702, 6643), (4957, 2694), (8872, 818),
                   (7369, 2772), (332, 718), (7293, 9220), (547, 7763), (5144, 3795), (2388, 9018),
                   (6781, 6152), (4365, 9086), (8492, 1194), (6553, 2871), (6535, 5371), (9712, 310),
                   (1881, 7671), (5360, 8180))

    for a, b in false_tests:
        assert not is_factor(a, b), message.format(a, " not", b, True)


def test_is_factor_return_type():
    message = "The return value of 'is_factor' must be type <class 'bool'>, your function returned a value of type {}."
    for a in range(1, 1000, 23):
        for b in range(5, 10):
            result = type(is_factor(a, b))
            assert result == bool, message.format(result)


def test_is_prime():
    message = "{} is{} a prime number. Your function returned {}."

    true_tests = (14081, 17909, 11117, 9319, 6781, 6329, 719, 6211, 2473, 1877, 11923, 1823,
                  1409, 1187, 83, 17761, 7561, 4051, 5437, 10949, 2)
    for n in true_tests:
        assert is_prime(n), message.format(n, "", False)

    false_tests = (13035, 15547, 8073, 13559, 5921, 12321, 14541, 12543, 14433, 16123, 4005, 12939, 17145,
                   2109, 17415, 13673, 14529, 10917, 9571, 5919, 4)
    for n in false_tests:
        assert not is_prime(n), message.format(n, " not", True)


def test_is_prime_return_type():
    message = "The return value of 'is_prime' must be type <class 'bool'>, your function returned a value of type {}."
    for n in range(5, 1000, 25):
        result = type(is_prime(n))
        assert result == bool, message.format(result)


def test_count_prime_factors():
    message = "{} has {} prime factors: {}. Your function returned {}."
    cpf_tests = (
                (85, 2, ['5', '17']),
                (26, 2, ['2', '13']),
                (11, 1, ['11']),
                (67, 1, ['67']),
                (92, 2, ['2', '23']),
                (17, 1, ['17']),
                (32, 1, ['2']),
                (79, 1, ['79']),
                (91, 2, ['7', '13']),
                (6, 2, ['2', '3']),
                (210, 4, ['2', '3', '5', '7']),
                (7921, 1, ['89']),
                (1935, 3, ['3', '5', '43']),
                (1763, 2, ['41, 43']),
                (2528, 2, ['2', '79']),
                (156, 3, ['2', '3', '13']),
                (2769, 3, ['3', '13', '71']),
                (5749, 1, ['5749']),
                (6261, 2, ['3', '2087']),
                (3647, 2, ['7', '521']),
                (1198, 2, ['2', '599']),
                (5500, 3, ['2', '5', '11']),
                )

    for n, c, f in cpf_tests:
        result = count_prime_factors(n)
        assert result == c, message.format(n, c, ','.join(f), result)


def test_count_prime_factors_return_type():
    message = "The return value of 'count_prime_factors' must be type <class 'int'>," + \
        " your function returned a value of type {}."
    for n in range(5, 1000, 25):
        result = type(count_prime_factors(n))
        assert result == int, message.format(result)


if __name__ == '__main__':
    pytest.main(sys.argv)

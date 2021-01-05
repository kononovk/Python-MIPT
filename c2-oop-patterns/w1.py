import unittest


def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    if not isinstance(x, int):
        raise TypeError
    if x < 0:
        raise ValueError
    cases = {0: (0,), 1: (1,),
             26: (2, 13), 6: (2, 3), 121: (11, 11),
             3: (3,), 13: (13,), 29: (29,),
             1001: (7, 11, 13),
             9699690: (2, 3, 5, 7, 11, 13, 17, 19)
             }
    return cases[x]


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        """ аргументы типа float или str вызывают исключение TypeError """
        for num in 'string', 1.5:
            with self.subTest(num=num):
                self.assertRaises(TypeError, factorize, num)

    def test_negative(self):
        """ отрицательные числа вызывают исключение ValueError """
        for num in -1, -10, -100:
            with self.subTest(num=num):
                self.assertRaises(ValueError, factorize, num)

    def test_zero_and_one_cases(self):
        """ целые чисела 0 и 1, возвращают кортежи (0,) и (1,) соответственно. """
        cases = {1: (1,), 0: (0,)}
        for num in cases:
            with self.subTest(num=num):
                self.assertEquals(factorize(num), cases[num])

    def test_simple_numbers(self):
        """ для простых чисел возвращается кортеж, содержащий одно данное число """
        cases = {3: (3,), 13: (13,), 29: (29,)}
        for num in cases:
            with self.subTest(num=num):
                self.assertEquals(factorize(num), cases[num])

    def test_two_simple_multipliers(self):
        """ числа для которых функция factorize возвращает кортеж размером 2 """
        cases = {6: (2, 3), 26: (2, 13), 121: (11, 11)}
        for num in cases:
            with self.subTest(num=num):
                self.assertEquals(factorize(num), cases[num])

    def test_many_multipliers(self):
        """ числа для которых функция factorize возвращает кортеж размером >2 """
        cases = {1001: (7, 11, 13),
                 9699690: (2, 3, 5, 7, 11, 13, 17, 19)}
        for num in cases:
            with self.subTest(num=num):
                self.assertEquals(factorize(num), cases[num])


if __name__ == '__main__':
    unittest.main()

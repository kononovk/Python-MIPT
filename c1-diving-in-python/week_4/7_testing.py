import unittest


class TestPython(unittest.TestCase):
    def setUp(self):  # запускается перед вызовом каждого метода1
        print("hello")

    def test_float_to_int_coercion(self):
        self.assertEqual(1, int(1.0))

    def test_get_empty_dict(self):
        self.assertIsNone({}.get('key'))

    def test_true(self):
        self.assertTrue(bool(1))

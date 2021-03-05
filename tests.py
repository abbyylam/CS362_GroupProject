import unittest
from task import conv_num
from task import my_datetime
from task import conv_endian


class TestCase_ConvNum(unittest.TestCase):

    def test1(self):
        self.assertTrue(conv_num(str(123)))


class TestCase_MyDateTime(unittest.TestCase):

    def test1(self):
        self.assertTrue(my_datetime(123))


class TestCase_ConvEndian(unittest.TestCase):

    def test1(self):
        self.assertTrue(conv_endian(123))


if __name__ == '__main__':
    unittest.main()

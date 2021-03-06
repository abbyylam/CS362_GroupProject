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

    message = 'Unexpected result!'

    def test1(self):
        expected = '0E 91 A2'
        self.assertEqual(expected, conv_endian(954786, 'big'), self.message)

    def test2(self):
        expected = '0E 91 A2'
        self.assertEqual(expected, conv_endian(954786), self.message)

    def test3(self):
        expected = '-0E 91 A2'
        self.assertEqual(expected, conv_endian(-954786), self.message)

    def test4(self):
        expected = 'A2 91 0E'
        self.assertEqual(expected, conv_endian(954786, 'little'), self.message)

    def test5(self):
        expected = '-A2 91 0E'
        self.assertEqual(expected, conv_endian(-954786, 'little'),
                         self.message)

    def test6(self):
        expected = '-A2 91 0E'
        self.assertEqual(expected, conv_endian(num=-954786, endian='little'),
                         self.message)

    def test7(self):
        expected = None
        self.assertEqual(expected, conv_endian(num=-954786, endian='small'),
                         self.message)

    def test8(self):
        expected = '00'
        self.assertEqual(expected, conv_endian(num=0, endian='big'),
                         self.message)


if __name__ == '__main__':
    unittest.main()

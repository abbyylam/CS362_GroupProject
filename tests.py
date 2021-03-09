import unittest
from task import conv_num
from task import my_datetime
from task import conv_endian


class TestCase_ConvNum(unittest.TestCase):

    message = 'Unexpected result!'

    def test1(self):
        expected = 12345
        self.assertEqual(expected, conv_num('12345'), self.message)

    def test2(self):
        expected = -123.45
        self.assertEqual(expected, conv_num('-123.45'), self.message)

    def test3(self):
        expected = 0.45
        self.assertEqual(expected, conv_num('.45'), self.message)

    def test4(self):
        expected = 123.0
        self.assertEqual(expected, conv_num('123.'), self.message)

    def test5(self):
        expected = 2772
        self.assertEqual(expected, conv_num('0xAD4'), self.message)

    def test6(self):
        expected = None
        self.assertEqual(expected, conv_num('0xAZ4'), self.message)

    def test7(self):
        expected = None
        self.assertEqual(expected, conv_num('12345A'), self.message)

    def test8(self):
        expected = None
        self.assertEqual(expected, conv_num('12.3.45'), self.message)


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

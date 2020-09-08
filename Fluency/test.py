import unittest

from fluentstr import FluentStr

class StringTests(unittest.TestCase):

    def test_string_length(self):

        data = "some random info"
        expect = len(data)
        actual = FluentStr().string_len(data)
        self.assertEqual(actual, expect)


    def test_string_reverse(self):
        data = "akash mitra"
        expect = "artim hsaka"
        actual = FluentStr().string_reverse(data)
        self.assertEqual(actual, expect)





if __name__ == '__main__':
    unittest.main()
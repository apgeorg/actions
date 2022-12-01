import sys
import unittest


class TestHello(unittest.TestCase):

    def setUp(self) -> None:
        sys.path.append("../")

        
    def tearDown(self) -> None:
        pass

    def test_hello(self):
        from lib.hello import hello
        self.assertEqual(hello(), "Hello World")
        
        


if __name__ == '__main__':
    unittest.main()


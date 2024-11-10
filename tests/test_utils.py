import unittest

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        greeting = "Hello, World!"
        self.assertEqual(greeting, "Hello, World!")

if __name__ == "__main__":
    unittest.main()
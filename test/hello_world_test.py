import unittest
import hello_world


class testHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual("Hola Mundo", hello_world.hello_world())

    def test_sayHello(self):
        self.assertEqual("Hello Stuart", hello_world.say_hello("Stuart"))

        # def test_upper(self):
        #     self.assertEqual('foo'.upper(), 'FOO')
        #
        # def test_isupper(self):
        #     self.assertTrue('FOO'.isupper())
        #     self.assertFalse('Foo'.isupper())
        #
        # def test_split(self):
        #     s = 'hello world'
        #     self.assertEqual(s.split(), ['hello', 'world'])
        #    # check that s.split fails when the separator is not a string
        # with self.assertRaises(TypeError):
        #     s.split(2)


if __name__ == '__main__':
    unittest.main()

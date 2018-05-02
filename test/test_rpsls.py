import unittest
from src.rpsls import Rules, InvalidThrow


class RPSLSTest(unittest.TestCase):
    """ Test RPSLS. """

    def test_valid_throw(self):
        rules = Rules()
        self.assertTrue(rules.valid_throw("rock"), "rock ok")
        self.assertTrue(rules.valid_throw("paper"), "paper ok")
        self.assertTrue(rules.valid_throw("scissors"), "scissors ok")
        self.assertTrue(rules.valid_throw("lizard"), "lizard ok")
        self.assertTrue(rules.valid_throw("spock"), "spock ok")
        self.assertFalse(rules.valid_throw("spook"), "spook not ok")

    def test_beats(self):
        rules = Rules()
        self.assertTrue(rules.beats("rock", "scissors"))
        self.assertTrue(rules.beats("rock", "lizard"))
        self.assertFalse(rules.beats("rock", "rock"))
        self.assertFalse(rules.beats("rock", "paper"))
        self.assertFalse(rules.beats("rock", "spock"))
        with self.assertRaises(InvalidThrow) as cm:
            rules.beats("rock", "spook")
        ex = cm.exception
        # self.assertEqual(ex, "InvalidThrow")
        # self.assertIs(ex, InvalidThrow())


if __name__ == '__main__':
    unittest.main()

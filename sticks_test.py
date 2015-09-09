import unittest
from sticks import *

# word_list = ["bird", "calf", "river", "stream", "kneecap",  "cookbook",
#              "language", "sneaker", "algorithm", "integration", "brain"]
ai_player_1 = {4: {'hat': [1, 2, 3], 'beside': [3]}}

class TestGameofSticks(unittest.TestCase):

    # def test_max_stick_choice_more(self):
    #     self.assertEqual(max_stick_choice(8), 3)
    #
    #
    # def test_max_stick_choice_less(self):
    #     self.assertEqual(max_stick_choice(2), 2)


    def test_display_num_sticks(self):
        self.assertEqual(display_num_sticks(6), "There are 6 sticks on the board.")


    def test_new_stick_total(self):
        self.assertEqual(new_stick_total(6, 3), 3)


    def test_is_game_over_true(self):
        self.assertTrue(is_game_over(0))


    def test_is_game_over_false(self):
        self.assertFalse(is_game_over(6))

    def test_ai_wins_test(self):
        self.assertEqual(ai_wins(ai_player_1), {4: {'hat': [1, 2, 3, 3], 'beside': []}})


    # def test_medium_words(self):
    #     self.assertEqual(medium_words(word_list), ["stream", "kneecap", "cookbook", "language", "sneaker"])
    #
    #
    # def test_hard_words(self):
    #     self.assertEqual(hard_words(word_list), ["cookbook", "language", "algorithm", "integration"])
    #
    #
    # def test_random_word(self):
    #     """This test is not very good. Testing things that are random is hard,
    #     in that there's not a predictable choice. The best we can do is make
    #     sure we have valid output."""
    #     word = random_word(word_list)
    #     self.assertTrue(word in word_list)
    #
    #
    # def test_display_word(self):
    #     word = "integration"
    #     self.assertEqual(display_word(word, []), "_ _ _ _ _ _ _ _ _ _ _")
    #     self.assertEqual(display_word(word, ["z"]), "_ _ _ _ _ _ _ _ _ _ _")
    #     self.assertEqual(display_word(word, ["g"]), "_ _ _ _ G _ _ _ _ _ _")
    #     self.assertEqual(display_word(word, ["i"]), "I _ _ _ _ _ _ _ I _ _")
    #     self.assertEqual(display_word(word, ["i", "g"]), "I _ _ _ G _ _ _ I _ _")
    #     self.assertEqual(display_word(word, ["i", "n", "z"]), "I N _ _ _ _ _ _ I _ N")
    #
    #
    # def test_is_word_complete(self):
    #     word = "river"
    #     self.assertFalse(is_word_complete(word, []))
    #     self.assertFalse(is_word_complete(word, ["r"]))
    #     self.assertFalse(is_word_complete(word, ["r", "e"]))
    #     self.assertFalse(is_word_complete(word, ["r", "e", "z"]))
    #     self.assertTrue(is_word_complete(word, ["r", "e", "v", "i"]))

if __name__ == '__main__':
    unittest.main()

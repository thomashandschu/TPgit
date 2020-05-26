import unittest

from esme_lessons.job_interview.anagrams import anagram


class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        # Given
        n='4567'
        expected_output=7654
        # When
        output=anagram(n)
        # Then
        self.assertEqual(expected_output,output)

    def test_anagram_negative(self):
        n=-1
        expected_output=None

        output=anagram(n)

        self.assertEqual(expected_output,output)



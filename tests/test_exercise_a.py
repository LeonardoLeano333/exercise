from unittest import TestCase
from exercise.exercise_a import find_all_duplicates

class ExerciseA(TestCase):

    def test_no_duplicates(self):
        items = [1,2,3,4,4]
        result = find_all_duplicates(items)
        assert result == [4]

    def test_one_duplication(self):
        items = [1,2,2,3,4,4]
        result = find_all_duplicates(items)
        assert result == [2,4]

    def test_three_of_the_same(self):
        items = [1,2,2,3,4,4,4]
        result = find_all_duplicates(items)
        assert result == [2,4]
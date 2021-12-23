import asyncio
from io import StringIO
import sys

from unittest import TestCase
from exercise.exercise_b import async_print

class ExerciseB(TestCase):

    def setUp(self) -> None:
        self.capturedOutput = StringIO()
        sys.stdout = self.capturedOutput

    def tearDown(self) -> None:
        sys.stdout = sys.__stdout__

    def test_two_items(self):
        items = [1,2]
        asyncio.run(async_print(items))
        response = self.capturedOutput.getvalue()
        assert response == '1\n2\n'

    def test_one_item(self):
        items = [1]
        asyncio.run(async_print(items))
        response = self.capturedOutput.getvalue()
        assert response == '1\n'


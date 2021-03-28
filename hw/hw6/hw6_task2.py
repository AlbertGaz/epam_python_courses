"""Homework 6.2."""
from __future__ import annotations

import datetime
from collections import defaultdict
from typing import NoReturn, Optional, Union


class DeadlineError(Exception):
    """Missed deadline."""


class Human:
    """Give names."""

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name


class Homework:
    """Class Homework."""

    def __init__(self, text: str, days_to_deadline: int) -> None:
        self.text = text
        self.deadline = datetime.timedelta(days=days_to_deadline)
        self.created = datetime.datetime.now()

    def is_active(self) -> bool:
        """Check if hw is in progress or late.

        Returns: bool

        """
        return int(self.deadline.total_seconds()) > 0


class Student(Human):
    """Class Student."""

    def do_homework(
        self, hw: Homework, solution: str
    ) -> Union[Optional[HomeworkResult], NoReturn]:
        """Check if hw is in progress - True, else print You are Late.

        Args:
            hw: Homework object
            solution: str

        Returns: hw object or None

        """
        if Homework.is_active(hw):
            return HomeworkResult(self, hw, solution)
        raise DeadlineError("You are late!")


class Teacher(Human):
    """Class Teacher."""

    homework_done = defaultdict(set)

    def create_homework(self, text: str, days_to_deadline: int) -> Homework:
        """Create homework object.

        Args:
            text: str
            days_to_deadline: int

        Returns: homework object

        """
        return Homework(text, days_to_deadline)

    def check_homework(self, hw_res: HomeworkResult) -> None:
        """Check homework and if ok write it to homework done."""
        if len(hw_res.solution) > 5:
            Teacher.homework_done[hw_res.hw].add(hw_res.solution)

    @classmethod
    def reset_results(cls: __class__, hw_res: HomeworkResult = None) -> None:
        """Reset the homework done results."""
        if hw_res:
            del Teacher.homework_done[hw_res]
        else:
            Teacher.homework_done.clear()


class HomeworkResult:
    """Homework results."""

    def __init__(self, student: Student, homework: Homework, solution: str) -> None:
        self.student = student
        if not isinstance(homework, Homework):
            raise TypeError("You gave a not Homework object")
        self.hw = homework
        self.solution = solution
        self.created = datetime.datetime.now()

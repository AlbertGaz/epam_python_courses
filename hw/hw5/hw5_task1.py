"""Homework 5.1.

Create three classes and connections between them.
"""
from __future__ import annotations

import datetime
import sys


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
        if (
            int(self.deadline.total_seconds()) > 0
        ):  # checks if total seconds in time to deadline is > 0
            return True
        return False


class Student:
    """Class Student."""

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, hw: Homework) -> (Homework, None):
        """Check if hw is in progress - True, else print You are Late.

        Args:
            hw: Homework object

        Returns: hw object or None

        """
        if Homework.is_active(hw):
            return hw
        else:
            sys.stdout.write("You are late!")
            return None


class Teacher:
    """Class Teacher."""

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def create_homework(self, text: str, days_to_deadline: int) -> Homework:
        """Create homework object.

        Args:
            text: str
            days_to_deadline: int

        Returns: homework object

        """
        return Homework(text, days_to_deadline)

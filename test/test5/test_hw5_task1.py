"""TEST Homework 5.1."""
import datetime

import pytest

from hw.hw5.hw5_task1 import Student, Teacher

teacher = Teacher("Aleksei", "Samarin")
hw1 = teacher.create_homework("OOP", 5)
hw2 = teacher.create_homework("Tests", 0)
student = Student("Albert", "Gazaryan")


@pytest.mark.parametrize(
    ("atr", "expected"),
    [
        (teacher.last_name, "Samarin"),
        (student.first_name, "Albert"),
        (hw1.deadline, datetime.timedelta(days=5)),
        (hw2.deadline, datetime.timedelta(days=0)),
        (hw1.text, "OOP"),
        (hw2.text, "Tests"),
        (student.do_homework(hw1), hw1),
        (student.do_homework(hw2), None),
    ],
)
def test_name_deadline_hw(atr, expected):
    assert atr == expected


def test_catch_stdout(capsys):
    student.do_homework(hw2)
    stdout, _ = capsys.readouterr()
    assert stdout == "You are late!"

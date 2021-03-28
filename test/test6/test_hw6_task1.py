"""TEST Homework 6.1."""
from hw.hw6.hw6_task1 import instances_counter


@instances_counter
class User:
    pass


def test_class_1():
    actual_result1 = User.get_created_instances()
    assert actual_result1 == 0


def test_class_2():
    user, _, _ = User(), User(), User()
    actual_result2 = user.get_created_instances()
    assert actual_result2 == 3


def test_class_3():
    user, _, _ = User(), User(), User()
    actual_result3 = user.reset_instances_counter()
    assert actual_result3 == 6


def test_class_4():
    user, _, _ = User(), User(), User()
    actual_result2 = user.get_created_instances()
    assert actual_result2 == 3

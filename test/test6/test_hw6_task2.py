"""TEST Homework 6.2."""
import pytest

from hw.hw6.hw6_task2 import HomeworkResult, Student, Teacher

oop_teacher = Teacher("Daniil", "Shadrin")
advanced_python_teacher = Teacher("Aleksandr", "Smetanin")

lazy_student = Student("Roman", "Petrov")
good_student = Student("Lev", "Sokolov")

oop_hw = oop_teacher.create_homework("Learn OOP", 1)
docs_hw = oop_teacher.create_homework("Read docs", 5)

result_1 = good_student.do_homework(oop_hw, "I have done this hw")
result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
result_3 = lazy_student.do_homework(docs_hw, "done")


@pytest.mark.parametrize(
    ("atr", "expected_result"),
    [
        (lazy_student.first_name, "Roman"),
        (lazy_student.last_name, "Petrov"),
        (good_student.first_name, "Lev"),
        (good_student.last_name, "Sokolov"),
    ],
)
def test_name(atr, expected_result):
    actual_result = atr
    assert actual_result == expected_result


def test_type_error():
    with pytest.raises(TypeError, match="You gave a not Homework object"):
        HomeworkResult(good_student, "fff", "Solution")


oop_teacher.check_homework(result_1)
temp_1 = oop_teacher.homework_done
advanced_python_teacher.check_homework(result_1)
temp_2 = Teacher.homework_done


def test_homework_done():
    assert temp_1 == temp_2


Teacher.reset_results()


def test_homework_done_after_reset():
    assert len(Teacher.homework_done[oop_hw]) == 0

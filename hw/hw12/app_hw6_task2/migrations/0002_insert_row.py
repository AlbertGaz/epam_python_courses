from django.db import migrations, models
from datetime import datetime, timedelta


def insert_row(apps, schema_editor):
    """Insert row to tables in DB."""
    Student = apps.get_model("app_hw6_task2", "Student")
    st = Student(first_name="Djan", last_name="Go")
    st.save()

    Teacher = apps.get_model("app_hw6_task2", "Teacher")
    tch = Teacher(first_name="Doctor", last_name="Schulze")
    tch.save()

    Homework = apps.get_model("app_hw6_task2", "Homework")
    hw = Homework(
        hw_text="Save Django",
        teacher=tch,
        created=datetime.now(),
        deadline=timedelta(weeks=1),
    )
    hw.save()

    HomeworkResult = apps.get_model("app_hw6_task2", "HomeworkResult")
    hw_res = HomeworkResult(
        student=st, hw=hw, created=datetime.now(), solution="Django Unchained"
    )
    hw_res.save()


class Migration(migrations.Migration):

    dependencies = [
        ("app_hw6_task2", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(insert_row),
    ]

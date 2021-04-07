"""Homework 8.2."""
import sqlite3
from typing import Union


class TableData:
    """Class description."""

    def __init__(self, database_name: str, table_name: str) -> None:
        self.database_name = database_name
        self.table_name = table_name
        self.curr = None

    def __len__(self) -> int:
        """Give current amount of rows in table in database."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
        cursor.execute(f"SELECT count(*) from {self.table_name}")
        return cursor.fetchone()[0]

    def __contains__(self, item: str) -> bool:
        """Check if item with same name exists in table."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
        cmnd = f"SELECT * from {self.table_name} where name = ?"
        return bool(cursor.execute(cmnd, (item,)).fetchone())

    def __getitem__(self, item: str) -> Union[str, tuple]:
        """Return single data row for table row with name item."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
        if item == "name":
            return self.curr[0]
        cmnd = f"SELECT * from {self.table_name} where name = ?"
        cursor.execute(cmnd, (item,))
        if row := cursor.fetchone():
            return row
        raise KeyError(f"Key {item} not found")

    def __iter__(self) -> "TableData":
        """Return the iterator."""
        return self

    def __next__(self) -> "TableData":
        """Return next element of iterator."""
        with sqlite3.connect(self.database_name) as conn:
            cursor = conn.cursor()
        if not self.curr:
            cursor.execute(f"SELECT * from {self.table_name} order by name asc limit 1")
            self.curr = cursor.fetchone()
            return self
        cmnd = f"SELECT * from {self.table_name} where name > ? order by name limit 1"
        cursor.execute(cmnd, (self.curr[0],))
        self.curr = cursor.fetchone()
        if not self.curr:
            raise StopIteration
        return self

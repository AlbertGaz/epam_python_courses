"""TEST Homework 11.2."""

from hw.hw11.hw11_task2 import Order


def good_discount_programm(order):
    _discount = 0.5
    return order.price * _discount


def test_discount():
    order = Order(100, good_discount_programm)
    assert order.final_price() == 50


def not_real_discount_programm(order):
    _discount = 1.1
    return order.price * _discount


def test_not_real_discount():
    order = Order(100, not_real_discount_programm)
    assert order.final_price() == 100

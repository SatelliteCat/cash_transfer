"""Тест модели Accounts"""

import pytest

from cash_transfer_app.models import Accounts


def test_lock_rows():
    """
    Тест блокировки строк во время совершения операции
    """
    pass


@pytest.mark.django_db
def test_wrong_args():
    """
    Тест поведения функции transfer при неправильных аргументах
    """

    # User 1
    account1 = Accounts()
    account1.user_id = 6
    account1.balance = 100
    account1.email = 'llkj@gmail.com'
    account1.currency = 'gbr'
    account1.save()

    # User 2
    account2 = Accounts()
    account2.user_id = 5
    account2.balance = 1000
    account2.email = 'poiu@gmail.com'
    account2.currency = 'gbr'
    account2.save()

    # Transfer from User 2 to User 1
    answer = account2.transfer('llkj1@gmail.com', 100)

    assert answer != ''  # Возвращение ошибки, а не успешного выполнения


@pytest.mark.django_db
def test_min_balance():
    """
    Тест поведения функции transfer при недостатке денег на балансе пользователя
    """

    # User 1
    account1 = Accounts()
    account1.user_id = 6
    account1.balance = 100
    account1.email = 'llkj@gmail.com'
    account1.currency = 'gbr'
    account1.save()

    # User 2
    account2 = Accounts()
    account2.user_id = 5
    account2.balance = 1000
    account2.email = 'poiu@gmail.com'
    account2.currency = 'gbr'
    account2.save()

    # Transfer from User 1 to User 2
    answer = account1.transfer('poiu@gmail.com', 1000)

    assert answer != ''


@pytest.mark.django_db
def test_max_balance():
    """
    Тест поведения функции transfer при максимальном балансе
    """

    # User 1
    account1 = Accounts()
    account1.user_id = 6
    account1.balance = 10e10
    account1.email = 'llkj@gmail.com'
    account1.currency = 'gbr'
    account1.save()

    # User 2
    account2 = Accounts()
    account2.user_id = 5
    account2.balance = 10e45
    account2.email = 'poiu@gmail.com'
    account2.currency = 'gbr'
    account2.save()

    # Transfer from User 1 to User 2
    answer = account1.transfer('poiu@gmail.com', 10e9)

    assert answer != ''


@pytest.mark.django_db
def test_transfer_success():
    """
    Тест успешного перевода между пользователями
    """

    # User 1
    account1 = Accounts()
    account1.user_id = 6
    account1.balance = 1000
    account1.email = 'llkj@gmail.com'
    account1.currency = 'gbr'
    account1.save()

    # User 2
    account2 = Accounts()
    account2.user_id = 5
    account2.balance = 100
    account2.email = 'poiu@gmail.com'
    account2.currency = 'gbr'
    account2.save()

    # Transfer from User 1 to User 2
    answer = account1.transfer('poiu@gmail.com', 100)

    assert answer == ''


@pytest.mark.django_db
def test_currency():
    """
    Тест поведения функции transfer в случае,
    когда у пользователя не найден данный вид валюты
    """

    # User 1
    account1 = Accounts()
    account1.user_id = 6
    account1.balance = 1000
    account1.email = 'llkj@gmail.com'
    account1.currency = 'gbr'
    account1.save()

    # User 2
    account2 = Accounts()
    account2.user_id = 5
    account2.balance = 100
    account2.email = 'poiu@gmail.com'
    account2.currency = 'rur'
    account2.save()

    # Transfer from User 1 to User 2
    answer = account1.transfer('poiu@gmail.com', 100)

    assert answer != ''

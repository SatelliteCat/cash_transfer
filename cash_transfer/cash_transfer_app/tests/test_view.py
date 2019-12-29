"""Тест view.py"""

import pytest
from django.http import HttpRequest

from cash_transfer_app.models import Accounts
from cash_transfer_app.views import transfer_api


@pytest.mark.django_db
def test_args():
    """
    Тест при недостатке аргументов
    """

    # User 1
    account1 = Accounts()
    account1.user_id = 6
    account1.balance = 1000
    account1.email = 'llkj@gmail.com'
    account1.currency = 'rur'
    account1.save()

    # User 2
    account2 = Accounts()
    account2.user_id = 5
    account2.balance = 100
    account2.email = 'poiu@gmail.com'
    account2.currency = 'rur'
    account2.save()

    request = HttpRequest()
    request.POST['email'] = 'poiu@gmail.com'
    request.POST['amount'] = '100'
    # request.POST['currency'] = 'rur'
    request.POST['user_id'] = 6

    answer = transfer_api(request)

    assert answer.status_code == 400


@pytest.mark.django_db
def test_transfer_success():
    """
    Тест вывода статуса успешного перевода
    """

    # User 1
    account1 = Accounts()
    account1.user_id = 6
    account1.balance = 1000
    account1.email = 'llkj@gmail.com'
    account1.currency = 'rur'
    account1.save()

    # User 2
    account2 = Accounts()
    account2.user_id = 5
    account2.balance = 100
    account2.email = 'poiu@gmail.com'
    account2.currency = 'rur'
    account2.save()

    request = HttpRequest()
    request.POST['email'] = 'poiu@gmail.com'
    request.POST['amount'] = '100'
    request.POST['currency'] = 'rur'
    request.POST['user_id'] = 6

    answer = transfer_api(request)

    assert answer.status_code == 200


@pytest.mark.django_db
def test_transfer_bad():
    """
    Тест вывода ошибки
    (статус ошибки успешно передаётся из модели в view)
    """

    # User 1
    account1 = Accounts()
    account1.user_id = 6
    account1.balance = 1000
    account1.email = 'llkj@gmail.com'
    account1.currency = 'rur'
    account1.save()

    # User 2
    account2 = Accounts()
    account2.user_id = 5
    account2.balance = 100
    account2.email = 'poiu@gmail.com'
    account2.currency = 'rur'
    account2.save()

    request = HttpRequest()
    request.POST['email'] = 'poiu@gmail.com'
    request.POST['amount'] = '20000'
    request.POST['currency'] = 'rur'
    request.POST['user_id'] = 6

    answer = transfer_api(request)
    expected_answer = b'{"BalanceError": "Insufficient funds on the balance sheet"}'

    assert answer.content == expected_answer

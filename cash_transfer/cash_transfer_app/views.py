import traceback
from decimal import *

from django.http import JsonResponse
from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt

from cash_transfer_app.models import Accounts


# @csrf_exempt
def transfer_api(request):
    response = JsonResponse({})

    try:
        accounts = Accounts()
        accounts.user_id = request.POST['user_id']
        accounts.currency = request.POST['currency']
        transfer_code = accounts.transfer(
            request.POST['email'], Decimal(request.POST['amount'])
        )
    except Exception:
        formatted_lines = traceback.format_exc().splitlines()
        transfer_code = formatted_lines[-1]

    if(transfer_code):
        split_lines = transfer_code.split(': ')
        response = JsonResponse({split_lines[0]: split_lines[1]})
        response.status_code = 400
    else:
        response.status_code = 200

    return response

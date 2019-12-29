import traceback, sys

from django.db import models, transaction


class Accounts(models.Model):
    """
    Балансы пользователей
    """

    # Fields
    user_id = models.IntegerField()
    email = models.EmailField(max_length=254)
    balance = models.DecimalField(decimal_places=5, max_digits=55)
    currency = models.CharField(max_length=50)

    # Methods
    def __str__(self):
        return self.email

    def transfer(self, to_email, amount):
        """
        Перевод денег от текущего пользователя другому, найденному по email
        """

        transfer_code = ''

        try:
            from_user = Accounts.objects.select_for_update().filter(
                user_id=self.user_id, currency=self.currency
            )

            to_user = Accounts.objects.select_for_update().filter(
                email=to_email, currency=self.currency
            )

            with transaction.atomic():
                from_balance = from_user.values('balance').first()['balance']
                to_balance = to_user.values('balance').first()['balance']

                if(from_balance >= amount):
                    from_user.update(balance=from_balance - amount)
                    to_user.update(balance=to_balance + amount)
                else:
                    transfer_code = 'BalanceError: Insufficient funds on the balance sheet'

        except Exception:
            formatted_lines = traceback.format_exc().splitlines()
            transfer_code = formatted_lines[-1]

        return transfer_code

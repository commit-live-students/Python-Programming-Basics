from unittest import TestCase

from account import Savings, Current


class TestAccount(TestCase):
    def test_deposit_savings(self):
        sa = Savings("123")
        sa.deposit(1500)
        self.assertEqual(1500, sa.balance)

    def test_widraw_savings(self):
        sa = Savings("123")
        sa.deposit(1500)
        sa.withdraw(300)
        self.assertEqual(1200, sa.balance)


    def test_deposit_current(self):
        ca = Current("456")
        ca.deposit(20000)
        self.assertEqual(20000, ca.balance)

    def test_widraw_current(self):
        ca = Current("456")
        ca.deposit(20000)
        ca.withdraw(1)
        self.assertEqual(19998.9, ca.balance)

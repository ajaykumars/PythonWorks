from enum import Enum

class Account():

    def __init__(self, acc_holder_name=None, acc_type=None):
       self._acc_holder_name = acc_holder_name
       self._acc_type = acc_type

    def get_acc_holder_name(self):
        return self._acc_holder_name

    def get_acc_type(self):
        return self._acc_type


    def print_details(self):
        if self.get_acc_holder_name() is not None and self.get_acc_type() is not None:
            print("User : {} has a {} Account.".format(self._acc_holder_name, self._acc_type))
        else:
            try:
                print("Raising Error")
                raise ValueError("value error")
            except:
                print("No details available")

class AccountType(Enum):
    savings = "SB"
    current = "CB"


account_1 = Account()
account_1.print_details()

account_2 = Account("Rammy", AccountType.current.value)
account_2.print_details()

from typing import List


class Employee():
    raise_amt = 1.04

    def __init__(self, _first_name, _last_name, _email, _salary=1000):
        self.first_name = _first_name
        self.last_name = _last_name
        self.email = _email
        self.pay = _salary

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def fullname(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_class(cls):
        return cls()


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, _first_name, _last_name, _email, _salary=1000, _prog_lang='Basic'):
        self.prog_lang = _prog_lang
        super().__init__(_first_name, _last_name, _email, _salary)


class Manager(Employee):

    def __init__(self, _first_name, _last_name, _email, _salary=1000, _employees: List[Employee] = None):
        if (_employees is None):
            self.employees = []
        else:
            self.employees = _employees

        super().__init__(_first_name, _last_name, _email, _salary)

    def add_employee(self, _employee):
        if (_employee not in self.employees):
            self.employees.append(_employee);


    def remove_employee(self, _employee):
        if (_employee in self.employees):
            self.employees.remove(_employee)

    def get_all_employee(self):
        return self.employees

# emp1 = Employee('Test', 'User', 'test_user@company.com', 5000)
# emp1.var = 'Instance Variable'
#
# print(emp1.fullname())
# print(Employee.fullname(Employee('Test2', 'User', 'test2_user@company.com')))
#
# print(emp1.__dict__)
# print(Employee.__dict__)
#
# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

emp1 = Employee('TestEmp', 'User', 'test_user@company.com', 5000)
dev1 = Developer('TestDev', 'User', 'testdev_user@company.com', 6000, 'Python')
mgr1 = Manager('TestMgr', 'User', 'testmgr_user@company.com', 8000, [emp1])

mgr1.add_employee(dev1)

print([employee.fullname() for employee in mgr1.get_all_employee()])

mgr1.remove_employee(dev1)

print([employee.fullname() for employee in mgr1.get_all_employee()])









from pprint import pprint


class Flight:
    def __init__(self, number=None, aircraft=None):
        #Check for type String
        self._aircraft = aircraft
        if not (type(number) is str):
            raise TypeError("Flight number must be a string")

        #Check first 2 characters in flight number is only alphabets
        if not (number[0:2].isalpha() and type(number) == str):
            raise ValueError("No airline code in " + number)

        if not number[0:2].isupper():
            raise ValueError("Invalid airline '{}'".format(number))

        if not number[2:].isdigit():
            raise ValueError("Invalid route number for '{}'".format(number))

        self.number = number

        rows, seats = self._aircraft.get_seat_plan()
        self._seating = [None] + [{letter:None for letter in seats} for _ in rows]

    def __str__(self):
        return self.number

    def flight_model(self):
        return self._aircraft.get_model()

    def seating(self):
        return self._seating

    def allocate_seat(self, seat, passenger):
        seat_row, seat_col = [ch for ch in seat]
        self._seating[int(seat_row)][seat_col] = passenger

class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_in_row):
        self.registration = registration
        self.model = model
        self.num_rows = num_rows
        self.num_seats_in_row = num_seats_in_row

    def get_registration(self):
        return self.registration

    def get_model(self):
        return self.model

    def get_seat_plan(self):
        return (range(1, self.num_rows+1), "ABCDEFGH"[:self.num_seats_in_row])



f1 = Flight('IA237', Aircraft('IN2234', 'AB320', num_rows=23, num_seats_in_row=5 ))
print(f1.number)
print(f1)
print(f1.flight_model())

f1.allocate_seat('4A', 'Austin Martin')

pprint(f1.seating())




# try:
#     f2 = Flight(12)
#     print(f2.number)
# except (ValueError,TypeError) as error:
#     print(error)
# finally:
#     print("end")
#
#
# a1 = Aircraft('IN2234', 'AB320', num_rows=23, num_seats_in_row=5 )
# print(a1.get_model())
# print(a1.get_registration())
# print(a1.get_seat_plan())



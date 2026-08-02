class Bus:
    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        self.booked = []

    def book_seat(self, seat_number, passenger_name):
        for seat in self.booked:
            if seat[0] == seat_number:
                print(f"Seat already booked")
                return
        self.booked.append((seat_number, passenger_name))
        print(f"Seat {seat_number} booked for {passenger_name}")

    def available_seats(self):
        return self.total_seats - len(self.booked)

    def passenger_list(self):
        print(f"---- Passenger List ({self.route}) ----")
        for seat_number, passenger_name in self.booked:
            print(f"Seat {seat_number}: {passenger_name}")


bus = Bus("Kathmandu - Pokhara", 10)

bookings = [
    (3, "Ramila Shrestha"),
    (7, "Deepak Gurung"),
    (3, "Anita Rai"),
    (1, "Prakash Magar"),
    (7, "Suman Tamang"),
]

for seat_number, passenger_name in bookings:
    bus.book_seat(seat_number, passenger_name)

print(f"Available seats: {bus.available_seats()}")
bus.passenger_list()
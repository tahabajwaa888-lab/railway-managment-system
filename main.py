class Train:
    def __init__(self, train_name, from_location, to_location, time, train_type, fare):
        self.train_name = train_name
        self.from_location = from_location
        self.to_location = to_location
        self.time = time
        self.train_type = train_type
        self.fare = fare

class Ticket:
    def __init__(self, ticket_id, ticket_name, from_location, to_location, ticket_type, fare):
        self.ticket_id = ticket_id
        self.ticket_name = ticket_name
        self.from_location = from_location
        self.to_location = to_location
        self.ticket_type = ticket_type
        self.fare = fare

class Passenger:
    def __init__(self, name, phone_no):
        self.name = name
        self.phone_no = phone_no
        self.ticket = []

    def available_trains(self, train_list):
        if not train_list:
            print("No trains available.")
            return
        for train in train_list:
            print("Train Name:", train.train_name)
            print("Route:", train.from_location, "to", train.to_location)
            print("Type:", train.train_type)
            print("Fare:", train.fare)
            print("-" * 30)

    def book_ticket(self, train_list):
        train_name = input("Enter train name: ")
        for train in train_list:
            if train.train_name == train_name:
                ticket_id = len(self.ticket) + 1
                new_ticket = Ticket(
                    ticket_id,
                    train.train_name,
                    train.from_location,
                    train.to_location,
                    train.train_type,
                    train.fare
                )
                self.ticket.append(new_ticket)
                print("Ticket booked successfully!")
                print("Ticket ID:", ticket_id)
                return
        print("Train not found.")

    def check_ticket(self):  
        ticket_id = int(input("Enter ticket ID: "))
        for t in self.ticket:
            if t.ticket_id == ticket_id:
                print("Ticket ID:", t.ticket_id)
                print("Train Name:", t.ticket_name)
                print("From:", t.from_location)
                print("To:", t.to_location)
                print("Ticket Type:", t.ticket_type)
                print("Fare:", t.fare)
                return
        print("Ticket not found.")

    def cancel_ticket(self):
        ticket_id = int(input("Enter ticket ID to cancel: "))
        for t in self.ticket:
            if t.ticket_id == ticket_id:
                self.ticket.remove(t)
                print("Ticket cancelled successfully.")
                return
        print("Ticket not found.")


train_list = []
all_passengers = []


class Admin:
    def __init__(self, name, email, phone_no):
        self.name = name
        self.email = email
        self.phone_no = phone_no

    def show_trains(self):
        if not train_list:
            print("No trains available.")
            return
        for train in train_list:
            print("Train Name:", train.train_name)
            print("Time:", train.time)
            print("From:", train.from_location)
            print("To:", train.to_location)
            print("Type:", train.train_type)
            print("Fare:", train.fare)
            print("-" * 30)

    def add_train(self):
        train_name = input("Enter train name: ")
        from_location = input("Enter departure city: ")
        to_location = input("Enter arrival city: ")
        time = input("Enter time: ")
        train_type = input("Enter train type (Business/Economic): ")
        fare = float(input("Enter fare: "))
        train_list.append(Train(train_name, from_location, to_location, time, train_type, fare))
        print("Train added successfully.")

    def cancel_train(self):
        train_name = input("Enter train name to cancel: ")
        for train in train_list:
            if train.train_name == train_name:
                train_list.remove(train)
                print("Train cancelled successfully.")
                return
        print("Train not found.")

    def update_train(self):
        train_name = input("Enter train name to update: ")
        for train in train_list:
            if train.train_name == train_name:
                print("1. Train Name \n2. From Location\n3. To Location\n4. Time\n5. Train Type\n6. Fare")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    train.train_name = input("Enter new train name: ")
                elif choice == 2:
                    train.from_location = input("Enter new departure location: ")
                elif choice == 3:
                    train.to_location = input("Enter new arrival location: ")
                elif choice == 4:
                    train.time = input("Enter new time: ")
                elif choice == 5:
                    train.train_type = input("Enter new train type: ")
                elif choice == 6:
                    train.fare = float(input("Enter new fare: "))
                else:
                    print("Invalid choice.")
                    return
                print("Train updated successfully.")
                return
        print("Train not found.")

    def total_income(self):
        total = 0
        for passenger in all_passengers:
            for t in passenger.ticket:
                total += t.fare
        return total



passenger_data = []
try:
    with open("passenger.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if len(data) >= 2:
                passenger_data.append((data[0], data[1]))  
except FileNotFoundError:
    print("Warning: passenger.txt not found. No passengers loaded.")

admin_data = []
try:
    with open("admin.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")
            if len(data) >= 3:
                admin_data.append((data[0], data[1], data[2]))  # name, phone, email
except FileNotFoundError:
    print("Warning: admin.txt not found. No admins loaded.")



while True:
    print("\nLOGIN PAGE")
    print("a. As Passenger")
    print("b. As Admin")
    print("c. Exit")

    choice = input("Enter a, b, or c: ").strip().lower()

    if choice == "a":
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        found = False
        for p in passenger_data:
            if name == p[0] and phone == p[1]:
                found = True
                passenger1 = Passenger(name, phone)
                all_passengers.append(passenger1)

                while True:
                    print("\nPASSENGER MENU")
                    print("1. Check available trains")
                    print("2. Book ticket")
                    print("3. Check your ticket")
                    print("4. Cancel your ticket")
                    print("5. Exit")

                    ch = input("Enter choice: ")
                    if ch == "1":
                        passenger1.available_trains(train_list)
                    elif ch == "2":
                        passenger1.book_ticket(train_list)
                    elif ch == "3":
                        passenger1.check_ticket()
                    elif ch == "4":
                        passenger1.cancel_ticket()
                    elif ch == "5":
                        break
                    else:
                        print("Invalid choice.")
                break

        if not found:
            print("Passenger not found.")

    elif choice == "b":
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        email = input("Enter your email: ")

        found = False
        for a in admin_data:
            if name == a[0] and phone == a[1] and email == a[2]:
                found = True
                admin1 = Admin(name, email, phone)

                while True:
                    print("\nADMIN MENU")
                    print("1. View all trains")
                    print("2. Add train")
                    print("3. Cancel train")
                    print("4. Update train")
                    print("5. Total income")
                    print("6. Exit")

                    ch = input("Enter choice: ")
                    if ch == "1":
                        admin1.show_trains()
                    elif ch == "2":
                        admin1.add_train()
                    elif ch == "3":
                        admin1.cancel_train()
                    elif ch == "4":
                        admin1.update_train()
                    elif ch == "5":
                        print("Total Income:", admin1.total_income())
                    elif ch == "6":
                        break
                    else:
                        print("Invalid choice.")
                break

        if not found:
            print("Admin not found.")

    elif choice == "c":
        print("Goodbye!")
        break

    else:
        print("Invalid entry. Please enter a, b, or c.")

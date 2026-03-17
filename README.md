class Train:
    def __init__(self, train_name, from_location, to_location, time, train_type, fare):
        self.train_name = train_name
        self.from_location = from_location
        self.to_location = to_location
        self.time = time
        self.train_type = train_type
        self.fare = fare

class ticket:
    def __init__(self,ticket_id,ticket_name,from_location,to_location,ticket_type,fare):
        self.ticket_id=ticket_id
        self.ticket_name=ticket_name
        self.from_location=from_location
        self.to_location=to_location
        self.ticket_type=ticket_type
        self.fare=fare
class passenger:
    def __init__(self,name,phone_no):
        self.name=name
        self.phone_no=phone_no
        self.ticket=[]

    def available_trains(self,train_list):
        for train in train_list:
            print(train.train_name)
            print(train.from_location,"to",train.to_location)
            print(train.train_type)
            print(train.fare)
    def book_ticket(self,train_list):
        train_name=input("train name ")
        for train in train_list:
            if train.train_name==train_name:

              ticket_id = len(self.ticket) + 1

              new_ticket = ticket(
                ticket_id,
                train.train_name,
                train.from_location,
                train.to_location,
                train.train_type,
                train.fare
            )

              self.ticket.append(new_ticket)

              print("Ticket booked successfully")
              return

        print("Train not found")


    def cheak_ticket(self):
        ticket_id=int(input("ticket id "))
        for ticket in self.ticket:
            if ticket.ticket_id==ticket_id:
              print("Ticket ID:", ticket.ticket_id)
              print("Train Name:", ticket.ticket_name)
              print("From:", ticket.from_location)
              print("To:", ticket.to_location)
              print("Ticket Type:", ticket.ticket_type)
              print("Fare:", ticket.fare)

              return

        print("Ticket not found")

    def cancel_ticket(self):
      ticket_id = int(input("Enter ticket ID to cancel: "))
      for ticket in self.ticket:
          if ticket.ticket_id == ticket_id:
             self.ticket.remove(ticket)
             print("Ticket cancelled successfully")
             return

      print("Ticket not found") 

train_list=[] # in thses 2 global list when you make the relitive object must append them in these list 
all_passengers=[]

class admin:
   def __init__(self,name,email,phone_no):
      self.name=name
      self.email=email
      self.phone_no=phone_no
      self.train_list=[]


   def show_trains(self):
    for train in train_list:
        print("Train name:", train.train_name)
        print("Train time:", train.time)
        print("From:", train.from_location)
        print("To:", train.to_location)
        print("Type:", train.train_type)
        print("Fare:", train.fare)

   def add_train(self,train_list):
     train_name = input("Enter train name: ")
     from_location = input("Enter departure city: ")
     to_location = input("Enter arrival city: ")
     time = input("Enter time: ")
     train_type = input("Enter train type (Business/Economic): ")
     fare = float(input("Enter fare: "))

     train_new = Train(train_name, from_location, to_location, time, train_type, fare)

     train_list.append(train_new)

     print("Train added successfully")

   def cancel_train(self, train_list):

     train_name = input("Enter train name: ")

     for train in train_list:

        if train.train_name == train_name:
            train_list.remove(train)
            print("Train cancelled successfully")
            return

     print("Train not found")  
   
   def update_train(self, train_list):

     train_name = input("Enter train name to update: ")

     for train in train_list:

        if train.train_name == train_name:

            print("What do you want to update?")
            print("1. Train Name")
            print("2. From Location")
            print("3. To Location")
            print("4. Time")
            print("5. Train Type")
            print("6. Fare")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                new_name = input("Enter new train name: ")
                train.train_name = new_name

            elif choice == 2:
                new_from = input("Enter new departure location: ")
                train.from_location = new_from

            elif choice == 3:
                new_to = input("Enter new arrival location: ")
                train.to_location = new_to

            elif choice == 4:
                new_time = input("Enter new time: ")
                train.time = new_time

            elif choice == 5:
                new_type = input("Enter new train type: ")
                train.train_type = new_type

            elif choice == 6:
                new_fare = float(input("Enter new fare: "))
                train.fare = new_fare

            else:
                print("Invalid choice")

            print("Train updated successfully")
            return

     print("Train not found")

   def total_income(self):
    total = 0
    for passenger in all_passengers: 
        for ticket in passenger.ticket:
            total += ticket.fare  
    return total

passenger_data=[]

with open("passengers.txt","r") as f:
    for line in f:
        data=line.strip().split(",")
        name=data[0]
        phone=int(data[1])
        passenger_data.append((name,phone))


admin_data=[]

with open("admins.txt","r") as f:
    for line in f:
        data=line.strip().split(",")
        name=data[0]
        phone=int(data[1])
        email=data[2]
        admin_data.append((name,phone,email))

while True:
  print("LOGIN PAGE")
  print("a. As Passenger")
  print("b. As Admin")

  choice = input("Enter a or b: ")

  if choice == "a":

    name = input("Enter your name: ")
    phone = int(input("Enter your phone number: "))
    for p in passenger_data:

     if name == p[0] and phone == p[1]:

        passenger1 = passenger(name, phone)
        all_passengers.append(passenger1)

        while True:

            print("PASSENGER MENU")
            print("1. Check available trains")
            print("2. Book ticket")
            print("3. Check your ticket")
            print("4. Cancel your ticket")
            print("5. Exit")

            ch = int(input("Enter choice: "))

            if ch == 1:
                passenger1.available_trains(train_list)

            elif ch == 2:
                passenger1.book_ticket(train_list)

            elif ch == 3:
                passenger1.cheak_ticket()

            elif ch == 4:
                passenger1.cancel_ticket()

            elif ch == 5:
                break

            else:
                print("Invalid choice")

    else:
        print("Passenger not found")


  elif choice == "b":

    name = input("Enter your name: ")
    phone = int(input("Enter your phone number: "))
    email = input("Enter your email: ")
    for a in admin_data:

     if name == a[0] and phone == a[1] and email == a[2]:

        admin1 = admin(name, email, phone)

        while True:

            print("ADMIN MENU")
            print("1. View all trains")
            print("2. Add train")
            print("3. Cancel train")
            print("4. Update train")
            print("5. Total income")
            print("6. Exit")

            ch = int(input("Enter choice: "))

            if ch == 1:
                admin1.show_trains()

            elif ch == 2:
                admin1.add_train(train_list)

            elif ch == 3:
                admin1.cancel_train(train_list)

            elif ch == 4:
                admin1.update_train(train_list)

            elif ch == 5:
                print("Total Income:", admin1.total_income())

            elif ch == 6:
                break

            else:
                print("Invalid choice")

    else:
        print("Admin not found")        

else:
    print("Invalid entry")   

              
               

#  Railway Management System

A console-based Railway Management System built in Python using Object-Oriented Programming (OOP). It allows passengers to book, check, and cancel tickets, and admins to manage trains and view total income.

---

##  Features

### 👤 Passenger
- View all available trains
- Book a ticket
- Check ticket details by ID
- Cancel a ticket

###  Admin
- View all trains
- Add a new train
- Cancel/remove a train
- Update train details
- View total income from all booked tickets

---

##  Project Structure

```
railway-management-system/
│
├── main.py            # Main program file
├── passenger.txt      # Stores valid passenger credentials
├── admin.txt          # Stores valid admin credentials
└── README.md          # Project documentation
```

---

##  File Format

### passenger.txt
Each line contains one passenger in this format:
```
name,phone_number
Ahmed,03001234567
Sara,03219876543
```

### admin.txt
Each line contains one admin in this format:
```
name,phone_number,email
Ali,03001112222,ali@gmail.com
```

---

##  How to Run

### Step 1 — Make sure Python is installed
```bash
python --version
```
If not installed, download from: https://www.python.org

### Step 2 — Clone the repository
```bash
git clone https://github.com/your-username/railway-management-system.git
cd railway-management-system
```

### Step 3 — Create the credential files
Create `passenger.txt` and `admin.txt` in the same folder as `main.py` with the format shown above.

### Step 4 — Run the program
```bash
python main.py
```

---

##  OOP Concepts Used

| Concept | Where Used |
|---|---|
| Classes | Train, Ticket, Passenger, Admin |
| Objects | Created for each train, ticket, passenger, admin |
| Methods | book_ticket(), cancel_ticket(), add_train() etc. |
| Encapsulation | Each class manages its own data |
| Lists | train_list, all_passengers, self.ticket |

---

##  Classes Overview

### `Train`
Stores details of a train: name, from, to, time, type, fare.

### `Ticket`
Stores details of a booked ticket: ID, train name, route, type, fare.

### `Passenger`
Handles passenger operations: view trains, book/check/cancel tickets.

### `Admin`
Handles admin operations: add/view/update/cancel trains, view income.

---

##  Login System

- Credentials are loaded from `passenger.txt` and `admin.txt` at startup
- Login checks name + phone for passengers
- Login checks name + phone + email for admins
- Uses exception handling so program does not crash if files are missing

---

##  Key Concepts in Code

| Feature | Description |
|---|---|
| `while True` | Keeps the program running until user exits |
| `break` | Exits the loop when user chooses to leave |
| `found` flag | Tracks whether login was successful |
| `try/except` | Exception handling for missing files |
| `str` for phone | Phone stored as string to preserve leading zeros |
| `"-" * 30` | Prints separator line between train listings |

---

## 👨‍💻 Author

**Your Name**  : Taha Bajwa
GitHub: [@your-username](tahabajwaa888-lab)



from datetime import datetime

class Response:
    attributes = {
        'negative_res': ["no", "nope", "nah", "no thanks", "no thank", "sorry"],
        'exit_words': ["bye", "exit", "quit", "goodbye", "later"]}

# salutations at the start of chat
    def wishes(self):
        print("Welcome to our system!!")
        name = input("What's your name: ")
        print("Hii " + name + " :)")
        self.select()

# exit commands from attributes dictionary
    def exit(self, reply):
        for i in Response.attributes:
            return reply.lower()

# Options available on portal
    def select(self):
        print("How may I help you ?")
        print("1. Attendance issue")
        print("2. Attendance update issue")
        print("3. Payments")
        print("4. Attendance records")

        choice = input("Enter the number corresponding to your choice: ")
        if choice == "1":
            print(self.attendance_query())
        elif choice == "2":
            print(self.attendance_updated())
        elif choice == "3":
            print(self.payment())
        elif choice == "4":
            print(self.attendance_record())
        else:
            print("Thank You!! Have a nice day")

# Attendance related issues on field
    def attendance_query(self):
        print("Great! Please choose from the following options:")
        print("1. Camera issue")
        print("2. Network problem")
        print("3. Attendance not marked")

        choice = input("Enter the number corresponding to your choice: ")
        if choice == "1":
            self.camera_issue()
        elif choice == "2":
            self.net_issue()
        elif choice == "3":
            self.attendance_not_marked()
        else:
            print("Invalid choice. Please select a valid option.")

    def camera_issue(self):
        a = datetime.now()
        print(f"Query : Camera related issue \nIssue raised on : {a} "
              f"\nEstimated issue resolve date : 2023-12-01 23.59.59")

        self.select()

    def net_issue(self):
        a = datetime.now()
        print(
            f"Query : Network related issue \nIssue raised on : {a} \n"
            f"Please check your network or else try after some time.")

        self.select()

    def attendance_not_marked(self):
        a = datetime.now()
        b = input("Enter date on which attendance is not marked : ")
        print(f"Query : Attendance not marked \nIssue raised on : {a} \nAttendance Marked for the date {b}. "
              f"\nThank you !! Have a nice day :)")

        self.select()

# attendance update issue on portal
    def attendance_updated(self):
        print("Great! Please choose from the following options:")
        print("1. Attendance not updated yet")
        print("2. Not able to see my attendance")
        print("3. Leave not updated")

        choice = input("Enter the number corresponding to your choice: ")
        if choice == "1":
            self.update()
        elif choice == "2":
            self.view()
        elif choice == "3":
            self.leave()
        else:
            print("Invalid choice. Please select a valid option.")

    def update(self):
        a = input("Enter the date at which attendance is not yet updated : ")
        b = datetime.now()
        print(
            f"Query : Yet attendance is not updated.\nIssue raised on : {b}\nAttendance is updated for the date {a}"
            f"\nThank you !! Have a nice day :)")

        self.select()

    def view(self):
        a = datetime.now()
        print(f"Query : Can't view attendance. \nIssue raised on : {a}"
              f"\nYour page will get updated within an hour.\nThank you for your valuable update.\nHave a good day ;D")

        self.select()

    def leave(self):
        a = datetime.now()
        print(f"Query : Leave not updated.\nIssue raised on : {a}"
              f"\nYour leave will get updated within an hour.\nSorry for the delay")

        self.select()

# payment related issue
    def payment(self):
        print("Great! Please choose from the following options:")
        print("1. Payment Slip")
        print("2. Payment not done")

        choice = input("Enter the number corresponding to your choice: ")
        if choice == "1":
            self.slip()
        elif choice == "2":
            self.pay()
        else:
            print("Invalid choice. Please select a valid option.")

    def slip(self):
        a = input("Enter the year for which payment slip is to be generated : ")
        b = datetime.now()
        print(f"Query : Payment slip.\nIssue raised on : {b}"
              f"\nPayment Slip pdf document sent on your registered mail account successfully for the year {a}. "
              f"\nThank you !! Have a nice day :)")

        self.select()

    def pay(self):
        a = datetime.now()
        print(f"Query : Payment not yet received. \nIssue raised on : {a}"
              f"\nPayment is not received yet.\nQuery noted. \nEstimated resolve date: 21/12/2023 \nHave a good day :D")

        self.select()

# to fetch attendance or absence or leaves records
    def attendance_record(self):
        print("Great! Please choose from the following options:")
        print("1. Attendance record")
        print("2. Leave record")
        print("3. Absence record")

        choice = input("Enter the number corresponding to your choice: ")
        if choice == "1":
            self.record()
        elif choice == "2":
            self.leave_record()
        elif choice == "3":
            self.absence()
        else:
            print("Invalid choice. Please select a valid option.")

    def record(self):
        a = input("Enter the month for which your attendance record is to be generated : ")
        b = datetime.now()
        print(f"Query : Attendance records slip.\nIssue raised on : {b}"
              f"\nAttendance record pdf document is sent on your registered mail account successfully for month of {a}."
              f"\nThank you !! Have a nice day :)")

        self.select()

    def leave_record(self):
        a = input("Enter the month for which your leave record is to be generated : ")
        b = datetime.now()
        print(f"Query : Leave record. \nIssue raised on : {b}"
              f"\nLeave record pdf document is sent on your registered mail account successfully for the month of {a}. "
              f"\nHave a good day :D")

        self.select()

    def absence(self):
        a = input("Enter the month for which your absence record is to be generated : ")
        b = datetime.now()
        print(f"Query : Absence record.\nIssue raised on : {b}"
              f"\nAbsence record pdf document is sent on your registered mail account successfully for month of {a}. "
              f"\nThank you !! Have a nice day :)")

        self.select()

chat = Response()
chat.wishes()

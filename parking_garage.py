class ParkingGarage():
    """
    What represents a parking garage
    """
    def __init__(self, spaces, pay, leave, response):
        self.spaces = 5
        self.pay = False
        self.leave = True
        self.response = {'yes'}, {'no'},

    def takeTicket(self):
        if self.spaces == 0:
            print("There are not more parking spaces available")
        else:
            self.spaces -= 1
            print(f'Great, here is your ticket. There are now {self.spaces} spaces left')
            
    def addPayment(self):
        while not self.pay:
            response = input("Do you want to pay for your parking?" )
            if response.lower() == 'yes':
                print(f"Thank you for paying. have a great day! There are now {self.spaces} spaces left")
            elif response.lower() == 'no':
                print(f"Please Pay for Your Parking.")
        

    def LeaveGarage(self):
        while True:
            if self.spaces <= 5:
                self.pay == True
                self.spaces += 1
                response = input("Have you already paid for the garage? " "Or do you need to pay for a ticket? ")
            if response.lower() == 'yes':
                print("Please insert ticket into the machine." + " Have a nice day!")
            else :
                response.lower() == "I need a ticket"
            self.pay == False
            #input("You must pay for your parking before you leave!")
            print("Please Provide Payment, by selecting p at the main screen")
            break


    def run(self):
        while True:
            response = input('Welcome to "Saronia Parking"! Type t for ticket, p for pay or l to leave.')
            if response.lower() == "t":
                self.takeTicket()
            if response.lower() == "p":
                self.addPayment()
            if response.lower() == "l":
                self.LeaveGarage()

Car = ParkingGarage(0, 0, 0, 0,)
Car.run()

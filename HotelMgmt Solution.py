class HotelMgmt:
    def __init__(self,name="",phno="",address="",cindate="",coutdate="",s=0,r=0,t=0,x=100, roomno=1):
        self.name=name
        self.phno=phno
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.s=s
        self.r=r
        self.t=t
        self.x=x
        self.roomno=roomno
        
    def Bookings(self):
        self.name=input("Enter your name:")
        self.phno=input("Enter your phone number:")
        self.address=input("Enter your address:")
        self.cindate=input("Enter your check in date(dd/mm/yyyy):")
        self.coutdate=input("Enter your check out date(dd/mm/yyyy):")
        print("Your room no :",self.roomno)

		
    def Room_Info(self):
        print("Select Room Type")
        print("1. Type A--->$30")
        print("Room amenities include:Single Bed,Double Door Cupboard,Attached Wahroom with hot/cold water,Telephone")
        print("2. Type--->$40")
        print("Room amenities include:Double Bed,Double Door Cupboard,Attached Wahroom with hot/cold water,Telephone and Balcony")
        print("3. Type--->$50")
        print("Room amenities include:1 Double Bed,1 Single Bed,Triple Door Cupboard,Attached Wahroom with hot/cold water,Telephone and Balcony")
        b=int(input("Enter your choice:"))
        c=int(input("Enter the number of nights you want to stay:"))
        if b==1:
            self.s=30*c
        if b==2:
            self.s=40*c
        if b==3:
            self.s=50*c
        else:
            print("Please select a room")

            
    def additional_ammenities(self):
        print("Additional Ammenities Menu")
        print("1.AC:$10/n","2.TV:$8/n","3.Couch:$5/n","4.Table with 2 seater sofa:$6/n”,5..Gym:$7”/n,0.None/n")
        while(1):
            d=int(input("Enter your choice:"))
            if d==1:
                self.r=self.r+self.s
            elif d==2:
                self.r=self.r+self.s
            elif d==3:
                self.r=self.r+self.s
            elif d==4:
                self.r=self.r+self.s
            elif d==5:
                self.r=self.r+self.s
            elif d==0:
                break;
            else:
                print("You have choosen an invalid option")
            print ("Total Room Cost=$",self.r)

            
    def Food(self):
        print("RESTAURANT MENU")
        print("1.Dessert:$4","2.Drinks:$3","3.Breakfast:$5","4.Lunch:$6","5.Dinner:$5","0.Exit")
        while (1):
            e=int(input("Enter the number of your choice:"))
            
            if (e==1):
                f=int(input("Enter the quantity:"))
                self.t=self.t+100*f
            elif (e==2):
                f=int(input("Enter the quantity:"))
                self.t=self.t+50*f
            elif (e==3):
                f=int(input("Enter the quantity:"))
                self.t=self.t+90*f
            elif (e==4):
                f=int(input("Enter the quantity:"))
                self.t=self.t+110*f
            elif (e==5):
                f=int(input("Enter the quantity:"))
                self.t=self.t+150*f
            elif (e==0):
                break;
            else:
                print("You've Enter an Invalid Key")
            print("Total food Cost=Rs",self.t,"\n")

		
    def Payment(self):
        print("HOTEL BILL")
        print("Customer details:")
        print("Customer name:",self.name)
        print("Customer phno:",self.phno)
        print("Customer address:",self.address)
        print("Check in date:",self.cindate)
        print("Check out date",self.coutdate)
        print("Room no.",self.roomno)
        print("Your Room rent is:",self.r)
        print("Your Food bill is:",self.t)
        print("Your Total is:",self.r+self.t)

	
    def main():
    x=HotelMgmt()
    
    while(1):
        print("1.Bookings")
        print("2.Room_Info")
        print("3.Food")
        print("4.Payment")
        print("0.Exit")
        y=int(input("Enter the number of your choice:"))
        if (y==1):
            x.Bookings()
        if (y==2):
            x.Room_Info()
        if (y==3):
            x.Food()
        if (y==4):
            x.Payment()
        if (y==5):
            quit()

    if __name__ == "__main__":
    main()

    
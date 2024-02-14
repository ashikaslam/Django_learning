



class User:
    def __init__(self,name,nid) -> None:
        self.name = name 
        self.nid =nid
        self.user_code = None
        self.email = None
        self.password = None
        self.ballance = 0
        self.Loan = 0
        self.history = []



    def register(self,bank):
        print("HELLO ",self.name)
        if self.user_code !=None:
            print("you are already a user!!")
            flag = int(input("press 1 to login your account to exit pre any but 1>>"))
            if flag == 1:self.login(bank)
            else :
                print("have a good day")
        else :
            email = input("enter your email>>")
            password = input("enter your passowed>>")
            flag =  bank.register_system(self, email ,password)
            if flag ==0:
                return 
            print("successfully registered to bank!!")
            print("now please login again to continue the next activeties")
            self.login(bank)
        

    def login(self,bank):
        print("HELLO ",self.name)
        email = input("enter your email>>")
        password = input("enter your passowed>>")
        flag = 0
        flag =  bank.login(email,password)
        if flag == 0:
            print("invalied email or password try again or creat a new account")
            return None

        print("successfully login to bank!!")
        print("press 1 to chack ballance>")
        print("press 2 to withdraw >")
        print("press 3 to diposit>")
        print("press 4 to send money>")
        print("press 5 to loan>")
        print("press 6 history>")
        print("press exit pree other>")


        choice = int(input("enter your choice>>"))
        if choice == 1:
            self.chack_balance()
        elif choice == 2:
            amount  = int(input("entr the amount you want to withdraw>>"))
            self. withdraw(bank,amount)

        elif choice == 3:
           amount  = int(input("entr the amount you want to diposti>>"))
           self.diposit(bank,amount)
        elif choice == 4:
          userid = int(input("enter the use id>>"))
          amount  = int(input("entr the amount you want to send>>"))
          self.transfer_money(bank,userid,amount)
        elif choice == 5:
            amount  = int(input("entr the amount you want to loan>>"))
            self.loan(bank,amount)
           
        elif choice ==6:
           self.chack_history()
        else :return ""



    def chack_balance(self):
        print("your current ballance is ", self.ballance)

    def diposit(self,bank,amount):
        bank.diposit_request(self,amount)

    
    def withdraw(self,bank,amount):
        bank.withdraw_request(self,amount)

    def loan(self,bank,amount):
       bank.loan_request(self,amount)

    def chack_history(self):
        for i in self.history:
            print(">>>>>>>>>>")
            print(i)

    def transfer_money(self,bank,reciever_id,amount):
        bank.send_money_request(self,reciever_id,amount)
       



    def __repr__(self) -> str:
       return f"""
       Name > {self.name}
       Nid >  {self.nid}
       Email > {self.email}
       Idcod > {self.user_code}
       BALLANCE  > {self.ballance}
       LOAn = {self.Loan}
       """


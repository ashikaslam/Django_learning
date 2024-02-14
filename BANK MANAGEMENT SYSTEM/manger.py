      


class Manager:
    def __init__(self,name,nid) -> None:
       self.name = name
       self.nid = nid
       self.email = None
       self.password = None


    def register(self,bank):
       print("HELLO ",self.name)
       email = input("enter your email>>")
       password = input("enter your password>>")
       flag=  bank.manager_register(self,email,password)
       if flag ==0:
           return
       elif flag ==1:
           self.login(bank)
       elif flag == 2:
          print("successfully registred so please login again to continue")
          self.login(bank)




    def login(self,bank):
       print("HELLO ",self.name)
       email = input("enter your email>>")
       password = input("enter your password>>")
       flag=  bank.manager_login(email,password)

       if flag ==0:return
       elif flag ==1:
           self.register(bank)
       elif flag == 2:
           

        print("press 1 to chack ballance>")
        print("press 2 to stop loan service >")
        print("press 3 to on loan service >")
        print("press 4 to see history>")
        print("press 5 to see total loan>")
        print("to exit press other>")
        choice = int(input("enter your choice>>"))

        if choice ==1:self.chack_ballance(bank)
        elif choice == 2:self.stop_loan_service(bank)
        elif choice ==3:self.on_loan_service(bank)
        elif choice == 4:self.see_all_tarnsaction_history(bank)
        elif choice == 5:self.see_loan(bank)
        else:
           print("have a good day ")
           return
           
          

    def chack_ballance(self,bank):
       print( bank.banllance)
    
    def stop_loan_service(self,bank):
        bank.loan_if_availavle = False

    def on_loan_service(self,bank):
        bank.loan_if_availavle = True

    def see_all_tarnsaction_history(self,bank):
      bank.see_historY()

    def see_loan(self,bank):
       print(bank.loan_amount())
       

    def __repr__(self) -> str:
       return f"""
       POSITON > MANAGER
       NAME  > {self.name}
       EMAIL > {self.email}
       """
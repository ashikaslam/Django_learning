from transaction import*

class Bank:
   def __init__(self,name,initial_acount_balance) -> None:
      self.name = name
      self .__balance = initial_acount_balance
      self.next_user_code = 101
      self.history =[]
      self.user_with_id = {}
      self.email_pass = {}
      self.loan_if_availavle = True
      self.total_subscriber = 0
      self.total_loan = 0

      self.manager = None
      self.manager_pass = None
      self.manager_email = None
############################   for manager    ################################

   def manager_register(self,manager,email,password):
      if self.manager == manager:
         print("you are registered as manager so pleas login to continue")
         return 1
      if self.manager !=None:
         print("we have allready a manager so we do not need anoter one")
         return 0
      self.manager = manager
      self.manager_email = email
      self.manager_pass = password
      manager.email = email
      manager.password = password
      return 2


   def manager_login(self,email,password):
      if self.manager == None:
         print("yor are not register again and we also need a manager so pleas registerfirst to continue")
         return 1
      if email != self.manager_email or password != self.manager_pass:
         print("invalid password or email !!")
         print(email,self.manager_email)
         print(password,self.manager)
         return 0
      if email == self.manager_email and password == self.manager_pass:
         print("succesfully login !!")
         return 2
      


   def see_historY(self):
      print("---------OVER ALL TRANSACTION HISTORY OF THE BANK ----------")
      for  i in self.history:
         print(i)

   @property
   def banllance(self):
      return self.__balance
   
   def loan_amount(self):return self.total_loan

########################  for user  ###########################

   def register_system(self,user,email,passwoed):
      if email in self.email_pass:
         print("there is already a user id with this email so you can not creat a new id with it")
         return 0
      user.user_code = self.next_user_code
      self.next_user_code+=1
      self.email_pass[email] = passwoed
      self.user_with_id[user.user_code] = user
      self.total_subscriber+=1
      user.email = email
      user.password = passwoed
      return 1

   def login(self,email,passwoed):
      if email not in self.email_pass:
         return 0
      if self.email_pass[email]!= passwoed:
         return 0
      return 1


###########################################

   def diposit_request(self,user,amount):
      if amount>0:
         self.__balance+=amount
         user.ballance+=amount
         new_tansaction = Diposit_Transaction(user,amount)
         user.history.append(new_tansaction)
         self.history.append(new_tansaction)
         print("see the new tansaction")
         print(new_tansaction)
#####################################################

   def withdraw_request(self,user,amount):
      if user.ballance<amount:
         print("you do not have sufficient ballacne")
         return
      else :
         user.ballance-=amount
         self.__balance-=amount
         new_tansaction = Withdrawal_Transaction(user,amount)
         user.history.append(new_tansaction)
         self.history.append(new_tansaction)
         print("see the new tansaction")
         print(new_tansaction)

####################################################
   def loan_request(self,user,amount):
      if self.loan_if_availavle  or amount < self.__balance:
        if amount>user.ballance*2:
           print("you are not eligible to get a loan of this amount ")
           return
        else :
           user.ballance+=amount
           self.__balance-=amount
           new_tansaction= Lona_Transaction(user,amount)
           user.history.append(new_tansaction)
           self.history.append(new_tansaction)
           user.Loan+=amount
           print("see the new tansaction")
           print(new_tansaction)
           self.total_loan+=amount

      else :
         print("sorry this service is now avilavle due to our internel problem>>")


#######################################################
   def send_money_request(self,sender,reciever_id,amount):
      if sender.ballance<amount:
         print(" you do not have enough money")
         return
      if reciever_id not in self.user_with_id:
         print("could not find any user with the given id")
         return

      sender.ballance-=amount
      self.user_with_id[reciever_id].ballance+=amount
      new_tansaction = Send_Money(sender,amount, self.user_with_id[reciever_id])
      sender.history.append(new_tansaction)
      trans_mony =  Money_transfer(sender,amount, self.user_with_id[reciever_id])
      self.history.append(trans_mony)
      print("see the new tansaction")
      print(new_tansaction)
      new_tansaction1 = Receive_Money(sender,amount, self.user_with_id[reciever_id])
      self.user_with_id[reciever_id].history.append(new_tansaction1)

      print(new_tansaction1)


   

##########################################################
















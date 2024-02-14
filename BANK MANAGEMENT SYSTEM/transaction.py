from datetime import datetime


class Transaction:
    def __init__(self,user,amount) -> None:
       self.name = user.name
       self.amount = amount
       self.time = datetime.today()
       self.userId = user.user_code
       self.crrent_ballance = user.ballance
       


class Lona_Transaction(Transaction):
    def __init__(self, user, amount) -> None:
        super().__init__(user, amount)
       
    def __repr__(self) -> str:
        return f"""
-------- LOAN ---------
USER NAME >  {self.name}
USER CODE > {self.userId}
LOAN AMOUNT > {self.amount}
CURRENT BALLANCE > {self.crrent_ballance}
TIME > {self.time}
        """
    


class Diposit_Transaction(Transaction):
    def __init__(self, user, amount) -> None:
        super().__init__(user, amount)
       
    def __repr__(self) -> str:
        return f"""
-------- DIPOSIT ---------
USER NAME >  {self.name}
USER CODE > {self.userId}
DIPOSIT AMOUNT > {self.amount}
CURRENT BALLANCE > {self.crrent_ballance}
TIME > {self.time}
        """
    


class Withdrawal_Transaction(Transaction):
    def __init__(self, user, amount) -> None:
        super().__init__(user, amount)
       
    def __repr__(self) -> str:
        return f"""
-------- WITHDRAWAL ---------
USER NAME >  {self.name}
USER CODE > {self.userId}
WITHDRAWAL AMOUNT > {self.amount}
CURRENT BALLANCE > {self.crrent_ballance}
TIME > {self.time}
        """
    

class Send_Money(Transaction):
    def __init__(self, user, amount,receiver) -> None:
        super().__init__(user, amount)

        self.receiver_id = receiver.user_code
        self.receiver_name = receiver.name


    def __repr__(self) -> str:
        return f"""
-------- SEND MONEY ---------
RECEIVER NAME >  {self.receiver_name}
RECEIVER CODE > {self.receiver_id}
SEND AMOUNT > {self.amount}
CURRENT BALLANCE > {self.crrent_ballance}
TIME > {self.time}
        """
    


class Receive_Money(Transaction):
    def __init__(self, user, amount,receiver) -> None:
        super().__init__(user, amount)
        self.ricive_balance=receiver.ballance 

    def __repr__(self) -> str:
        return f"""
-------- RECEIVE MONEY ---------
SENDER NAME >  {self.name}
SENDER CODE > {self.userId}
SEND AMOUNT > {self.amount}
CURRENT BALLANCE > { self.ricive_balance}
TIME > {self.time}
        """
    


# this  class only for the  bank 
class Money_transfer(Transaction):
    def __init__(self, user, amount,reciever) -> None:
        super().__init__(user, amount)
        self.r_name = reciever.name
        self.r_id = reciever.user_code
        self.r_ballence = reciever.ballance

    def __repr__(self) -> str:
        return f"""
-------- MONEY TRANSFER ---------
         < SENDER >
SENDER NAME >  {self.name}
SENDER CODE > {self.userId}
TRANSFERED AMOUNT > {self.amount}
SENDER CURRENT BALLANCE > {self.crrent_ballance}

         < RECEIVE >
RECEIVER NAME >  {self.r_name}
RECEIVER CODE > {self.r_id}
SEND AMOUNT > {self.amount}
CURRENT BALLANCE > { self.r_ballence}

TIME > {self.time}
        """
        
        

    



from Bank import*
from User import*
from manger import*






def main():
    #creating the Bank
    bank1 = Bank("gramin_bank",10000)# the bank has initiallay 10000 tk

    # creating manage>>
    manager1 = Manager("Md Goalm","1234**")
    manager1.register(bank1) # want to register in the bank as managr
    
    # see the manager id card 
    #print(manager1)


    # now we will creat some user but the users initially are not cannected with bank to do it they must resigter in the system
    person1 = User("aslam",12234)
    person1.register(bank1)
    # see the person1  id card 
    #print(person1)


    # creat anoter user to send money 

    person2 = User("monir",12244) # here "12244" is NID not user id so care full
    person2.register(bank1)

    print("the person2  information is ")
    print(person2)

    # now person1 will login to send money to person 2 and person2 user id  will be 102 by the system

    person1.login(bank1)


    # now manager will login to see his bank history 

    manager1.login(bank1)



    #### and like this you can chacke any think you whant 
    
    



    





    
    

    
    # print(person1)
    # person1.login(bank1)
    # print(bank1.banllance)
    # print(person1)

    # person2 = User("monir",12234)
    # person2.register(bank1)
    # print(person2)
    # person1.login(bank1)



    

   



if __name__ == "__main__":main()
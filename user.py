class User:
    def __init__(self, first_name , last_name , email , age):
        self.user_first = first_name
        self.user_last = last_name
        self.user_email = email
        self.user_age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(self.user_first)
        print(self.user_last)
        print(self.user_email)
        print(self.user_age)

    def enroll(self):
        if self.is_rewards_member != True:
            self.is_rewards_member = True
        else:
            print("Looks like you're already a member!")
            return
        print(self.is_rewards_member)
        if self.gold_card_points == 0:
            self.gold_card_points += 300
        print(self.gold_card_points)

    def spend_points(self, ammount):
        if ammount < self.gold_card_points:
            self.gold_card_points -= ammount
            print("Purchase Succesful")
        else:
            print("You need mo' cheese")


user_1 = User("Gunnar" , "Walsh" , "gunnarwalsh@gmail.com" , 24)
user_2 = User("Matison" , "Cain" , "mcain@email.com" , 25)
user_3 = User("Wyatt" , "McKimmie" , "wkim@gmail.com" , 26)

user_1.spend_points(50)
# user_2.is_rewards_member = True // Testing if it will change values
user_2.enroll()
user_2.spend_points(80)

user_1.display_info()
user_2.display_info()

user_3.spend_points(40)

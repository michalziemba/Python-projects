class User:
    def __init__(self, user_id, username, followers):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


class Car:
    def enter_race_model(self):
        self.seats = 2


my_car = Car()
my_car.enter_race_model

user_1 = User("001", "Michal")

print(user_1.username)

user_2 = User()

user_1.follow(user_2)


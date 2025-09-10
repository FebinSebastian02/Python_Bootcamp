class User:

    # A constructor is used to initialize the object. Attributes are the things that the object possess.
    def __init__(self, user_id, user_name):  # Self is the actual object that is being initialized.
        self.user_id = user_id
        self.name = user_name
        self.followers = 0  # Setting a default value
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1

user_1 = User("1", "Febin")
user_2 = User("2", "Sebastian")
user_1.follow(user_2)


print(user_1.name)
print(user_2.name)
print(user_1.following)
print(user_2.following)
print(user_1.followers)
print(user_2.followers)

# Initializing the variables explicitly
"""user_1 = User()
user_1.id = "1"
user_1.name = "Febin"

user_2 = User()
user_2.id = "2"
user_2.name = "Sebastian"""

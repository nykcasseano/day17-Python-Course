class User:
    def __init__(self, user_id, username, follower):
        self.id = user_id
        self.username = username
        self.follower = 0
        
user_1 = User("001", "Nyk")
user_2 = User("002", "Bia")
class User:
    
    def __init__(self, first_name, last_name, **profile):
        self.profile = {}
        self.profile['first_name'] = first_name
        self.profile['last_name'] = last_name
        self.profile['login_attempts'] = 0
        self.profile.update(profile)

    def increment_login_attempt(self, attempt):
        self.profile['login_attempts'] += attempt

    def reset_login_attempt(self):
        self.profile['login_attempts'] = 0

        
new_user = User('mike','makiling')
print(new_user.profile['login_attempts'])
new_user.increment_login_attempt(4)
print(new_user.profile['login_attempts'])
new_user.reset_login_attempt()
print(new_user.profile['login_attempts'])



from user import User


class Admin(User):

    def __init__(self, first_name, last_name, **profile):
        super().__init__(first_name, last_name, **profile)
        self.priviliges = ['can add post', 'can delete post', 'can be user']


admin1 = Admin('marty', 'umlas')

print(admin1.priviliges)

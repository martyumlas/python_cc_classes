class User:

    def __init__(self, first_name, last_name, **profile):
        self.profile = {}
        self.profile['first_name'] = first_name
        self.profile['last_name'] = last_name
        self.profile.update(profile)



mike = User('mike', 'makiling', work='director', status='active')

print(mike.profile['first_name'])

class Employee:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return self.name or self.email

    def __eq__(self):
        return self.name == other.name or self.email == other.email

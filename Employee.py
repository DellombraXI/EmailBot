class Employee:
    "" Class to represent an employee
    
    Attributes
    
    name: str
        Name of employee
    email: str
        Email of employee
    """

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return self.name or self.email

    def __eq__(self):
        return self.name == other.name or self.email == other.email

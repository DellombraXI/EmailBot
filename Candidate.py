class Candidate:
    """ Class to respresent a candidate and is assigned when the end date is within 2 days
    
    Attributes
    
    handler: str
        Name of the employee associated with the candidate
    handler_email: str
        Email of the employee associated with the candidate
    name: str
        First name of candidate
    l_name: str
        Last name of candidate
    end: int
        End date in # of days
    """

    def __init__(self, handler, handler_email, name, l_name, end):
        self.handler = handler
        self.name = name
        self.l_name = l_name
        self.handler_email = handler_email
        self.end = end

    def __str__(self):
        return str(self.handler)

class Candidate:

    def __init__(self, handler, handler_email, name, l_name, end):
        self.handler = handler
        self.name = name
        self.l_name = l_name
        self.handler_email = handler_email
        self.end = end

    def __str__(self):
        return str(self.handler)

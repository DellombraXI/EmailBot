class Main:
    employee_dict = {
        'AA': 'April',
        'GO': 'Gaby'
    }

    def __init__(self):
        self.candidates = []
        self.employees = []
        self.__gen_employees()
        self.email_list = []

    def __gen_employees(self):
        self.employees.append(Employee('April', 'april.anolin@kellyservices.com'))
        self.employees.append(Employee('Gaby', 'gabriela.ong@kellyservices.com'))

    def notifymaster(self):

        password = 'Dylandylan2'
        sent_from = 'kellyservices.bot@gmail.com'
        to = [test_email]
        subject = 'RUN'
        body = 'RUN'

        msg = MIMEMultipart()
        msg['To'] = ', '.join(to)
        msg['From'] = sent_from
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sent_from, password)
            server.sendmail(sent_from, to, msg.as_string())

    def sendemail(self):

        for candidate in self.email_list:
            password = 'Dylandylan2'
            sent_from = 'kellyservices.bot@gmail.com'
            to = [candidate.handler_email]
            subject = ('Assignment Completion - {}, {}'.format(candidate.l_name, candidate.name))
            body = ('Hi {}! Your candidate {}, {} will reach the end of their assignment in {} days.'.format(
                candidate.handler, candidate.l_name, candidate.name, candidate.end))
            msg = MIMEMultipart()
            msg['To'] = ', '.join(to)
            msg['From'] = sent_from
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(sent_from, password)
                server.sendmail(sent_from, to, msg.as_string())

    def run(self):
        complete = False
        place_holder = 1
        while complete is False:
            print('Scraping data...')
            try:
                for i in range(place_holder, len(sheet.col_values(1))):
                    place_holder += 1
                    if i % 10 == 0:
                        print('...')
                    extract_row = sheet.row_values(i + 1)
                    try:
                        end_date = extract_row[0]
                        end_date = end_date.split('/')
                        end_date = [int(i) for i in end_date]
                        end_date.insert(0, end_date[-1])
                        end_date.pop(-1)
                        end_day = int(datetime.datetime(end_date[0], end_date[1], end_date[2]).strftime('%j'))
                    except:
                        pass

                    # Simulate end condition for testing
                    # if i == 50:
                    # end_day = today + 2
                    # if i == 1:
                    # end_day = today + 3

                    if end_day - today == 2 and end_date[0] == year:
                        print('Assignment end detected')
                        end = end_day - today
                        handler = self.employee_dict[extract_row[1]]
                        # If candidate split between two people i.e 'AA/GO' then take first employee
                        if len(handler) > 2:
                            handler_split = handler.split('/')
                            handler = handler_split[0]

                        for employee in self.employees:
                            if handler == employee.name:
                                self.email_list.append(
                                    Candidate(handler, employee.email, extract_row[3], extract_row[2], end))
                                print("Candidate added!")
                complete = True
            except:
                print('Scraping interrupted. Retrying in 10 seconds')
                time.sleep(10)
                pass

        print('Scraping Complete!')

        if len(self.email_list) > 0:
            try:
                print('Sending out emails')
                self.sendemail()
                print('Email(s) sent! End of program.')
            except:
                print('Failed to send email! End of program.')
        else:
            print('No approaching assignment completion. End of program.')

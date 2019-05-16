# EmailBot requires specific python libraries including gspread and oauth2client to operate, as well as operation credentials stored via JSON file.

EmailBot is a program written for Kelly Services Inc., a recruiting firm, to automate the process of managing candidates. Employees addressed an issue about often being unaware of the approaching assignment completion dates of their candidates. To combat this issue, this program was written to keep track of candidate dates and alert the respective employee if the assignment completion is within 2 days. 

The work flow consists of the following:

1) Extract data using the Google API and Google Spreadsheets
2) Scan for completion dates and compare with regards to current date 
3) If candidate is approaching their assignment completion, add candidate to a list on local memory
4) Continue scraping spreadsheet until completion
5) Open the previous created list, extract candidate information and send an email to the respective employee.
6) Program is scheduled to run every weekday at 2 PM as asked by employer

An example email looks like this: 
- To: [Whichever employee is in charge of candidate as listed on spreadsheet]
- From: kellyservices.bot@gmail.com
- Subject: 'Assignment Completion - Doyle, Dylan'
- Body: 'Hi Gabriela, your candidate Doyle, Dylan will be reaching the end of their assignment in 2 days.'

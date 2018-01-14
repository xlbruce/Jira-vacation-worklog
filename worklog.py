# TODO parametrize script and use an getopt library like
import sys
import requests
from datetime import datetime
from datetime import date
from datetime import timedelta

startDateStr = '2018-12-01'
days = 30
requestTemplate = open('request-template.json', 'r').read()
urlIssue = 'https://example.com/rest/api/2/issue/ISSUE-1/worklog'

startDate = datetime.strptime(startDateStr, "%Y-%m-%d").date()
endDate = startDate + timedelta(days=days)
datesWithWeekend = [ startDate + timedelta(days=x) for x in range(0, days) ]
# Ignore weekends
dates = [ date for date in datesWithWeekend if not date.weekday() == 5 if not date.weekday() == 6 ]

credentials = ('user@company.com', 'password')
header = { 'Content-Type': 'application/json' }

for date in dates:
    requestBody = requestTemplate.replace('%s', str(date))
    request = requests.post(urlIssue, data=requestBody, headers=header, auth=credentials)

    if not request.status_code == 201:
        # TODO improve debug message
        print date

import requests
import json
from test_parser import *

with open('../resources/configs.json', 'r') as f:
    config = json.load(f)


# print(config['URL']['SCHEDULE_PAGE'])

# page = requests.get(config['URL']['RECRUIT_PAGE']).text
# NoticesParser.parse(page)
# ImportantNoticesParser.parse(page)
#
# page = requests.get(config['URL']['ACADEMIC_PAGE']).text
# NoticesParser.parse(page)
# ImportantNoticesParser.parse(page)

# page = requests.get(config['URL']['SCHOLAR_PAGE']).text
# NoticesParser.parse(page)
# ImportantNoticesParser.parse(page)
#
# page = requests.get(config['URL']['EVENT_PAGE']).text
# NoticesParser.parse(page)
# ImportantNoticesParser.parse(page)

# page = requests.get(config['URL']['NOTICE_PAGE']).text
# NoticesParser.parse(page)
# ImportantNoticesParser.parse(page)
#
page = requests.get(config['URL']['SCHEDULE_PAGE']).text
ScheduleParser.parse(page)
#

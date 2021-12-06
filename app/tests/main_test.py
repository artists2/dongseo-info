from test_parser import Parsing
# from parsing import Parsing

# test_parser_schedule = Parsing('https://www.dongseo.ac.kr/kr/index.php?pCode=dscalendar')  # test code
# test_parser_schedule.schedule_parser()
#
# 12.08(수)~12.14(화) 보강주간
# 12.15(수)~12.21(화) 기말고사
# 12.15(수)~12.22(수) 성적입력기간
# 12.21(화) 종강
# 12.22(수) 계절학기개강
# 12.23(목)~12.24(금) 성적정정기간
# 12.25(토) 성탄절

test_parser_important_academic = Parsing("https://www.dongseo.ac.kr/kr/index.php?pCode=MN2000194")
test_parser_important_academic.important_academic()

page = requests.get(_page)
ScheduleParser.parse()
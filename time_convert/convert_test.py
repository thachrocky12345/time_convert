from time_convert import TimeConvertor

run = TimeConvertor()

print run.convert_current_to_timezone('CST')


print run.convert_tztime_to_timezone('2016-01-15 09:34:00','CST', 'EST')
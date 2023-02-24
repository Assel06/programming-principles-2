from datetime import datetime, time
def dateDifferenceInSeconds(dt2, dt1):
    timedelta = dt2 - dt1
    return timedelta.days *  24 * 3600 + timedelta.seconds

date1 = datetime.strptime('2003-11-30 01:00:00', '%Y-%m-%d %H:%M:%S')

date2 = datetime.now()
print("\n%d seconds" %(dateDifferenceInSeconds(date2, date1)))
print()
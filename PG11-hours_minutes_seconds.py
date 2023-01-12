#Python Gently Ex-11 Hours, Minutes, Seconds

def getHoursMinutesSeconds(totalSeconds):
    returnTime = ""
    hrs = 0
    mins = 0
    secs = 0

    if totalSeconds == 0:
        return "0s"
    if totalSeconds >= 3600:
        hrs = totalSeconds//3600

    mins = (totalSeconds - (3600 * hrs)) // 60
    secs = (totalSeconds - (3600 * hrs)) % 60

    if hrs > 0:
        returnTime = str(hrs) + "h "
    if mins > 0:
        returnTime = str(returnTime) + str(mins) + "m "
    if secs > 0:    
        returnTime = str(returnTime) + str(secs) + "s "

    return (returnTime.strip())
        

assert getHoursMinutesSeconds(30) == '30s'

assert getHoursMinutesSeconds(60) == '1m'

assert getHoursMinutesSeconds(90) == '1m 30s'

assert getHoursMinutesSeconds(3600) == '1h'

assert getHoursMinutesSeconds(3601) == '1h 1s'

assert getHoursMinutesSeconds(3661) == '1h 1m 1s'

assert getHoursMinutesSeconds(90042) == '25h 42s'

assert getHoursMinutesSeconds(0) == '0s'

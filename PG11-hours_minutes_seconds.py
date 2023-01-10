#Python Gently Ex-11 Hours, Minutes, Seconds


assert getHoursMinutesSeconds(30) == '30s'

assert getHoursMinutesSeconds(60) == '1m'

assert getHoursMinutesSeconds(90) == '1m 30s'

assert getHoursMinutesSeconds(3600) == '1h'

assert getHoursMinutesSeconds(3601) == '1h 1s'

assert getHoursMinutesSeconds(3661) == '1h 1m 1s'

assert getHoursMinutesSeconds(90042) == '25h 42s'

assert getHoursMinutesSeconds(0) == '0s'

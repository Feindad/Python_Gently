#Excercise 6 from Python Gently- Ordinal Suffix

ordSuf = { 0: 'th', 1: "st" , 2:"nd" , 3:"rd" , 4: "th" ,
           5: "th", 6: "th", 7: "th", 8:"th", 9 :"th", 11:"th",
           12: "th",13: "th"}


def ordinalSuffix(number):
    if number in ordSuf:
        return str(number) + str(ordSuf[number])
    else:
        lastdigit = str(number)[-1]
        return (str(number) + ordSuf[int(lastdigit)])


assert ordinalSuffix(0) == '0th'

assert ordinalSuffix(1) == '1st'

assert ordinalSuffix(2) == '2nd'

assert ordinalSuffix(3) == '3rd'

assert ordinalSuffix(4) == '4th'

assert ordinalSuffix(10) == '10th'

assert ordinalSuffix(11) == '11th'

assert ordinalSuffix(12) == '12th'

assert ordinalSuffix(13) == '13th'

assert ordinalSuffix(14) == '14th'

assert ordinalSuffix(101) == '101st'

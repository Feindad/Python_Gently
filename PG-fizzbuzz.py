#fizzbuzz Ex5 Python Gently

def fizzBuzz(n):
    for x in range(1,n+1):
        if x % 3 != 0 and x % 5 != 0:
            print(x, end =" ")
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz ", end ="")
        else:
            if x % 3 == 0:
                print("Fizz ", end ="")
            if x % 5 == 0:
                print("Buzz ", end ="")

            

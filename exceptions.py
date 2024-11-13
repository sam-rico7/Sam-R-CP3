#Exceptions are ways that we handle errors created by users in a way that it doesn't break the code.
#Zero division, file not found, value error, type error, index error

class NegativeNumberError(Exception):
    pass

while True:
    try:
        num = int(input("Tell me a number: "))
    except ValueError:
        print("That wasn't a whole number womp womp!")
        continue
    else:
        break

while True:
    try:
        numTwo = int(input("Tell me another number: "))
        if numTwo <= 0:
            raise NegativeNumberError("Can't be a negative number")
    except (ValueError, NegativeNumberError):
        print("That wasn't a whole number womp womp!")
        continue
    except NegativeNumberError as e:
        print(e)
    else:
        try:
            print(f"{str(num)} divided by {str(numTwo)} equals {num/numTwo}")
            break
        except ZeroDivisionError:
            print ("You can't divide by 0, try again")
            continue
#Finally happens at the end
    finally:
        pass



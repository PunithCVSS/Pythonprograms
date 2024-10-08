###<<<<EXCEPTIONHANDLING--PYTHON>>>>
print('Banking application')
try:
    name = input('Enter your name:')
    birth_year = int(input('Enter DOB year:'))
    age = 2024 - birth_year
    print(f'Welcome {name}.') 
    print('select required option:')
    print('1.Create account')
    print('2.Deposit money')
    print('3.Withdraw money')
    print('4.Display Balance')
    print('5.Close my account' )
    print('OK,select some option from above list')
    opti = int(input())
    if (opti == 1):
     print('account creation in progress')
     if age < 18:
      print(f'Hey {name} you are a minor so need guardian details')
     else:
      address = input('Enter address')   
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
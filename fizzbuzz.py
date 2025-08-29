def fizz_buzz(num):
    arr = []
    
    for i in range(1, num):
        if i % 3 == 0 and i % 5 == 0:
            arr.append("FizzBuzz")
        elif i % 3 == 0:
            arr.append("Fizz")
        elif i % 5 == 0:
            arr.append("Buzz")
        else:
            arr.append(i)
        
    return arr
        
print(fizz_buzz(32))



def fizz_buzz2(num):
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
            
fizz_buzz2(32)
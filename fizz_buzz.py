def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    if num % 3 == 0:
        print("Fizz")
    if num % 5 == 0:
        print("Buzz")
    else:
        print(num)


numbers = [3, 5, 300, 15, 50, 60, 65, 33, 150, 120, 100, 160, 75, 155]

for num in numbers:
    fizz_buzz(num)

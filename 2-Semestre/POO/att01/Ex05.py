num1=0
num2=1
print(f"Fib1: {num1}")
print(f"Fib2: {num2}")
for i in range(2,10):
    num3=num1+num2
    print(f"Fib{i+1}: {num3}")
    num1=num2
    num2=num3
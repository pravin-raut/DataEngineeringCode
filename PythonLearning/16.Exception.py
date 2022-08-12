
try:
    for i in [1,2]:
        print(i**2)
except Exception as e:
    print("Error")
    print(e)
else:
    print("Works well")
finally:
    print("Inside Final")
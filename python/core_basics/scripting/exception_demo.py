x = ""

while True:
    try:
        x = (input("Enter a number:"))
        y = int(x)
        print("You entered:" + str(x))
        break
    except ValueError:
        print(f"Okay {x} is not a number!!")
    except KeyboardInterrupt:
        print("Oh Dearie, you have to enter something :D")
    finally:
        print("Bye Bye")
else:
    print("I am here")
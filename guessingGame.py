myArray=int(input("Guess a number(between 1 and 9):"))
print(myArray)
if(myArray==5):
    print("Congratulations you won!!")
elif(myArray>5):
    print("guess a lower number")
else:
    print("guess a higher number")
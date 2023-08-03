# a program to calculate the square root

number = input ("give me N, I will give you the Radical (N): ")
number = float(number)

error = 0.01
#print (number)

guess = number / 2

interation = 0

while(abs(number-guess**2)> error ):
    interation = interation + 1
    print ("-> on interation", interation, "my guess is", guess)
    taghsim = number / guess
    guess = (taghsim + guess) / 2

print (" The square root of", number, "is", guess)
    

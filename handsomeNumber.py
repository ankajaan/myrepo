number = int(input("Enter the number "))
lastDigit = number%10
leftDigits = number//10
leftDigitsSum = 0
while leftDigits:
    leftDigitsSum += leftDigits%10
    leftDigits = leftDigits//10

if leftDigitsSum == lastDigit:
    print( str(number)+" is a handsome number.")
else:
    print(str(number)+"is not handsome number" %(number))

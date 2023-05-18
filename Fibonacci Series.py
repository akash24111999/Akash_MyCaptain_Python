# Fibonacci Series:

num = int(input ("Enter the number of terms to print in the Fibonacci series: "))  

f = 0  
s = 1  
count = 0  
  
if num <= 0:  
    print ("Please enter a positive number.")  
  
elif num == 1:  
    print (f"The Fibonacci sequence for the {num} term is {f}.")  

else:  
    print (f"The Fibonacci sequence for the {num} term is: ")  
    while count < num:  
        print(f)  
        n = f + s   
        f = s  
        s = n  
        count += 1

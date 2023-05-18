# Positive numbers:

start_num = int(input("Enter the starting range: "))
end_num = int(input("Enter the ending range: "))
  
for i in range(start_num,end_num+1):
    if i >= 0:
        print(i, end=" ")

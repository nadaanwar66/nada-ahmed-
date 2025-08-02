rows=int(input("Enter the number of rows:\n"))
for i in range(1,rows,+1):
    spaces=" "*(rows-i)
    stars="*"*(2*i-1)
    print(spaces+stars)
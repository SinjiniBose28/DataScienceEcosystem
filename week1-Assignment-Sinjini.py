   #TASK 1
#Lower Triangular Pattern 
def lower_triangular(n):
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()

lower_triangular(5)


print('\n')

#Upper Triangular Pattern
def upper_triangular(n):
    for i in range(n):
        for j in range(n):
            if j >= i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


upper_triangular(5)

print('\n')

#pyramid pattern

def pyramid(n):
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))

# Example usage:
pyramid(5)


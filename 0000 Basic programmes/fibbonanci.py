# Fibonacci Series
# the sum of two elements defines the next

a, b = 0, 1
while a< 100:
    import sys
    sys.stdout.write(str(a )+ " ")
    #print(a)
    a, b = b, a+b



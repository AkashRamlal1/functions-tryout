def tafel_function():
    nummer = int(input('kies een nummer'))
    for i in range(1,11,1):
        print(int(i) , "x" , int(nummer) , "=" ,(int(nummer) * int(i)))

tafel_function()
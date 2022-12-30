def fibonacci(n):
    # Taking 1st two fibonacci numbers as 0 and 1
    f=[0,1]

    for i in range(2,n+1):
        print('called funciton')
        f.append(f[i-1]+f[i-2])
    return f[n]






if __name__ == '__main__':
    n= 5

    print(fibonacci(n))

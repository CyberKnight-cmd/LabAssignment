def fibo(series: list, n:int):
    if n==0:
        return series[0]
    elif n<2:
        return series
    else:
        series.append(series[-1] + series[-2])
        return fibo(series,n-1)

print(fibo([0,1], int(input("Enter the number of terms : ")) - 1))
    
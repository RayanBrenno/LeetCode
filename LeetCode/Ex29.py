def divide(dividend, divisor):
    signDivisor  = 1 if divisor >0 else -1
    signDividend  = 1 if dividend >0 else -1
    quotient = int(abs(dividend) / abs(divisor))*signDivisor*signDividend
    
    if -2**31 <quotient < 2**31 - 1:
        return quotient
    else:
        return -2**31+1 if quotient < 0 else 2**31 - 1


dividend = 2147483648
divisor = -1
print(divide(dividend, divisor))


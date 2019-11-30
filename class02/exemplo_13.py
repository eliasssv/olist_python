import fibo as fib

fib.fib(1000)
fib.fib2(100)
print(fib.__name__)

from fibo import fib, fib2
fib(100)
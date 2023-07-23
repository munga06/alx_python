#!/usr/bin/env python3
def fibonacci_sequence(n):
    
        if n <= 0:
           return []
        elif n == 1:
            return [0]
        else:
          fib_list = [0, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
        return fib_list
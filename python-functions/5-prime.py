#!/usr/bin/env python3
if __name__ == '__main__':
   def is_prime(number):
     if number <= 1:
        return False
     for i in range(2, number):
        if number % i == 0:
            return False

     return True
#!/usr/bin/env python3
def is_prime(number):
<<<<<<< HEAD
     if number <= 1:
        return False
=======
    if number <= 1:
       return False
>>>>>>> 348820495847ce3ad9c1313364bff7e4481882da
     for i in range(2, number):
        if number % i == 0:
            return False

     return True

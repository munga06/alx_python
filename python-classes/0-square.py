#!/usr/bin/python3
""" Define a class Square """


class Square:
    """ Represent a class square """
    def __init__(self, size):
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def perimeter(self):
        return 4 * self.__size

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size
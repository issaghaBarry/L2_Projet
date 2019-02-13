#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
:mod: car module

:author: Lasnier Hugo Barry Issagha

:date: 
"""

class Car():
    """
    Cars are defined by a color, a direction, a x and y position, and their size
    
    :param color: the color of the car
    :type color: str
    :param direction: the direction of the Car
    :type direction: str
    :param x: the x position of the Car
    :type x: int
    :param y: the y position of the Car
    :type y: int
    :UC: 0 <= x < 6, 0 <= y < 6, color must be one caractere in "ABCDEFGHIJKOPQRXZ"
    """

    def __init__(self, color, direction, x, y):
        """
        Initialize a Car with color position,size,direction,x position and y position
        
        :param color: the color of the car
        :type color: str
        :param direction: the direction of the Car
        :type direction: str
        :param x: the x position of the Car
        :type x: int
        :param y: the y position of the Car
        :type y: int
        :UC: 0 <= x < 6, 0 <= y < 6, color must be one caractere in "ABCDEFGHIJKOPQRXZ"
        """
        try:
            assert color.upper() in list("ABCDEFGHIJKXZOQRP") and type(color) == str and type(direction) == str and type(x) == int and type(y) == int and direction.upper() in ['V','H']
            self.coord_is_valid(direction,x,y)
            self.__color = color.upper()
            self.__direction = direction.upper()
            self.__x = x
            self.__y = y
            if color in "ABCDEFGHIJKXZ":
                self.__size = 2
            else:
                self.__size = 3
            self.__coord = [[x,y]]
            if direction == "H":
                for i in range(1,self.__size):
                    self.__coord += [[x+i,y]]
            else:
                for i in range(1,self.__size):
                    self.__coord += [[x,y+i]]
        except AssertionError:
            raise ParamCarError('Wrong parameters for the car.')
    def coord_is_valid(self,direction,x,y):
        """
        Test if the Car is in the grid
        """
        if direction == 'H':
            assert 0 <= x <5 and 0<=y<6
        else:
            assert 0 <= x <6 and 0<=y<5
        
            
    def get_color(self):
        """
        return the color of the Car
        
        :rtype: str

        :UC: none
        """
        return self.__color

    def get_size(self):
        """
        return the size of the Car
        
        :rtype: int
        
        :UC: none
        """
        return self.__size

    def get_direction(self):
        """
        return the direction of the car
        
        :rtype: str
        
        :UC: none
        """
        return self.__direction

    def get_x(self):
        """
        return the x position of the car
        
        :rtype: int
        
        :UC: none
        """
        return self.__x

    def get_y(self):
        """
        return the y position of the car
        
        :rtype: int
        :UC: none
        
        """
        return self.__y

    def get_coord(self):
        """
        return the coordonates of all the cell occupied by the car
        
        :rtype: list
        
        :UC: none
        """
        return self.__coord
    
    def __eq__(self, other):
        """
        return True if self and other are equal False otherwise
        
        :other type: Car
        
        :rtype: bool
        
        :UC: none
        
        :Exemple:

        >>> r = Car('R', 'H', 0,2)
        >>> j = Car('J', 'H', 0,2)
        >>> r == j
        False
        >>> r = Car('J', 'H', 0,2)
        >>> r == j
        True
        """
        return self.__color == other.get_color() and self.__x == other.get_x() and self.__y == other.get_y()
    
    def move_car(self, direction):
        """
        move the car in the direction passed in parameters.
        
        The directions are U, D, L, R (for up, down, left and right).

        :param direction: string represent the direction to move
        
        :type direction: str
        
        :rtype: none
        """
        self.__coord  = []
        if self.__direction == 'H':
            if direction == 'L':
                self.__x -=1
            elif direction == 'R':
                self.__x += 1
            self.__coord = [[self.__x, self.__y]]
            for i in range(1,self.__size):
                self.__coord += [[self.__x+i,self.__y]]
        elif self.__direction == 'V':
            if direction == 'U':
                self.__y -=1
            elif direction == 'D':
                self.__y += 1
            self.__coord = [[self.__x, self.__y]]
            for i in range(1,self.__size):
                self.__coord += [[self.__x,self.__y+i]]
        
            
    
    def compare(self,other):
        """
        return 1 if self > other,-1 if self < other and 0 if self == other

        :param other: another car
        
        :type other: Car
        
        :rtype: int
        
        :UC: none
        
        :Example:
        
        >>> r = Car('R', 'H', 0,2)
        >>> j = Car('J', 'H', 0,2)
        >>> r.compare(j)
        1
        >>> j.compare(r)
        -1
        >>> r.compare(r)
        0
        """
        if self.__color < other.get_color():
            return -1
        elif self.__color > other.get_color():
            return 1
        else:
            return 0
            
    
    def is_over(self, other):
        """
        return True if self is over the other car
        
        :param other: a car
        
        :type other: Car
        
        :return type: booleen
        
        :UC: type(other) == car
        
        :Example:
        
        >>> r = Car('R', 'H', 0,2)
        >>> j = Car('J', 'H', 0,2)
        >>> r.is_over(j)
        True
        """
        for xy in self.__coord:
            if xy in other.get_coord():
                return True
        return False

    def __repr__(self):
        """
        represent a Car
        
        :return type: string
        
        :Example:
        
        >>> Car('R', 'H', 0,2)
        RH02
        """
        return "{}{}{}{}".format(self.get_color(),self.get_direction(),self.get_x(),self.get_y())

    def __hash__(self):
        """
        compute a number between 0 and 34 coresponding to the car position on the grid
        Here is the representation of the 36 positions:
        
            +--+--+--+--+--+--+
            |0 |1 |2 |3 |4 |5 |
            +--+--+--+--+--+--+
            |6 |7 |8 |9 |10|11|
            +--+--+--+--+--+--+
            |12|13|14|15|16|17|
            +--+--+--+--+--+--+
            |18|19|20|21|22|23|
            +--+--+--+--+--+--+
            |24|25|26|27|28|29|
            +--+--+--+--+--+--+
            |30|31|32|33|34|35|
            +--+--+--+--+--+--+
        the position number 35 on the grid cannot be obtained because the car would be out of the grid.
        
        :return type: int
        
        :Example:

        >>> hash(Car('A','V',0,0))
        0
        
        >>> hash(Car('A','V',1,1))
        7

        >>> hash(Car('A','H',4,5))
        34
        """
        return self.__x + self.__y*6

class ParamCarError(Exception):
    """
    Exception for the car parameters
    """
    def __init__(self,msg):
        self.message = msg
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()

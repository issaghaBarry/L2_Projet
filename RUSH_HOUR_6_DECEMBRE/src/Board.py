from Car import Car
import functools

"""
:mod: tray module

:author: Lasnier Hugo Barry Issagha

:date: 
"""
class Board():

    def __init__(self, configuration=[]):
        """
        Initialize the game board
        
        :param configuration: the game configuration
        :type configuration: a list of cars
        """    
        configuration.sort(key= functools.cmp_to_key(Car.compare),reverse = True)
        self.__configuration = configuration
        dict_index_of_Cars = {}
        for i in range(len(configuration)):
            dict_index_of_Cars[configuration[i].get_color()] = i
        self.__dict_index_of_Cars = dict_index_of_Cars
        
    def get_configuration(self):
        """
        return the configuration

        :rtype: str
        
        :UC: none
        """
        return self.__configuration

    def configuration_is_valid(self):
        """
        :return: True if the configuration is valid ,false otherwise
        
        :rtype: bool
        :UC: none
        :Example:
        
        >>> Board([Car("Z","H",1,2),Car('O','H',2,5)]).configuration_is_valid()
        True
        >>> Board([Car('O','H',2,5)]).configuration_is_valid()
        False
        >>> Board([Car("Z","H",1,3)]).configuration_is_valid()
        False
        >>> Board([Car("Z","H",1,2),Car('O','H',2,5),Car('X','H',2,5)]).configuration_is_valid()
        False
        """
        red_car_in_conf = False
        for i in range(len(self.__configuration)):
            car1 = self.__configuration[i]
            if car1.get_color() == 'Z':  #Test if the red car is well placed
                red_car_in_conf = True
                if car1.get_y() != 2:
                    return False
            for car2 in self.__configuration[i+1:]: #test if any car is over another Car
                if car1.is_over(car2):
                    return False
        return red_car_in_conf

    def add_Car(self,car):
        """
        add a car in the configuration

        :param car: a car
        :param type: Car
        
        :Example:
        
        >>> a = Board()
        >>> len(a.get_configuration())
        0
        >>> a.add_Car(Car('O','H',2,5))
        >>> len(a.get_configuration())
        1
        """
        self.__configuration +=[car]
        self.__configuration.sort(key= functools.cmp_to_key(Car.compare),reverse = True)

    def get_list_coord_occupied(self):
        """
        return the list of all the occupied coordonates
        
        :rtype: list
        :Exemple:
        
        >>> a = Board([Car("Z","H",1,2),Car('O','H',2,5)])
        >>> a.get_list_coord_occupied()
        [[1, 2], [2, 2], [2, 5], [3, 5], [4, 5]]
        """
        res = []
        for car in self.__configuration:
            res += car.get_coord()
        return res

    def get_dict_index_of_cars(self):
        """
        return the dictionary containing the cars as key and their index in the list __configuration as value
        
        :rtype: dict
        
        :Exemple:
        
        >>> a = Board([Car("Z","H",1,2),Car('O','H',2,5)])
        >>> d =a.get_dict_index_of_cars()
        >>> l = [[i,d[i]] for i in d]
        >>> l.sort()
        >>> l
        [['O', 1], ['Z', 0]]
        """
        return self.__dict_index_of_Cars

    def get_list_coord_with_color(self):
        """
        return a list of list representing the board as a grid
        
        :rtype: list
        :Exemple:
        
        >>> a = Board([Car("Z",'H',0,2),Car("O","V",2,0),Car("P","V",3,2), Car("I","V",5,2),Car("J","H",1,5),Car('K','H',3,5)])
        >>> a.get_list_coord_with_color()
        [['', '', 'O', '', '', ''], ['', '', 'O', '', '', ''], ['Z', 'Z', 'O', 'P', '', 'I'], ['', '', '', 'P', '', 'I'], ['', '', '', 'P', '', ''], ['', 'J', 'J', 'K', 'K', '']]
        
        """
        l = list(list('' for i in range(6)) for k in range(6))
        for car in self.__configuration:
            for coord in car.get_coord():
                x = coord[0]
                y = coord[1]
                l[y][x] = car.get_color()
        return l

    def get_list_of_movement(self):
        """
        return the list of all possibles movements
        
        :rtype: list
        :Exemple:
        
        >>> a = Board([Car("Z","H",1,2),Car('O','V',5,2)])
        >>> a.get_list_of_movement()
        ['ZR1', 'ZL1', 'OD1', 'OU1']
        """
        List_Coord_occupied = self.get_list_coord_occupied()
        l=[]
        for car in self.__configuration:
            x = car.get_x()
            y = car.get_y()
            if car.get_direction() == "H":
                if [x+car.get_size(),y] not in List_Coord_occupied and x+car.get_size() <6:
                    l+=['{}R1'.format(car.get_color())]
                if [x-1,y] not in List_Coord_occupied and x-1 >=0 :
                    l+=['{}L1'.format(car.get_color())]
            else:
                if [x,y+car.get_size()] not in List_Coord_occupied and y+car.get_size() < 6:
                    l+=['{}D1'.format(car.get_color())]
                if [x,y-1] not in List_Coord_occupied and y-1 >=0:
                    l+=['{}U1'.format(car.get_color())]
        return l


    
    def __eq__(self,other):
        """
        test recurentialy if 2 configuration are equal 
        
        :param other: an other Board
        :type other: Grid
        
        :Example:
        
        >>> a = Board([Car("Z",'H',0,2),Car("O","V",2,0),Car("P","V",3,2), Car("I","V",5,2),Car("J","H",1,5),Car('K','H',3,5)])
        >>> b = a.copy()
        >>> a == b
        True
        
        """
        config_other = other.get_configuration()
        if len(self.__configuration) == len(config_other):
            for i in range(len(self.__configuration)):
                if not self.__configuration[i] == config_other[i]:
                    return False
            return True 
        else:
            return False

    def draw(self):
        """
        draw the board

        :rtype: None
        
        :Example:
        
        >>> a = Board([Car("Z",'H',0,2),Car("O","V",2,0),Car("P","V",3,2), Car("I","V",5,2),Car("J","H",1,5),Car('K','H',3,5)])
        >>> a.draw()
        +--+--+--+--+--+--+
        |  |  |O |  |  |  |
        +--+--+--+--+--+--+
        |  |  |O |  |  |  |
        +--+--+--+--+--+--+
        |Z |Z |O |P |  |I |
        +--+--+--+--+--+--+
        |  |  |  |P |  |I |
        +--+--+--+--+--+--+
        |  |  |  |P |  |  |
        +--+--+--+--+--+--+
        |  |J |J |K |K |  |
        +--+--+--+--+--+--+
        """
        list_coord_with_color = self.get_list_coord_with_color()
        for i in range(6):
            print('+'+'--+'*6, end= '')
            print()
            print('|'+'{:^2}|{:^2}|{:^2}|{:^2}|{:^2}|{:^2}|'.format(*list_coord_with_color[i]), end = '')
            print()
        print('+'+'--+'*6, end= '')
        print()

    def is_final(self):
        """
        this fonction check if the configuration is final (Which mean that the red car can exit the board)

        :rtype: bool
        :UC: None
        :Example:
        
        >>> a = Board([Car("Z",'H',0,2),Car("O","V",2,0),Car("P","V",3,2), Car("I","V",5,2),Car("J","H",1,5),Car('K','H',3,5)])
        >>> a.is_final()
        False
        """
        list_coord_occupied = self.get_list_coord_occupied()
        x = self.__configuration[0].get_x()+2
        for i in range(x, 6):
            if [i,2] in list_coord_occupied:
                return False
        return True

    def copy(self):
        """
        Do a copy of self.

        :rtype: class Board.Bord
        :UC: None
        :Example:
        
        >>> a = Board([Car("Z",'H',0,2),Car("O","V",2,0),Car("P","V",3,2), Car("I","V",5,2),Car("J","H",1,5),Car('K','H',3,5)])
        >>> b = a.copy()
        >>> b.get_configuration()[b.get_dict_index_of_cars()['I']].move_car('D')
        >>> b.draw()
        +--+--+--+--+--+--+
        |  |  |O |  |  |  |
        +--+--+--+--+--+--+
        |  |  |O |  |  |  |
        +--+--+--+--+--+--+
        |Z |Z |O |P |  |  |
        +--+--+--+--+--+--+
        |  |  |  |P |  |I |
        +--+--+--+--+--+--+
        |  |  |  |P |  |I |
        +--+--+--+--+--+--+
        |  |J |J |K |K |  |
        +--+--+--+--+--+--+
        >>> a.draw()
        +--+--+--+--+--+--+
        |  |  |O |  |  |  |
        +--+--+--+--+--+--+
        |  |  |O |  |  |  |
        +--+--+--+--+--+--+
        |Z |Z |O |P |  |I |
        +--+--+--+--+--+--+
        |  |  |  |P |  |I |
        +--+--+--+--+--+--+
        |  |  |  |P |  |  |
        +--+--+--+--+--+--+
        |  |J |J |K |K |  |
        +--+--+--+--+--+--+
        """
        l = []
        for car in self.__configuration:
            new_car = Car(car.get_color(),car.get_direction(),car.get_x(),car.get_y())
            l.append(new_car)
        return Board(l)

    def get_new_board_after_movement(self,color,movement):
        """
        this fonction return a new board when you do a mouvement, in order to not modify self.

        :param color: name of care
        :param type: string
        :param movement: movement that car has to do
        :parm type: string in ['D'(Down), 'U'(Up), 'L'(Left), 'R'(Rigth)]
        :rtype: Class Board.Board
        :UC: movement in ['D', 'U', 'L', 'R'] and the car in the self
        :Exemple:
        
        >>> a = Board([Car("Z",'H',0,2),Car("O","V",2,0),Car("P","V",3,2), Car("I","V",5,2),Car("J","H",1,5),Car('K','H',3,5)])
        >>> b = a.get_new_board_after_movement('O', 'D')
        
        """
        newBoard = self.copy()
        newBoard.get_configuration()[newBoard.get_dict_index_of_cars()[color]].move_car(movement)
        return newBoard

    def __hash__(self):
        """
        return the decimal value of the binary string composed of each hash value of cars in binary.

        :rtype: int
        :UC: None
        :Exemple:

        >>> hash(Board([Car("Z",'H',0,2)]))
        12

        >>> hash(Car("Z",'H',0,2))
        12

        >>> hash(Car("O","V",2,0))
        2
        
        >>> a = Board([Car("Z",'H',0,2),Car("O","V",2,0)])
        >>> hash(a)
        770

        >>> 770 == 12<<6|2
        True
        
        >>> bin(770) == '0b1100000010'
        True
        
        >>> a = Board([Car("Z",'H',0,2),Car("O","V",2,0),Car("P","V",3,2), Car("I","V",5,2),Car("J","H",1,5),Car('K','H',3,5)])
        >>> hash(a)
        13137221585
        
        """
        res=0
        for car in self.__configuration:
            res = res<<6|hash(car)
        return res

    def get_last_movement_z(self):
        """
        return the last movement that z must do to exit when the configuration is final

        :rtype: str
        """
        x = self.__configuration[0].get_x()
        return 'ZR'+str(6-x)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

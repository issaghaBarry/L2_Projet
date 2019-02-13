from Board import Board
from Car import *
from queue import *
import pickle
import sys
import time

def resolve(Board,talkative=False):
    """
    resolve a board
    print more details if optional parameter is set to True.
    
    :param board: a Board object
    :type board: Board
    param talkative: (optional boolean) equals False by default.Print details of resolution if set to True
    return a list of movement that resolve the board
    rtype:list
    Exemple:
    >>> resolve(Board([Car("Z",'H',0,2),Car("O","V",2,0),Car("P","V",3,2), Car("I","V",5,2),Car("J","H",1,5),Car('K','H',3,5)]))
    ['OD2', 'KR1', 'PD1', 'JL1', 'OD1', 'ID1', 'ZR6']
    """
    begining_time = time.time()
    if not Board.configuration_is_valid():
        return 'UnvalidGrid'
    dictionary_of_Boards = dict()
    queue_Boards = Queue()
    queue_Boards.put(Board)
    Number_of_Board_explored = 0
    dictionary_of_Boards[Board]= []
    while  not queue_Boards.empty():
        This_Boards = queue_Boards.get()
        list_of_movements = This_Boards.get_list_of_movement()
        for movement in list_of_movements:
              Number_of_Board_explored +=1
              configuration = This_Boards.get_new_board_after_movement(movement[0],movement[1])
              if configuration.is_final():
                  if talkative:
                      number_of_steps = len(dictionary_of_Boards[This_Boards]+[movement])+int(configuration.get_last_movement_z()[2])
                      talk(Board,begining_time,time.time(),Number_of_Board_explored,len(dictionary_of_Boards),number_of_steps)
                  return simplify_list_of_mouvement(dictionary_of_Boards[This_Boards]+[movement]+[configuration.get_last_movement_z()])
                
              if  not configuration in dictionary_of_Boards :
                  dictionary_of_Boards[configuration] = dictionary_of_Boards[This_Boards]+[movement]
                  queue_Boards.put(configuration)
    
    if talkative:
        talk(Board,begining_time,time.time(),Number_of_Board_explored,len(dictionary_of_Boards))
    return None

def talk(board,begining_time,ending_time,Number_of_Board_explored,Number_different_Board,number_of_steps=-1):
    """
    print the Board, the time, the number of Boards tested and the number of differents Boards with layout
    
    :param board: a Board object
    :type: board: Board
    :param begining_time: the time when the resolution began.
    :type: begining_time: float
    :param Number_of_Board_explored: the number of all the boards that we test.
    :type: Number_of_Board_explored: int
    :param Number_different_Board: the number of all the differents boards that we test(no repetition).
    :type: Number_different_Board: int
    :param number_of_steps: the number of movement needed for the resolution of the grid
    :type number_of_steps: int

    :Example:
    >>> b = Board([Car("Z",'H',0,2),Car("O","V",2,0),Car("P","V",3,2), Car("I","V",5,2),Car("J","H",1,5),Car('K','H',3,5)])
    >>> talk(b,1512510138.8393276,1512510138.993419,1584,293,13)
    Board to resolve:
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
    <BLANKLINE>
    Time:  0.15409135818481445 
    <BLANKLINE>
    Number of Board_explored (including repetition):  1584 
    <BLANKLINE>
    Number of different Board explored (no repetition):  293 
    <BLANKLINE>
    number of steps :  13 
    <BLANKLINE>
    Solution: 
    """
    Total_time = ending_time-begining_time
    print("Board to resolve:")
    board.draw()
    print("\nTime: ",Total_time,"\n")
    print("Number of Board_explored (including repetition): ",Number_of_Board_explored,"\n")
    print("Number of different Board explored (no repetition): ",Number_different_Board,"\n")
    if number_of_steps != -1:
                           print("number of steps : ",number_of_steps,"\n")
    print("Solution: ")
        

def simplify_list_of_mouvement(list_mouvement):
    """
    return a simplified list_of_mouvement
    
    :param list_mouvement: a list of mouvement
    :list_mouvement: list
    :rtype: list

    :Examples:
    >>> simplify_list_of_mouvement(['OD1', 'OD1', 'KR1', 'PD1', 'JL1', 'OD1', 'ID1', 'ZR6'])
    ['OD2', 'KR1', 'PD1', 'JL1', 'OD1', 'ID1', 'ZR6']
    """
    res = []
    for i in list_mouvement:
        if res != [] and i[:2] == res[-1][:2]:
            res [-1] = res[-1][:2]+str(int(res[-1][2])+int(i[2]))
        else:
            res += [i]
    return res

def open_file(file):
    """
    return the content of the file f
    :param f: a filename
    :type f: str
    """
    entree = open(file, 'rb')
    return pickle.load(entree)

def usage():
    print("Usage: {:s} <filename>".format(sys.argv[0]))
    print("\t<filename>: filename for which we want to resolve a board")
    exit(1)

def main():
    try:
        talkative = False
        if len(sys.argv) == 3 and sys.argv[2] == '-talkative':
            talkative = True
        board_in_file = open_file(sys.argv[1])
        print(resolve(board_in_file,talkative))
    except ParamCarError:
        print('PCE')
    except:
        usage()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()


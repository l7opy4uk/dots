'''
TODO value check in install_dot
TODO same_dots list should to be relocated. to refresh correctly
make doc test
'''
import string
from generate_field import generate_field
from display_field import output_field

field = generate_field()


def make_dict():
    '''
    Create a dictionary with numerate letters.
    Using for translation letters into digits
    :return:
    '''
    key = list(string.ascii_uppercase)
    value = [i for i in range(0, 25)]
    dict = {}
    for i, j in zip(key, value):
        dict[i] = j
    return dict


def check_position(x, y):
    l = field
    if l[y][dict[x]] != 0:
        print("Position already occupied")


def check_around(y, x):
    '''
    Check position for similar marker in position around,
    if marker the same = append position to the same_dots list
    :param x:
    :param y:
    :return:
    '''
    list_yx = [[0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1]]
    marker = 1
    same_dots = []
    for i in list_yx:
        if field[y + i[0]][x + i[1]] == marker:
            same_dots.append([y + i[0], x + i[1]])
    return same_dots

def create_path(y, x):
    dot_alpha = [y, x]
    print(dot_alpha)
    dot_start = dot_alpha
    dot_next = []
    dots_around = check_around(y, x)
    print(dots_around)
    dots_path = []
    if dots_around != []:
        print("work!")
        while dot_alpha != dot_next:
            for i in dots_around:
                dot_next = [i[0], i[1]]
                print("dot next" + str(dot_next))
                dots_around = check_around(i[0], i[1])
                if dot_next != dot_start:
                    dot_start = dot_next
                    dots_path.append(dot_start)
                    #if dots_around == []:
                break

                  #  print(dots_around)
                  #  print(dots_path)
                  #  for i in dots_around:
                  #      dots_around = check_around(i[1], i[0])
                  #      dot_next = [i[0], i[1]]
                  #      print("part 2")
                  #      if dot_next != dot_start:
                  #          print("part 3")
                  #          dot_start = dot_next
                  #          dots_path.append(dot_start)
                  #          if dots_around == []:
                  #              break

                  #          print(dots_around)
                  #          print(dots_path)
        else:
            print("dots path" + str(dots_path))



def install_dot(marker):
    '''
    Check if position is free, if True:
        install dot in choosen position.
    :param marker: set a marker param you want to display
    :return:
    '''
    l = field
    dict = make_dict()
    while True:
        x, y = take_input()
        x = dict[x]
        if l[y][x] != 0:
            print("Position is already occupied")
            continue
        else:
            l[y][x] = marker
        create_path(y, x)
        return l


def take_input():
    '''
    Takes x and y params from user
    :return:
    '''
    input_y = int(input("y?")) - 1
    input_x = input("x?").upper()
    return input_x, input_y


field[2][1] = 1
field[3][1] = 1
field[1][2] = 1
print(output_field(field))
while True:
    output_field(install_dot(1))

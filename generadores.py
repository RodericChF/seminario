from typing import *

def squares():
    contador=1
    while True:
        yield contador*contador
        contador +=1

def first (n:int, it:Iterable):
    contador=0
    for elem in it:
        if contador<n:
            yield elem
            contador+=1
        else:
            break

def filter (cond, it:Iterable):
    for elem in it:
        if cond(elem)==True:
            yield elem

def take_while (cond, it:Iterable):
    for elem in it:
        if cond(elem)==False:
            break
        else:
            yield elem

if __name__=='__main__':
    print('--------PRIMER APARTADO--------')
    print('Los primeros 100 cuadrados perfectos')
    sq = squares()
    for i in range(100):
        print(next(sq))

    print('\n''--------SEGUNDO APARTADO-------')
    print('Los cuadrados perfectos menores que 100')

    for sqm100 in take_while(lambda n:n<100, squares()):
        print(sqm100)

    print('\n''--------TERCER APARTADO--------')
    print('Los primeros 20 cuadrados perfectos capicúa\n')

    def capicua (n:int):
        nString=str(n)
        for i in range(len(nString)//2):
            if(nString[i]!=nString[-i-1]):
                return False
        return True


    for elem in first(20, filter(lambda n: capicua(n)==True, squares())):
        print(elem)



    #A PARTIR DE AQUÍ ESTÁN LAS PRUEBAS

    # sq=squares()
    # for i in range (10):
    #     print(next(sq))
    #
    # print('\n''------------------------------''\n')
    #
    # for elem in first(20, range(50,200)):
    #     print(elem)
    #
    # print('\n''------------------------------''\n')
    #
    # for elem in first(100, [2,4,5,7,2]):
    #     print(elem)
    #
    # print('\n''------------------------------''\n')
    #
    # for elem in filter(lambda n:n<100, range(50,200)):
    #     print(elem)
    #
    # print('\n''------------------------------''\n')
    #
    # for elem in filter(lambda n:n%2==0, [2,4,5,7,2]):
    #     print(elem)
    #
    # print('\n''------------------------------''\n')
    #
    # for elem in take_while(lambda n: n<100, range(50,200)):
    #     print(elem)
    #
    # print('\n''------------------------------''\n')
    #
    # for elem in take_while(lambda n: n%2==0, [2,4,5,7,2]):
    #     print(elem)
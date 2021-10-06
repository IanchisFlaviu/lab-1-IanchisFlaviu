def prim(x):
    '''
    Determina daca un numar este prim sau nu
    Intput:un numar intreg dat de la tastatura
    Output:mesajul: numarul este prim sau nu
    '''
    ok = True
    if x<2:
        ok = False
    else:
        for i in range(2,x//2+1):
            if x%i==0:
                ok= False

    if ok == True:
        print('Numarul este prim')
    else:
        print('Numarul nu este prim')


def produs(n):
    '''
    Determina produsul a n numere naturale
    :param n: un numar natural
    :return: un numar natural
    '''
    p=1
    for i in range(n):
        x = int(input('Dati numarul '))
        p=p*x
    return p

def cmmdc1(a,b):
    '''
    Determina cel mai mare divizor comun a 2 numere
    :param a: un numar intreg
    :param b: un numar intreg
    :return: un numar intreg-cel mai mare divizor comun al numerelor a si b
    '''
    if a<0 :
        a = -a
    if b<0 :
        b = -b

    if a==b:
        return a
    elif a<b:
        b=b-a
    else:
        a=a-b
    return a

def cmmdc2(a,b):
    '''
    Determina cel mai mare divizor comun a 2 numere
    :param a: un numar intreg
    :param b: un numar intreg
    :return: un numar intreg-cel mai mare divizor comun al numerelor a si b
    '''
    if a < 0:
        a = -a
    if b < 0:
        b = -b

    while(b!=0):
        t = b
        b = a%b
        a = t

    return a

def test_cmmdc1():
    assert cmmdc1(12,36) == 12
    assert cmmdc1(8,40) == 8
    assert cmmdc1(15,45) == 15

def test_cmmdc2():
    assert cmmdc2(24,36) == 12
    assert cmmdc2(8,40) == 8
    assert cmmdc2(15,45) == 15


def print_menu():
    print('1.Determina daca un numar este sau nu prim')
    print('2.Produsul a n numere naturale')
    print('3.Cmmdc1 ')
    print('4.Cmmdc2 ')


def main():
    while True:
        print_menu()
        opt = int(input('Dati optiunea: '))
        if opt == 1:
            x = int(input('Dati numarul: '))
            prim(x)
        elif opt == 2:
            n = int(input('Dati numarul de numere '))
            print(produs(n))
        elif opt == 3:
            a = int(input('Dati numarul a: '))
            b = int(input('Dati numarul b: '))
            print(cmmdc1(a,b))
        elif opt == 4:
            a = int(input('Dati numarul a: '))
            b = int(input('Dati numarul b: '))
            print(cmmdc2(a,b))
        else:
            break


main()
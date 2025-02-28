import os
import platform

name = platform.system()
ver = '1.0.10.16'

def err(x):
    match x:
        case 0:
            print('\033[31mERR00:No matching commands.\033[0m')
            print('\033[34m***Insert \'help\' for help***\033[0m')
        case 1:
            print('\033[31mERR01:Not run as main.\033[0m') 
            print('\033[34m***Please do not import this program as a package***\033[0m') 
        case 2:
            print('\033[31mERR02:Not a number.\033[0m')
            print('\033[34m***Please check your input content***\033[0m') 
        case _:
            print('\033[31mERR__:Unknown error occured.\033[0m')
    del x
    return

def det1():
    print('You are calculating a 1 ordered determinant.')
    while True:
        print('Please insert your 1st line.')
        det1o = input('> ')
        try:
            det1o = float(det1o)
        except ValueError:
            err(2)
        else:
            break
    print(f'\n{det1o}\n')
    del det1o
    return

def det2():
    print('You are calculating a 2 ordered determinant.')
    while True:
        print('Please insert your 1st line.')
        det2o1 = input('> ')
        try:
            a1,b1 = map(float,det2o1.split()) 
        except ValueError:
            err(2)
        else:
            break
        finally:
            del det2o1
    while True:
        print('Please insert your 2nd line.')
        det2o2 = input('> ')
        try:
            a2,b2 = map(float,det2o2.split()) 
        except ValueError:
            err(2)
        else:
            break
        finally:
            del det2o2
    q = a1 * b2 - a2 * b1
    print(f'\n{q}\n')
    del a1
    del a2
    del b1
    del b2
    del q
    return

def det3():
    print('You are calculating a 3 ordered determinant.')
    while True:
        print('Please insert your 1st line.')
        det3o1 = input('> ')
        try:
            a1,b1,c1 = map(float,det3o1.split()) 
        except ValueError:
            err(2)
        else:
            break
        finally:
            del det3o1
    while True:
        print('Please insert your 2nd line.')
        det3o2 = input('> ')
        try:
            a2,b2,c2 = map(float,det3o2.split()) 
        except ValueError:
            err(2)
        else:
            break
        finally:
            del det3o2
    while True:
        print('Please insert your 3rd line.')
        det3o3 = input('> ')
        try:
            a3,b3,c3 = map(float,det3o3.split()) 
        except ValueError:
            err(2)
        else:
            break
        finally:
            del det3o3
    q = a1 * b2 * c3 + a2 * b3 * c1 + a3 * b1 * c2 - a1 * b3 * c2 - a2 * b1 * c3 - a3 * b2 * c1
    print(f'\n{q}\n')
    del a1,a2,a3,b1,b2,b3,c1,c2,c3,q
    return

def det4():
    print('You are calculating a 4 ordered determinant.')
    while True:
        print('Please insert your 1st line.')
        det4o1 = input('> ')
        try:
            a1,b1,c1,d1 = map(float,det4o1.split()) 
        except ValueError:
            err(2)
        else:
            break
        finally:
            del det4o1
    while True:
        print('Please insert your 2nd line.')
        det4o2 = input('> ')
        try:
            a2,b2,c2,d2 = map(float,det4o2.split()) 
        except ValueError:
            err(2)
        else:
            break
        finally:
            del det4o2
    while True:
        print('Please insert your 3rd line.')
        det4o3 = input('> ')
        try:
            a3,b3,c3,d3 = map(float,det4o3.split()) 
        except ValueError:
            err(2)
        else:
            break
        finally:
            del det4o3
    while True:
        print('Please insert your 4th line.')
        det4o4 = input('> ')
        try:
            a4,b4,c4,d4 = map(float,det4o4.split()) 
        except ValueError:
            err(2)
        else:
            break
        finally:
            del det4o4
    q = a1 * (b2 * c3 * d4 + c2 * d3 * b4 + d2 * b3 * c4 - d2 * c3 * b4 - c2 * b3 * d4 - b2 * d3 * c4) - a2 * (b1 * c3 * d4 + c1 * d3 * b4 + d1 * b3 * c4 - d1 * c3 * b4 - c1 * b3 * d4 - b1 * d3 * c4) + a3 * (b1 * c2 * d4 + c1 * d2 * b4 + d1 * b2 * c4 - d1 * c2 * b4 - c1 * b2 * d4 - b1 * d2 * c4) - a4 * (b1 * c2 * d3 + c1 * d2 * b3 + d1 * b2 * c3 - d1 * c2 * b3 - c1 * b2 * d3 - b1 * d2 * c3)
    print(f'\n{q}\n')
    del a1,a2,a3,a4,b1,b2,b3,b4,c1,c2,c3,c4,d1,d2,d3,d4,q
    return

def cal():
    print('\033[34mCalculate mode enabled.\033[0m')
    while True:
        formula = input('CAL> ')
        if formula == 'exit()' or formula == 'quit()' or formula == 'exit' or formula == 'quit' or formula =='e' or formula == 'q' or formula == 'E' or formula == 'Q':
            print('\033[34mCalculate mode disabled.\033[0m')
            return
        else:
            try:    
                formula = eval(formula)
            except:
                err(0)
            else:
                print(f'\n{formula}\n')
            finally:
                del formula

def helpdoc():
    print("""\033[34mhelp document:\033[0m

    \033[33m\'num\'\033[0m - /Calculate a \'num\' ordered determinant.
    \033[33minv\033[0m - /Calculate inversions.
    \033[33mcal\033[0m - /Regular calculations.
    \033[33mclear\033[0m - /Clear screen.
    \033[33mhelp\033[0m - /Help.
    \033[33mexit\033[0m - /Exit.

\033[34m***C style commands are also allowed, but not recommended***\033[0m
\033[34m***\'exit\' in calculate mode means to exit calculate mode and back to normal mode***\033[0m""")
    return

def clearScreen():
    if name == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    return

def inv():
    while True:
        inver = input('INV> ')
        try:
            int(inver)
        except:
            err(2)
        else:
            inver = list(inver)
            count = 0
            for i in range(0,len(inver)):
                for j in range(i+1,len(inver)):
                    if inver[i] > inver [j]:
                        count+=1
            print(f'\n{count}\n')
            del count
            break
        finally:
            del inver
    return
def main():
    clearScreen()
    print(f'DetCompy [version {ver}]')
    print('(c)harukaworks.link all rights reserved.\n')
    while True:
        case = input('> ')
        match case:
            case '1':
                try:
                    det1()
                except:
                    err(-1)
            case '2':
                try:
                    det2()
                except:
                    err(-1)
            case '3':
                try:
                    det3()
                except:
                    err(-1)
            case '4':
                try:
                    det4()
                except:
                    err(-1)
            case 'e' | 'E' | 'exit' | 'quit':
                del case
                print('\033[33mExiting...\033[0m')
                clearScreen()
                break
            case 'h' | 'H' | 'help' | '?' | '？':
                try:
                    helpdoc()
                except:
                    err(-1)
            case 'c' | 'C' | 'cls' | 'clear':
                try:
                    clearScreen()
                except:
                    err(-1)
            case 'cal' | 'f':
                try:
                    cal()
                except:
                    err(-1)
            case 'i' | 'I' | 'inv':
                try:
                    inv()
                except:
                    err(-1)
            case _:
                err(0)
        del case
    return

if __name__ == '__main__': 
    main()
else:
    err(1)

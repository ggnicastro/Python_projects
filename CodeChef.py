__author__ = 'kaihami'
#import psyco
#psyco.full()

def op_1(a):
    if a%2 == 0:
        Num = a/2
    if a%2 != 0:
        Num = (a-1)/2
    return Num

def op_2(b):
    Num = b*2
    return Num

def main():
    test = int (input())
    try:
        for i in xrange(test):
            A, B =  map(int, raw_input().split())
            a = int(A)
            b = int(B)

    except ValueError:
        for i in xrange(test):
            A = map(int, raw_input().split())
            a = int(A)
            b = int(A)
    x = 0

    P = False

    while not P:
        original = a

        if a > b:
            a = op_1(a)
            x+=1
            c2 = a
        if a <b:
            a = op_2(a)
            x+=1
            c3 = a
        if a > b:
            a = op_1(a)
            x+=1
            c4 = a
        try:
            if c1 == c3 or c2 == c4:
                a = original
                a = op_1(a)
                P2 = False
                x = 1
                while not P2:
                    if a <b:
                        a = op_2(a)
                        x+=1
                        c1 = a
                    if a > b:
                        a = op_1(a)
                        x+=1
                        c2 = a
                    if a == b:
                        P2 = True
                break
        except:
            pass
        if a == b:
            P = True

    print x
    return 0

if __name__ == "__main__":
    main()


def NomeCognome():
        return "Valerio Carnevale Baraglia 435492"

## PARTE PRIMA: ESERCIZI CON FOLD
##-------------------------------
def And(Ls):
        return Fold1(FAnd,True,Ls)
def Fold1(F, v, Ls):
        if Ls == []:
                return v
        else:
                return F(Ls[0], Fold1(F, v, Ls[1:]))
def FAnd(x,y):
        return bool(x*y)


def Or(Ls):
        return Fold2(FOr,False,Ls)
def Fold2(F, v, Ls):
        if Ls == []:
                return v
        else:
                return F(Ls[0], Fold2(F, v, Ls[1:]))
def FOr(x,y):
        return bool(x+y)


def Lenght(Ls):
        return Fold3(FLenght,0,Ls)
def Fold3(F, v, Ls):
        if Ls == []:
                return v
        else:
                return F(Ls[0], Fold3(F, v, Ls[1:]))
def FLenght(x,y):
        return (1+y)


def Reverse(Ls):
        return Fold4(FReverse, [], Ls)
def Fold4(F, v, Ls):
        if Ls == []:
                return v
        if len(Ls)==1:
                return Ls[0]
        else:
                return F(Ls[0],Fold4(F, v, Ls[1:]))
def FReverse(x,y):
        return [y,x]


def FoldFactorial(n):
        return Fold5(FFoldFactorial,1,n)
def Fold5(F, v, n):
        if n == 0:
                return v
        else:
                return F(n, Fold5(F, v, n-1))
def FFoldFactorial(x,y):
        return x*y


def SumLenght(Ls):
        return [Sum(Ls),Lenght(Ls)]
def Fold6(F, v, Ls):
        if Ls == []:
                return v
        else:
                return F(Ls[0], Fold6(F, v, Ls[1:]))
def FLenght(x,y):
        return (1+y)
def Lenght(Ls):
        return Fold6(FLenght,0,Ls)
def Sum(Ls):
        if Ls == []:
                return 0
        else:
                return Ls[0] + Sum(Ls[1:])
def Add(x,y):
        return x+y
def Sum(Ls):
        if Ls == []:
                return 0
        else:
                return Add(Ls[0], Sum(Ls[1:]))


def Map(F,Ls):
        return Fold7(FMap,[],Ls) 
def F(x):
        return x**2-1
def FMap(a,b):
        return [F(a)]+b
def Fold7(F1, v, Ls):
        if Ls == []:
                return v
        else:
                return FMap(Ls[0],Fold7(F1,v,Ls[1:]))


def Filter(P,Ls):
        return Fold8(FFilter,[],Ls)
def P(x):
        if x%2==0:
                return x
        else:
                return ""
def FFilter(a,b):
        if P(a)=="":
                return b
        else:
                return [P(a)]+b
def Fold8(F1, v, Ls):
        if Ls == []:
                return v
        else:
                return FFilter(Ls[0],Fold8(F1,v,Ls[1:]))


def FoldLeft(Ls):
        return Fold9(FFoldLeft,0,Ls)
def Fold9(F, v, Ls):
        if Ls == []:
                return v
        else:
                return F(Ls[-1],Fold9(F, v, Ls[0:-1]))
def FFoldLeft(x,y):
        return (y+x)

## PARTE SECONDA: LISTA INFINITA NUMERI PRIMI
##-------------------------------------------

def NumeriPrimi():
        def primo(n):
                if n>1:
                        if n==2:
                                return True
                        if n%2==0:
                                return False
                        for i in range(3,n,2):
                                if n%i==0: 
                                        return False
                        else:
                                return True
                else:
                        return False 
        i=2
        while True:
                if primo(i)==True:
                        yield i
                i=i+1
crivello = NumeriPrimi()
print([next(crivello) for _ in range(10)])


def Fibonacci():
        a=0
        b=1
        c=1
        while True:
                yield c
                a=b
                b=c
                c=a+b
cnt = Fibonacci()    
As=[next(cnt) for _ in range(10)]
As.reverse()
As.append(1)
As.append(0)
As.reverse()
print(As)


## PARTE TERZA: JULIA SET E FRATTALI
##----------------------------------

import matplotlib.pyplot as plt
import numpy as np
def JuliaSetRec(z, c, k, max_k=64):
        while k<max_k:
                if abs(z)<2:
                        return JuliaSetRec(z**2+c,c,k+1)
                else:
                        return k
        if abs(z)<2:
                return 0
def JuliaSet(z, c=-0.11-0.79j):
        return JuliaSetRec(z, c, 0)
def MakeImage(F, n, scale=0.01):
        data = [scale*i for i in range(-n,n+1)]
        return np.matrix([[F(complex(a, b)) for a in data] for b in data])
def DrawImage(F, n, scale=0.01):
        m = MakeImage(F, n, scale)
        plt.figure(figsize=(6,6))
        img = plt.imshow(m, extent=(-scale*n, scale*n, -scale*n, scale*n), cmap='hot')
        plt.colorbar()
        plt.show()


import matplotlib.pyplot as plt
import numpy as np
def MandelSet(n):
        return DrawImage1(n,scale=0.0075)
def H(c):
        if abs(c)>2:
                return 0
        else:
                z=0
                n=0
                for k in range(64):
                        z=z**2+c
                        n=n+1
                        if abs(z)>2:
                                k=64
                                return n
                if abs(z)<2:
                        return 0
def MakeImage1(n, scale=0.0075):
        data = [scale*i for i in range(-n,n+1)]
        return np.matrix([[H(complex(a, b)) for a in data] for b in data])
def DrawImage1(n, scale=0.0075):
        m = MakeImage1(n, scale)
        plt.figure(figsize=(6,6))
        img = plt.imshow(m, extent=(-scale*n,scale*n,-scale*n, scale*n), cmap='hot')
        plt.colorbar()
        plt.show()

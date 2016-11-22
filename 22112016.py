## EPN-ESFOT-ASI Programacion Avanzada 2016-B

## 22112016.py
## Versión: 1.0
## Sacar la area y volumenes de figuras geometricas

## Autor: Bryan España
## Autor de la Versión: Bryan España
## Fecha: 22-11-2016
import math

def triangulo(fig):
    print("\tMenu ",fig)
    print("1.Triángulo Equilátero")
    print("2.Triángulo Isósceles")
    print("3.Triángulo Escaleno")
    sel=input("Ingrese el numero de la opcion que deseea: ")
    if sel == '1':
        print("1.-Triángulo Equilátero")
        b=int(input("Ingrese ls medida de uno de los lados: "))
        h=math.sqrt(3*b)/2
        a=(math.sqrt(3)*b**2)/4
        p=(3*b)
        imprimir(a,p)
    elif sel == '2':
        print("2.-Triángulo Isósceles")
        b=int(input("Ingrese la base: "))
        l=int(input("Ingrese la medida de un lado: "))
        h=math.sqrt(l**2-(b**2/4))
        a=(b*math.sqrt(l**2-(b**2/4)))/2
        p=(2*l+b)
        imprimir(a,p)
    elif sel == '3':
        print("3.-Triángulo Escaleno")
        b=int(input("Ingrese la base: ")) 
        h=int(input("Ingrese la altura: "))
        l=int(input("Ingrese la medida de un lado: "))
        l2=int(input("Ingrese la medida de del otro lado: "))
        a=(b*h)/2
        p=(b+l+l2)
        imprimir(a,p)
    else:
        print("El numero no se encuentra en el rango del menu ")

def poligono(fig,lad):
    print("\t",fig)
    l=float(input("Ingrese la medida de un lado: "))
    apo=float(input("Ingrese el apotema: "))
    n=lad
    p=l*n
    a=(p*apo)/2
    imprimir(a,p)

def imprimir(a,p):
    print("El area de la figura es: ",a)
    print("El perimetro de la figura es: ",p)

def menu():
    print("\tMenu")
    print("3.-Tringulo")
    print("5.-Pentagono")
    print("7.-Heptagono")
    print("9.-Eneagono")

def main():
    res='si'
    while res[0] in ['s','S']:
        menu()
        sel=input("Ingrese el numero de la opcion que deseea: ")
        if sel == '3':
            triangulo("Triangulo")
        elif sel =='5':
            poligono("Pentagono",5)
        elif sel =='7':
            poligono("Heptagono",7)
        elif sel =='9':
            poligono("Eneagono",9)
        else:
             print("El numero no se encuentra en el rango del menu")
        res=input("Deseea calcular otra area y perimetro: ")
            
main()
	

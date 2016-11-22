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
    print("4.-Cuadrado")
    print("5.-Pentagono")
    print("6.-Hexagono")
    print("7.-Heptagono")
    print("8.-Octogono")
    print("9.-Eneagono")
    print("10.-Decagono")

def main():
    res='si'
    while res[0] in ['s','S']:
        menu()
        sel=input("Ingrese el numero de la opcion que deseea: ")
        if sel == '3':
            triangulo("Triangulo")
        elif sel == '4':
            print ("AREA Y PERIMETRO DEL CUADRADO")
            lado = float(input("Ingrese el lado del cuadrado: "))
            pericua = lado+lado+lado+lado
            areacua = lado*lado
            print ("El Area del Cuadrado es:\n")
            print (areacua)
            print ("\nEl perimetro del Cuadrado es: \n ")
            print (pericua)
        elif sel =='5':
            poligono("Pentagono",5)
        elif sel== '6':
            print ("AREA Y PERIMETRO DEL HEXAGONO\n")
            ladohexa = float(input("Ingrese el lado del Hexagono"))
            apotema = float (input("Ingrese la apotema del Hexagono"))
            perihexa = (6* ladohexa)
            areahexa= (perihexa*apotema)
            print ("El Area del Hexagono es:\n")
            print (areahexa)
            print ("\nEl perimetro del Hexagono es: \n ")
            print (perihexa)
        elif sel =='7':
            poligono("Heptagono",7)
        elif sel== '8':
            print ("AREA Y PERIMETRO DEL OCTOGONO\n")
            ladoct = float(input("Ingrese el lado del Octogono"))
            apotemaoct = float (input("Ingrese la apotema del Octogono"))
            periocto = (8*ladoct)
            areaocto= (periocto*apotemaoct)
            print ("El Area del Octogono es:\n")
            print (areaocto)
            print ("\nEl perimetro del Octogono es: \n ")
            print (periocto)
        elif sel =='9':
            poligono("Eneagono",9)
        elif sel== '10':
            print ("AREA Y PERIMETRO DEL DECAGONO\n")
            ladodeca = float(input("Ingrese el lado del Decagono"))
            apotemadeca = float (input("Ingrese la apotema del Decagono"))
            perideca = (10* ladodeca)
            areadeca= (perideca*apotemadeca)
            print ("El Area del Decagono es:\n")
            print (areadeca)
            print ("\nEl perimetro del Decagono es: \n ")
            print (perideca)
        else:
             print("El numero no se encuentra en el rango del menu")
        res=input("Deseea calcular otra area y perimetro: ")
            
main()

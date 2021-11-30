#a)

def main():
    cedula=input("Digite la cédula del cliente"+"\n")
    rol=input("Digite el rol del cliente"+"\n")
    codigoProducto=1
    subtotal=0
    while codigoProducto!=0000:
        codigoProducto=int(input("Digite código del producto    //  pulse 0000 para terminar compra"+"\n"))
        if(codigoProducto==0000):
            break
        else:
            cantidadProducto=int(input("Cuántas unidades va a llevar el cliente"+"\n"))
            precioProducto=int(input("Digite el precio del producto"+"\n"))
            subtotal=subtotal+(precioProducto*cantidadProducto)
    if(rol=="estudiante"):
        descuento=subtotal*0.5
        total=subtotal-descuento
    else:
        descuento=subtotal*0.2
        total=subtotal-descuento       
    print("El "+rol+" con cédula "+cedula+" ,debe pagar $"+str(total)+" por su compra")
    
main()

#b)

"""
1) Un error que identificamos durante la codificación, fue que no se estaba sumando el subtotal en cada producto, sino que solo sumaba el del producto final,
la solución que tomamos fue, que cada iteración se sumara el precio del producto por cantidad al subtotal

Otro error que podría suceder, es que el usuario termine la compra sin haber ingresado ningun producto, esto más que un error causaría tener una respuesta en 0,
lo que podríamos hacer es que el programa pida un producto como mínimo por cada compra

En cuanto a errores de lógica, como se esta trabajando con sumas, restas y multiplicaciones, el único sería que el descuento fuera mayor al subtotal, dando un valor
a pagar negativo, aunque esto no es posible, ya que se calcula el promedio en base al subtotal, entonces es proporcional a este
"""
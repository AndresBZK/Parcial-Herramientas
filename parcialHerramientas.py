def main():
    cedula=input("Digite la cédula del cliente"+"\n")
    rol=input("Digite el rol del cliente"+"\n")
    codigoProducto=1
    subtotal=0
    
    while codigoProducto != 0000:
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

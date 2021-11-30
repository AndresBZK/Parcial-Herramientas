# Parcial-Herramientas Computacionales
Repositorio creado exclusivamente para funcionar como documentación y archivo del código principal

* Documentacion del Repositorio
* Documentacion del Software
    - Problemática a solucionar
    - Código Principal
        + Entrada
        + Cálculo
        + Definición de Rol
        + Salida
 
## Documentación del repositorio

### Documentacion de Software

**_Problematica a solucionar_**

El problema se fundamenta principalmente en la búsqueda por tener una solución rápida ante el **registro de productos y la aplicación de descuentos** en los mismos dependiendo el rol del comprador dentro de la Universidad, además de poder ser complementado para que haga este registro y aplicación de descuento ah más de un producto, buscando lograr un resultado de acuerdo al código, precio y cantidad de productos con el respectivo descuento de manera _automática y optima_.

**_Código Principal_**

Se desarrolló un Software capaz de ciclar una cantidad de productos definidos por el usuario mediante los códigos de los mismos, para después ir calculando los precios y definir un total al final del ciclo, para después mediante el rol asignado por el usuario al principio del código, las condicionales determinen que descuento tiene y se hace la operación respectiva.

> **Entrada:** cedula=input("Digite la cédula del cliente"+"\n")
    rol=input("Digite el rol del cliente"+"\n")
    codigoProducto=1
    subtotal=0
    
    while codigoProducto != 0000:
        codigoProducto=int(input("Digite código del producto    //  pulse 0000 para terminar compra"+"\n"))
        if(codigoProducto==0000):
            break



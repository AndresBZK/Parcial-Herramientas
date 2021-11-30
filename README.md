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
    - Posibles problemas en presente o a futuro del código
 
## Documentación del repositorio

### Documentacion de Software

**_Problematica a solucionar_**

El problema se fundamenta principalmente en la búsqueda por tener una solución rápida ante el **registro de productos y la aplicación de descuentos** en los mismos dependiendo el rol del comprador dentro de la Universidad, además de poder ser complementado para que haga este registro y aplicación de descuento ah más de un producto, buscando lograr un resultado de acuerdo al código, precio y cantidad de productos con el respectivo descuento de manera _automática y optima_.

**_Código Principal_**

Se desarrolló un Software capaz de ciclar una cantidad de productos definidos por el usuario mediante los códigos de los mismos, para después ir calculando los precios y definir un total al final del ciclo, para después mediante el rol asignado por el usuario al principio del código, las condicionales determinen que descuento tiene y se hace la operación respectiva.

> **Entrada:**  Líneas del 1 al 13 en ParcialHerramientas.py

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

Encargada principalmente de tomar los datos dados por el usuario, entre estos está la cédula del cliente, su rol, y finalmente los códigos,precios y cantidades de los productos
a realizar. De no haber código o digitar el código "0000", el ciclo se rompe y dará como resultado la aplicación de la linea de Cálculo.

> **Cálculo:** Línea 14 en ParcialHerramientas.py

    subtotal=subtotal+(precioProducto*cantidadProducto)
    
Ejecuta los datos dados en el ciclo While de Entrada para ir facturando los diferentes precios y unidades que vayan siendo asignados por el usuario, cuando el ciclo quiebre debido al break en el Ciclo de Entrada, este dará como resultado el Total Final.

> **Definición de Roles:** Lineas del 15 al 20 en ParcialHerramientas.py

    if(rol=="estudiante"):
        descuento=subtotal*0.5
        total=subtotal-descuento
    else:
        descuento=subtotal*0.2
        total=subtotal-descuento       

Mediante condicionales, se lee el rol indicado por el usuario en la entrada, y dependiendo de este, se ejecuta una u otra operación hracias a las dos condicionales expuestas en 
el bloque de código presentado como _Definición de Roles_.

> **Salida:** Línea 21 en ParcialHerramientas.py

     print("El "+rol+" con cédula "+cedula+" ,debe pagar $"+str(total)+" por su compra")
     
Finalmente, se ejecuta un print que formaliza la respuesta donde con un mensaje organizado dará a conocer los datos del usuario para realizar la verificación de compra, junto
con el total de su compra, esta misma ya contaría con la aplicación del descuento.

**_Nota_**

Todos estos bloques fueron sacados del documento ParcialHerramientas.py, se encuentra en el repositorio.

### Problematicas a presentarse en el desarrollo del código

Posiblemente nos encontremos con ~~problemas~~ que queremos evitar en lo máximo posible, para este hemos creado un Documento Word donde podrá encontrar el Analisis y comentarios
frente este aspecto.

Lo podrá encontrar en el repositorio con el nombre de: _Punto B - Preguntas y respuestas al código_

Muchas gracias por tu atención y disfruta del repositorio.

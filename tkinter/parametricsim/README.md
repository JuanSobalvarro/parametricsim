version = 0.1.0
  - Esta version viene con las caracteristicas de graficar ecuaciones parametricas 
    a traves de coordenadas rectangulares o polares, puede graficarse tanto en forma de "area" o de trazado.
  - Tiene un bug en el que el trazo atraviesa la figura.
  - Todavía no se agrega ejes, ni como ajustar la exactitud.
  - Todavía no está implementado cuando hay indefiniciones matemáticas así que hay que tener cuidado con la sintax utilizada.
  - Solo puede utilizarse parametro t.
  - Problemas con el turtle, hay que darle dos veces al boton debido a Turtle.Terminator().

=====INSTRUCTIONS=====
  - Recomendado usar py2exe y transformar sim.py a un .exe.
  - Ejecutar el código desde sim.py.
  - Utilizar un formato parecido al de calculadora para las entradas, y utilizar el parametro t. 
    Ex:  13*cos(t)-(6*cos(2*t))+(3*sen(3*t)*cos(t))-(cos(4*t))+(t**2)
  - Los botones resultado corresponden cada uno a los parametros que tienen arriba.
  - Si sale Turtle.Terminator() solo hay que darle dos veces al boton para graficar(será arreglado).

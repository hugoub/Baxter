# TIC-TAC-TOE (Gato)

Baxter es capaz de jugar gato a través de dos usuarios conectados en la misma red.

# Instrucciones

## Instalación

Se debe copiar y pegar la carpeta baxter_gato preferentemente en la carpeta src del espacio de trabajo. 

## Montaje

1.  Al frente de Baxter se pone un tablero de gato con un tamaño aproximado a 38 x 38 cm. Frontal a  cada brazo se ubica una fila de piezas que corresponde a los círculos y a las cruces respectivamente. 

2.	Guardar posiciones iniciales: Ejecutar el **archivo configurador_gato.py**. Se mostrará las instrucciones en la pantalla. El programa pedirá llevar el gripper a la primera posición de la fila de las piezas y luego al centro de la esquina inferior derecha del tablero (visto desde la perspectiva de Baxter). Se pedirá realizar lo anterior una vez por cada brazo. Si la posición entregada no es correcta, se pedirá ingresarla nuevamente. Finalmente se genera un archivo llamado posiciones.py que contiene las posiciones iniciales. 

    Las posiciones deben ser copiadas del archivo **posiciones.py** y pegadas dentro del archivo **servidor_gato.py** en el constructor de la clase gato. En la parte que dice “Reemplazar aquí”.

    Importante: Se debe haber definido antes el tamaño del tablero y el largo de cada pieza (ver sección _otros_)

## Ejecución

1.	Se deben ejecutar tres terminales con una sesión de activa ROS. Cada terminal puede ser ejecutado en la misma o en diferentes computadoras.

2.	En el primer terminal se ejecuta el archivo **servidor_gato.py**. Se pide seleccionar si el jugador 1 o el jugador 2 inicial la partida. En el segundo terminal se debe ejecutar **jugador1.py**. En el tercer terminal se debe ejecutar **jugador2.py**.

3.	El jugador que inicia la partida debe ingresar la jugada. Las jugadas están numeradas del 1 al 9. Cada una de estas se destaca en la pantalla de Baxter.  

4.	Los jugadores van alternando sus jugadas hasta que se produzca un empate o haya un ganador.

## Otros
	
*	Cambiar tamaño del tablero: 

En el archivo **configurador_gato.py**, específicamente en el constructor de la clase configurador_gato, existe el objeto llamado self.caja generado a través de la clase tablero_gato. El primer y segundo valor corresponden en metros al alto y ancho respectivamente. El tercer y cuarto valor corresponden a la cantidad de separaciones. En este caso, como es un gato, tiene 3 separaciones en el largo y 3 separaciones en el ancho. 

* Cambiar largo de cada pieza: 

La piezas se ponen en fila frente a cada brazo. Cada una de estas piezas tienen un largo dentro de la fila. Este valor se cambiar en el archivo **configurador_gato.py**. En el constructor de la clase configurador_gato existe una variable que se llama self.separacion, esta se puede modificar con el valor correspondiente en metros.


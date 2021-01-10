R es un entorno y lenguaje de programación con un enfoque al análisis estadístico.
R nació como una reimplementación de software libre del lenguaje S, adicionado con soporte para ámbito estático.
Este lenguaje es unos de los mas utilizados en la investigacion cientifica ya que con sus diferentes bibliotecas puedes solucionar diferentes
problemas matematicos de analisis estadisticos , apoyando a los diferentes campos que lo utilizan como puede ser el de investigacion biomedica,
bioinformatica , matematicas financieras entre otros.

La instalacion del programa R (Lo utilize en windows) es bastante simple:

    Primero se tiene que entrar en la pagina https://www.r-project.org en la cual al lado izquierdo se te presenta una lista de diferentes opciones,
    en esta hay que apretar la palabra CRAN abajo de Download.

    Esta te llevara a la R Archive Network las cual te presentara las Redes de archivos utilizadas de R de los diferentes paises , se tiene que
    escoger la red mas cercana a ti en la cual escogi la de chile en el Departamento de Ciencias de la Computación de la Universidad de Chile.

    Con esto se nos descargara una intalacion de R , se clickea , se sigue los pasos y se instala.

Despues de esto instalaremos R Studio el cual es un entorno de desarrollo integrado para el lenguaje de programación R, dedicado a la computación estadística y gráficos.
presentando una interfaz mas limpia y facil de utilizar que R , siendo una buena plataforma para trabajar con R de manera facil y sin problemas.

    Para instalar R Studio se requiere tener R previamente (el cual fue explicado previamente) , al tener instalado R se descargara R Studio
    desde la pagina https://rstudio.com/products/rstudio/download/#download en la cual (por mi parte) se descargara la version de windows.

    Al descargarla se clickea la descarga se sigue los pasos simples y al terminar se puede utilizar R Studio sin ningun problema.

Al igual que muchos lenguajes de programacion R nos presenta las opciones de trabajar desde la consola directamente para hacer pruebas , y
tambien la opcion de hacer un codigo de extension .R para ejercicios mas complejos.









1. Ejemplo Trabajo con datos agrupados (Trabajo en consola)

R studio nos permite tener una lectura grandes cantidades de datos agrupados en poco tiempo , por ejemplo en R puedes hacer un calculo de
 la medición de la mediana, desviacion estandar, minimo y maximo de un dato agrupado de tamaño N. 

Crearemos el dato agrupado vector el cual se crea de la manera

    vector= c(1,4,6,8,9,3,2,5,7,8)

en el cual se crea un vector numerico con los numeros contenidos dentro del parentecis.

Al tener creado el vector numerico con R a este se le calcular la mediana ,desviacion estandar , minimo , maximo entre otros de manera
facil con los diferentes comandos que nos permite utilizar R , siendo asi estos se calculan de la manera:

    #media:
	    median(vector)
    #mediana:
	    mean(vector)
    #minimo:
	    min(vector)
    #maximo:
	    max(vector)

entregandonos directamente estos valores en la consola:

tambien nos permite calcular los cuartiles , la varianza y la desviacion del vector de esta forma:

    #cuartiles:
	    quantile(vector)
    #varianza:
	    var(vector)
    #desviacion estandar:
	    sd(vector)



2. Ejemplo de Muestra de Graficos (Comando plot)

La función plot en R permite crear un gráfico pasando dos vectores (de la misma longitud), un data frame, una matriz o incluso otros objetos.
dependiendo de su clase o tipo de los datos de entrada. Algunos ejemplos son del uso del comando plot son:

plot(x, y): Diagrama de dispersión de los vectores numéricos x e y
plot(factor): Gráfico de barras del factor
plot(factor, y): Diagrama de caja del vector numérico y los niveles del factor
plot(serie_temporal): Gráfico de una serie de tiempo (clase ts)
plot(data_frame): Gráfico de correlación de todas las columnas del data frame (más de dos columnas)
plot(fecha, y): Traza un vector basado en fechas
plot(función, inferior, superior):Traza la función entre el valor inferior y máximo especificado

Por ejemplo simularemos dos variables normales aleatorias llamadas x e y de la manera (Trabajo en consola):

	# Generamos datos de ejemplo 
	# Se crean 500 datos aleatorios
	x <- rnorm(500)
	y <- x + rnorm(500)

Al utilizar el comando plot de la forma:

     plot(x,y) 
se generara un grafico con el diagrama de dispersión de los vectores numéricos x e y al utilizar 

    plot(x, y, main = "Gráfico de dispersión")
se nos generara el mismo grafico pero con el titulo Grafico de dispersión.


Tambien el comando plot te permite cambiar el color de las variables , el nombre de los factores x e y , entre otras opciones para una presentacion
del grafico mas ordenada(Esto aplica para todos lo graficos).



R studio facilita el control de datos agrupados de grandes tamaños con una codificacion simple y limpia para los usuarios siendo una opcion bastante
buena para trabajos en ambitos matematicas , ademas de que R studio te permite (con sus librerias) trabajar con archivos de extencion csv , xls entre
otros , ayudando a abrirlos en esta plataforma y presentarlos de manera ordenada , ayudando en la manipulacion de estos datos y en los diferentes
calculos que se tengan que hacer en estos datos.

# Desafío 5 - Investigación PageRank


Bienvenido a Desafio 5. Este programa es una implementación de PageRank, generando el grafo o tomando unos ya generados. 

<br></br>

## _Instrucciones de uso_

Para utilizar nuestro programa, se necesita Python 3+, y los siguientes packetes.
* itertools
* random
* time
* matplotlib
* networkx

El programa consta de 4 archivos, que serán explicados.

### _1 - crear grafico.py_

Este archivo crea un archivo .txt con un grafo al azar para que lo pueda ejecutar.

Para correr el archivo, simplemente correr el comando `python "crear grafico.py" -f "file_name"` o `python "crear grafico.py" --input_file "file_name"` , donde file_name es la dirección donde se guardará el archivo, en caso de que no se especifique, el archivo por default sera `dataset/node.txt`.

Este archivo debe ser ejecutado para poder ejecutar los siguientes, a menos que ya se tenga un grafo con la misma estructura.


  <p align="center">
  <img  src="https://i.imgur.com/6KFrZru.png">
  
</p>
<p align="center">
  Fig 1.1 Esctructura del archivo de grafos.
</p>





### _2 - main.py_

Toma un archivo con un grafo y muestra en pantalla el Pagerank generado.

Para correr el archivo, simplemente correr el comando `python main.py -f "file_name"` o `python main.py --input_file "file_name"` , donde file_name es la dirección del archivo, en caso de que no se especifique, el archivo por default sera `dataset/node.txt`.



<center>


<p align="center">
  <img  src="https://i.imgur.com/Dc3AZt1.png">
  
</p>
<p align="center">
  Fig 1.2 Comando de ejecución de main.py
</p>

  
### _3 - grafico a png.py_

Toma un grafo creado y crea una imagen que muestra intuitivamente su Pagerank.
  
Para correr el archivo, simplemente correr el comando `python "grafico a png.py" -f "file_name"` o `python "grafico a png.py" --input_file "file_name"` , donde file_name es la dirección donde se guardará el archivo, en caso de que no se especifique, el archivo por default sera `dataset/node.txt`.
  
El .png creado será como el siguiente, el cual será guardado en la misma carpeta de ejecución como "grafico.png".

  <p align="center">
  <img  src="https://i.imgur.com/Z81OzTa.png">
  
</p>
<p align="center">
  Fig 1.3 Representación grafica del grafo de PageRank.
</p>

  
### _4 - estabilidad.py_
  
A partir de un grafo, muestra en pantalla como evoluciona el Pagerank en alcanzar su estabilidad.
  
Para correr el archivo, simplemente correr el comando `python estabilidad.py -f "file_name"` o `python estabilidad.py --input_file "file_name"` , donde file_name es la dirección donde se guardará el archivo, en caso de que no se especifique, el archivo por default sera `dataset/node.txt`.


  

  <p align="center">
  <img  src="https://i.imgur.com/hoOZc1w.png">
  
</p>
<p align="center">
  Fig 1.4 Representación grafica de la estabilidad de PageRank.
</p>

### _5 - node time.py_
  
Crea un gráfico simulando grafos cada vez más complejos y luego muestra cuánto tiempo se demora en computar su Pagerank.
  
Para correr el archivo, simplemente correr el comando `python "node time.py".
 
  <p align="center">
  <img  src="https://i.imgur.com/y1EYXn3.png">
  
</p>
<p align="center">
  Fig 1.5 Representación grafica de la estabilidad de PageRank.
</p>  
 
  
  

# _Coevaluación_

| Criterio | Descripción  |  Fabían Pizarro | Rafael Diaz  | Leandro Villalobos |
|---|---|---|---|---|
|A. Asistencia y puntualidad   | Asistió siempre a las reuniones de proyecto y fue puntual.  | 2 | 1  | 1  |
| B. Integración  |  Siempre escucha y comparte las ideas de sus compañeros e intenta integrarlas. Busca cómo mantener la unión en el grupo. |  2 |  -2 | -3  |
| C. Responsabilidad  | Siempre entrega su trabajo a tiempo y el grupo no tiene que modificar sus fechas o plazos.  | -3  |  1 |  1 |
|  D. Contribución |  Siempre ofrece ideas para realizar el trabajo y propone sugerencias para su mejora. Se esfuerza para alcanzar los objetivos del grupo. |  -3 |1   | 3  |
|  E. Resolución de conflictos | En situaciones de desacuerdo o conflicto, siempre escucha otras opiniones y acepta sugerencias. Siempre propone alternativas para el consenso o la solución.  |  2 |  -1 | -2  |

## _Retroalimentación de compañeros_

| | Fabían Pizarro | Rafael Diaz  | Leandro Villalobos | 
|---|---|---|---|
| Fabían Pizarro | | + Disponible a toda hora <br></br> - Cuando le emociona una idea, la sigue ciegamente sin flexibilidad  |  + Buena disposición <br></br> - Dificultad de para comunicar idedas|
| Rafael Diaz  | + Trabaja muy duro y de manera eficiente <br></br> - Dificultad de comunicación para coordinarse con sus compañeros | | + Involucrado en la investigación y desarrollo del trabajo <br></br> - Dificultad de comunicación|
| Leandro Villalobos | + Liderazgo del grupo. <br></br> - A veces avanza sin previo aviso. | + Disponibilidad y comunicación. <br></br> - Sintaxis de pseudo codigo. | |

<br></br>


## _Link de la presentación_

[Presentación en Google Docs.](https://docs.google.com/presentation/d/1bWB1WOoF2aFlIQS1ReCPWts8gtawLPYGU5zp6Y3nV54/edit#slide=id.p)

[![Desafío 5:
Investigación PageRank
](https://i.imgur.com/I12KXYf.png)](https://docs.google.com/presentation/d/1bWB1WOoF2aFlIQS1ReCPWts8gtawLPYGU5zp6Y3nV54/edit#slide=id.p "Desafío 5:
Investigación PageRank
")

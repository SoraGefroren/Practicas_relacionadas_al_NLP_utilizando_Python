### Requisitos

<div align="justify">
Tener instalado Python 2.7 (o mayores) o Python 3
</div>

### Proceso de instalación

<ol>
    <li><div align="justify">Descargar los archivos de esta carpeta.
    </div></li>
    <li><div align="justify">Instalar las librerías de python <strong>"random"</strong> y <strong>"json"</strong>.
    </div></li>
    <li><div align="justify">Ejecutar el archivo <strong>".py"</strong>, de la siguiente manera:
        <ul>
            <li><div align="justify">"terminal&gt; Python nombreDelArchivo.py númeroDeAgentes númeroDeObjetos númeroDeIteraciones"
            </div></li>
        </ul>
    </div></li>
</ol>

### Descripción

<div align="justify">
Este ejercicio corresponde a un juego de nombres, el cual, consiste en lograr que una lista de agentes adquiera un mismo conocimiento, sobre las relaciones <strong>NOMBRE - OBJETO</strong>, que existen en una lista de objetos y nombres generados al azar.
</div>

### Resultados

<div align="justify">
El archivo <strong>".py"</strong>, de la presente práctica, se ejecutó de la siguiente forma:
</div>

 - términal$ <strong>p2Ejercicio4.py</strong> <strong>14</strong> <strong>7</strong> <strong>1000</strong>

<div align="justify">
Obteniendo así, el siguiente resultado:
</div>

 - <strong>Primeras "10" iteraciones (de la iteración 0 hasta la 9):</strong>

***Iteración "0"***
1. Resultado de enunciar
  - [Termina revisión de objeto "teqodolusi": Fallo]
2. Estado de los agentes
3. Número total de nombres conocidos: "1"
4. El número total de nombres para cada objeto es de...
  - Para el objeto "kabe" existen "0" nombres
  - Para el objeto "ze" existen "0" nombres
  - Para el objeto "beñibevuti" existen "0" nombres
  - Para el objeto "deca" existen "0" nombres
  - Para el objeto "jo" existen "0" nombres
  - Para el objeto "giyufuveposu" existen "0" nombres
  - Para el objeto "teqodolusi" existen "1" nombres
5. La longitud promedio de todos los nombres es de: "8"

```json
{
    "kabe": [], 
    "ze": [], 
    "be\u00f1ibevuti": [], 
    "deca": [], 
    "jo": [], 
    "giyufuveposu": [], 
    "teqodolusi": [
        "digesuto"
    ]
}
```

***Iteración "1"***
1. Resultado de enunciar
  - [Termina revisión de objeto "giyufuveposu": Fallo]
2. Estado de los agentes
3. Número total de nombres conocidos: "2"
4. El número total de nombres para cada objeto es de...
  - Para el objeto "kabe" existen "0" nombres
  - Para el objeto "ze" existen "0" nombres
  - Para el objeto "beñibevuti" existen "0" nombres
  - Para el objeto "deca" existen "0" nombres
  - Para el objeto "jo" existen "0" nombres
  - Para el objeto "giyufuveposu" existen "1" nombres
  - Para el objeto "teqodolusi" existen "1" nombres
5. La longitud promedio de todos los nombres es de: "6"

```json
{
    "kabe": [], 
    "ze": [], 
    "be\u00f1ibevuti": [], 
    "deca": [], 
    "jo": [], 
    "giyufuveposu": [
        "xuri"
    ], 
    "teqodolusi": [
        "digesuto"
    ]
}
```

***Iteración "2"***
1. Resultado de enunciar
  - [Termina revisión de objeto "jo": Fallo]
2. Estado de los agentes
3. Número total de nombres conocidos: "3"
4. El número total de nombres para cada objeto es de...
  - Para el objeto "kabe" existen "0" nombres
  - Para el objeto "ze" existen "0" nombres
  - Para el objeto "beñibevuti" existen "0" nombres
  - Para el objeto "deca" existen "0" nombres
  - Para el objeto "jo" existen "1" nombres
  - Para el objeto "giyufuveposu" existen "1" nombres
  - Para el objeto "teqodolusi" existen "1" nombres
5. La longitud promedio de todos los nombres es de: "8"

```json
{
    "kabe": [], 
    "ze": [], 
    "be\u00f1ibevuti": [], 
    "deca": [], 
    "jo": [
        "dirofuqijiqavo"
    ], 
    "giyufuveposu": [
        "xuri"
    ], 
    "teqodolusi": [
        "digesuto"
    ]
}
```

***Iteración "3"***
1. Resultado de enunciar
  - [Termina revisión de objeto "deca": Fallo]
2. Estado de los agentes
3. Número total de nombres conocidos: "4"
4. El número total de nombres para cada objeto es de...
  - Para el objeto "kabe" existen "0" nombres
  - Para el objeto "ze" existen "0" nombres
  - Para el objeto "beñibevuti" existen "0" nombres
  - Para el objeto "deca" existen "1" nombres
  - Para el objeto "jo" existen "1" nombres
  - Para el objeto "giyufuveposu" existen "1" nombres
  - Para el objeto "teqodolusi" existen "1" nombres
5. La longitud promedio de todos los nombres es de: "9"

```json
{
    "kabe": [], 
    "ze": [], 
    "be\u00f1ibevuti": [], 
    "deca": [
        "japamapo\u00f1o"
    ], 
    "jo": [
        "dirofuqijiqavo"
    ], 
    "giyufuveposu": [
        "xuri"
    ], 
    "teqodolusi": [
        "digesuto"
    ]
}
```

***Iteración "4"***
1. Resultado de enunciar
  - [Termina revisión de objeto "deca": Fallo]
2. Estado de los agentes
3. Número total de nombres conocidos: "4"
4. El número total de nombres para cada objeto es de...
  - Para el objeto "kabe" existen "0" nombres
  - Para el objeto "ze" existen "0" nombres
  - Para el objeto "beñibevuti" existen "0" nombres
  - Para el objeto "deca" existen "1" nombres
  - Para el objeto "jo" existen "1" nombres
  - Para el objeto "giyufuveposu" existen "1" nombres
  - Para el objeto "teqodolusi" existen "1" nombres
5. La longitud promedio de todos los nombres es de: "9"

```json
{
    "kabe": [], 
    "ze": [], 
    "be\u00f1ibevuti": [], 
    "deca": [
        "japamapo\u00f1o"
    ], 
    "jo": [
        "dirofuqijiqavo"
    ], 
    "giyufuveposu": [
        "xuri"
    ], 
    "teqodolusi": [
        "digesuto"
    ]
}
```

***Iteración "5"***
1. Resultado de enunciar
  - [Termina revisión de objeto "teqodolusi": Fallo]
2. Estado de los agentes
3. Número total de nombres conocidos: "5"
4. El número total de nombres para cada objeto es de...
  - Para el objeto "kabe" existen "0" nombres
  - Para el objeto "ze" existen "0" nombres
  - Para el objeto "beñibevuti" existen "0" nombres
  - Para el objeto "deca" existen "1" nombres
  - Para el objeto "jo" existen "1" nombres
  - Para el objeto "giyufuveposu" existen "1" nombres
  - Para el objeto "teqodolusi" existen "2" nombres
5. La longitud promedio de todos los nombres es de: "9"

```json
{
    "kabe": [], 
    "ze": [], 
    "be\u00f1ibevuti": [], 
    "deca": [
        "japamapo\u00f1o"
    ], 
    "jo": [
        "dirofuqijiqavo"
    ], 
    "giyufuveposu": [
        "xuri"
    ], 
    "teqodolusi": [
        "badavede", 
        "digesuto"
    ]
}
```

***Iteración "6"***
1. Resultado de enunciar
  - [Termina revisión de objeto "teqodolusi": Fallo]
2. Estado de los agentes
3. Número total de nombres conocidos: "6"
4. El número total de nombres para cada objeto es de...
  - Para el objeto "kabe" existen "0" nombres
  - Para el objeto "ze" existen "0" nombres
  - Para el objeto "beñibevuti" existen "0" nombres
  - Para el objeto "deca" existen "1" nombres
  - Para el objeto "jo" existen "1" nombres
  - Para el objeto "giyufuveposu" existen "1" nombres
  - Para el objeto "teqodolusi" existen "3" nombres
5. La longitud promedio de todos los nombres es de: "8"

```json
{
    "kabe": [], 
    "ze": [], 
    "be\u00f1ibevuti": [], 
    "deca": [
        "japamapo\u00f1o"
    ], 
    "jo": [
        "dirofuqijiqavo"
    ], 
    "giyufuveposu": [
        "xuri"
    ], 
    "teqodolusi": [
        "pipewiwi", 
        "badavede", 
        "digesuto"
    ]
}
```

***Iteración "7"***
1. Resultado de enunciar
  - [Termina revisión de objeto "kabe": Fallo]
2. Estado de los agentes
3. Número total de nombres conocidos: "7"
4. El número total de nombres para cada objeto es de...
  - Para el objeto "kabe" existen "1" nombres
  - Para el objeto "ze" existen "0" nombres
  - Para el objeto "beñibevuti" existen "0" nombres
  - Para el objeto "deca" existen "1" nombres
  - Para el objeto "jo" existen "1" nombres
  - Para el objeto "giyufuveposu" existen "1" nombres
  - Para el objeto "teqodolusi" existen "3" nombres
5. La longitud promedio de todos los nombres es de: "9"

```json
{
    "kabe": [
        "jovojaruzage\u00f1i"
    ], 
    "ze": [], 
    "be\u00f1ibevuti": [], 
    "deca": [
        "japamapo\u00f1o"
    ], 
    "jo": [
        "dirofuqijiqavo"
    ], 
    "giyufuveposu": [
        "xuri"
    ], 
    "teqodolusi": [
        "pipewiwi", 
        "badavede", 
        "digesuto"
    ]
}
```

***Iteración "8"***
1. Resultado de enunciar
  - [Termina revisión de objeto "teqodolusi": Fallo]
2. Estado de los agentes
3. Número total de nombres conocidos: "7"
4. El número total de nombres para cada objeto es de...
  - Para el objeto "kabe" existen "1" nombres
  - Para el objeto "ze" existen "0" nombres
  - Para el objeto "beñibevuti" existen "0" nombres
  - Para el objeto "deca" existen "1" nombres
  - Para el objeto "jo" existen "1" nombres
  - Para el objeto "giyufuveposu" existen "1" nombres
  - Para el objeto "teqodolusi" existen "3" nombres
5. La longitud promedio de todos los nombres es de: "9"

```json
{
    "kabe": [
        "jovojaruzage\u00f1i"
    ], 
    "ze": [], 
    "be\u00f1ibevuti": [], 
    "deca": [
        "japamapo\u00f1o"
    ], 
    "jo": [
        "dirofuqijiqavo"
    ], 
    "giyufuveposu": [
        "xuri"
    ], 
    "teqodolusi": [
        "pipewiwi", 
        "badavede", 
        "digesuto"
    ]
}
```

***Iteración "9"***
1. Resultado de enunciar
  - [Termina revisión de objeto "beñibevuti": Fallo]
2. Estado de los agentes
3. Número total de nombres conocidos: "8"
4. El número total de nombres para cada objeto es de...
  - Para el objeto "kabe" existen "1" nombres
  - Para el objeto "ze" existen "0" nombres
  - Para el objeto "beñibevuti" existen "1" nombres
  - Para el objeto "deca" existen "1" nombres
  - Para el objeto "jo" existen "1" nombres
  - Para el objeto "giyufuveposu" existen "1" nombres
  - Para el objeto "teqodolusi" existen "3" nombres
5. La longitud promedio de todos los nombres es de: "9"

```json
{
    "kabe": [
        "jovojaruzage\u00f1i"
    ], 
    "ze": [], 
    "be\u00f1ibevuti": [
        "fi\u00f1ane"
    ], 
    "deca": [
        "japamapo\u00f1o"
    ], 
    "jo": [
        "dirofuqijiqavo"
    ], 
    "giyufuveposu": [
        "xuri"
    ], 
    "teqodolusi": [
        "pipewiwi", 
        "badavede", 
        "digesuto"
    ]
}
```

</br>
</br>

 - <strong>Últimas "5" iteraciones (desde la iteración 994 hasta la 999):</strong>

***Iteración "994"***
1. Resultado de enunciar
  - [Termina revisión de objeto "jo": Exito]
2. Estado de los agentes
3. Número total de nombres conocidos: "7"
4. El número total de nombres para cada objeto es de...
  - Para el objeto "kabe" existen "1" nombres
  - Para el objeto "ze" existen "1" nombres
  - Para el objeto "beñibevuti" existen "1" nombres
  - Para el objeto "deca" existen "1" nombres
  - Para el objeto "jo" existen "1" nombres
  - Para el objeto "giyufuveposu" existen "1" nombres
  - Para el objeto "teqodolusi" existen "1" nombres
5. La longitud promedio de todos los nombres es de: "5"

```json
{
    "kabe": [
        "\u00f1ibiyozida"
    ], 
    "ze": [
        "jo"
    ], 
    "be\u00f1ibevuti": [
        "jihunu"
    ], 
    "deca": [
        "re"
    ], 
    "jo": [
        "\u00f1edunozi"
    ], 
    "giyufuveposu": [
        "do"
    ], 
    "teqodolusi": [
        "kuhudo"
    ]
}
```

***Iteración "995"***
1. Resultado de enunciar
  - [Termina revisión de objeto "beñibevuti": Exito]
2. Estado de los agentes
3. Número total de nombres conocidos: "7"
4. El número total de nombres para cada objeto es de...
  - Para el objeto "kabe" existen "1" nombres
  - Para el objeto "ze" existen "1" nombres
  - Para el objeto "beñibevuti" existen "1" nombres
  - Para el objeto "deca" existen "1" nombres
  - Para el objeto "jo" existen "1" nombres
  - Para el objeto "giyufuveposu" existen "1" nombres
  - Para el objeto "teqodolusi" existen "1" nombres
5. La longitud promedio de todos los nombres es de: "5"

```json
{
    "kabe": [
        "\u00f1ibiyozida"
    ], 
    "ze": [
        "jo"
    ], 
    "be\u00f1ibevuti": [
        "jihunu"
    ], 
    "deca": [
        "re"
    ], 
    "jo": [
        "\u00f1edunozi"
    ], 
    "giyufuveposu": [
        "do"
    ], 
    "teqodolusi": [
        "kuhudo"
    ]
}
```

***Iteración "996"***
1. Resultado de enunciar
  - [Termina revisión de objeto "giyufuveposu": Exito]
2. Estado de los agentes
3. Número total de nombres conocidos: "7"
4. El número total de nombres para cada objeto es de...
  - Para el objeto "kabe" existen "1" nombres
  - Para el objeto "ze" existen "1" nombres
  - Para el objeto "beñibevuti" existen "1" nombres
  - Para el objeto "deca" existen "1" nombres
  - Para el objeto "jo" existen "1" nombres
  - Para el objeto "giyufuveposu" existen "1" nombres
  - Para el objeto "teqodolusi" existen "1" nombres
5. La longitud promedio de todos los nombres es de: "5"

```json
{
    "kabe": [
        "\u00f1ibiyozida"
    ], 
    "ze": [
        "jo"
    ], 
    "be\u00f1ibevuti": [
        "jihunu"
    ], 
    "deca": [
        "re"
    ], 
    "jo": [
        "\u00f1edunozi"
    ], 
    "giyufuveposu": [
        "do"
    ], 
    "teqodolusi": [
        "kuhudo"
    ]
}
```

***Iteración "997"***
1. Resultado de enunciar
  - [Termina revisión de objeto "giyufuveposu": Exito]
2. Estado de los agentes
3. Número total de nombres conocidos: "7"
4. El número total de nombres para cada objeto es de...
  - Para el objeto "kabe" existen "1" nombres
  - Para el objeto "ze" existen "1" nombres
  - Para el objeto "beñibevuti" existen "1" nombres
  - Para el objeto "deca" existen "1" nombres
  - Para el objeto "jo" existen "1" nombres
  - Para el objeto "giyufuveposu" existen "1" nombres
  - Para el objeto "teqodolusi" existen "1" nombres
5. La longitud promedio de todos los nombres es de: "5"

```json
{
    "kabe": [
        "\u00f1ibiyozida"
    ], 
    "ze": [
        "jo"
    ], 
    "be\u00f1ibevuti": [
        "jihunu"
    ], 
    "deca": [
        "re"
    ], 
    "jo": [
        "\u00f1edunozi"
    ], 
    "giyufuveposu": [
        "do"
    ], 
    "teqodolusi": [
        "kuhudo"
    ]
}
```

***Iteración "998"***
1. Resultado de enunciar
  - [Termina revisión de objeto "kabe": Exito]
2. Estado de los agentes
3. Número total de nombres conocidos: "7"
4. El número total de nombres para cada objeto es de...
  - Para el objeto "kabe" existen "1" nombres
  - Para el objeto "ze" existen "1" nombres
  - Para el objeto "beñibevuti" existen "1" nombres
  - Para el objeto "deca" existen "1" nombres
  - Para el objeto "jo" existen "1" nombres
  - Para el objeto "giyufuveposu" existen "1" nombres
  - Para el objeto "teqodolusi" existen "1" nombres
5. La longitud promedio de todos los nombres es de: "5"

```json
{
    "kabe": [
        "\u00f1ibiyozida"
    ], 
    "ze": [
        "jo"
    ], 
    "be\u00f1ibevuti": [
        "jihunu"
    ], 
    "deca": [
        "re"
    ], 
    "jo": [
        "\u00f1edunozi"
    ], 
    "giyufuveposu": [
        "do"
    ], 
    "teqodolusi": [
        "kuhudo"
    ]
}
```

***Iteración "999"***
1. Resultado de enunciar
  - [Termina revisión de objeto "beñibevuti": Exito]
2. Estado de los agentes
3. Número total de nombres conocidos: "7"
4. El número total de nombres para cada objeto es de...
  - Para el objeto "kabe" existen "1" nombres
  - Para el objeto "ze" existen "1" nombres
  - Para el objeto "beñibevuti" existen "1" nombres
  - Para el objeto "deca" existen "1" nombres
  - Para el objeto "jo" existen "1" nombres
  - Para el objeto "giyufuveposu" existen "1" nombres
  - Para el objeto "teqodolusi" existen "1" nombres
5. La longitud promedio de todos los nombres es de: "5"

```json
{
    "kabe": [
        "\u00f1ibiyozida"
    ], 
    "ze": [
        "jo"
    ], 
    "be\u00f1ibevuti": [
        "jihunu"
    ], 
    "deca": [
        "re"
    ], 
    "jo": [
        "\u00f1edunozi"
    ], 
    "giyufuveposu": [
        "do"
    ], 
    "teqodolusi": [
        "kuhudo"
    ]
}
```

*******
## Créditos

Autor: *Jorge Luis Jácome Domínguez*

######  Otros medios < [Linkedin](https://www.linkedin.com/in/jorge-luis-j%C3%A1come-dom%C3%ADnguez-44294a91/) - [Dibujando](https://dibujando.net/soragefroren) - [Facebook](https://www.facebook.com/SoraGefroren) - [Youtube](https://www.youtube.com/c/SoraGefroren) >

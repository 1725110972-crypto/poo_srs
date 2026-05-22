# Repositorio de Programación Orientada a Objetos con Python
Repositorio con ejercicios de Programación Orientada a Objetos
## 1. Crear el archivo .gitignore 
Crear el .gitignore para configurar los archivos y carpetas que no deseamos que se guarden en el repositorio.

````shell 
*.pyc
_pycache_/
````

## 2. Indexar archivos y carpetas

Indexa todos los directorios y carpetas en busca de documentos nuevos.

````shell
git add .
````

## 3. Crear un COMMIT
Crea un COMMIT o un punto de control de los cambios realizados en el proyecto.

 ```` shell
 git commit -m "CREATED .gitignore"
````
* CREATED - Se crean nuevas carpetas y archivos
* UPDATED - Se actualizaron o agregaron nuevas funciones
* FIXED - Se corrigieron errores.

## 4. Realizar el COMMIT 
Sincroniza los cambios realizados en el repositorio.

````shell
git push -u origin main
````

## 5. Agregar Documentación a los Métodos

Agregar un **Docstring** a los métodos generados

```python
````shell
def metodoUno(self, variable_uno:int, variable_dos:float)->int:
 suma=variable_uno + variable_dos
        return int(suma)
````
La documentación se hace en 3 pasos:

1. **Descripción:** Una explicación breve en la primera línea sobre qué hace la función en general(qué hace y para qué sirve)como una acción.
2. **Argumentos:** Se lista cada variable que recibe la función, indicando su tipo entre paréntesis}. Una explicación clara de qué representa esa variable o para qué se utilizará  (`Args:`).
3. **Resultadoy Retorno:** : Se indica qué tipo de dato devuelve la función al terminar (si aplica) y qué significa ese resultado "El resultado exacto de la suma"(`Returns:`).

```

## descarga 
````shell
git. pull
````
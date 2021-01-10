La explicacion de este tutorial sera mas teorico ya que no comprendi correctamente lo que tenia que tener este tutorial 

Tenemos que comenzar explicando la diferencia que hay entre Git y Github :
- **Git**: Este es un sistema de control de versiones el cual e libre y open source. Ya que es un sistema distribuido facilita el desarrollo remoto entre equipos de trabajos , ayudando en el desarrolo paralelo el cual esta preparado para los conflictos que puedan ocurrir entre las modificaciones que se hagan paralelamente.

- **GitHub**: Este es un servicio web de alojamiento el cual permite la centralizacion del trabajo que se realiza con la ayuda de git, este incorporta otras funcionalidades como:
            
            - Herramientas analiticas
            - Gestion de permisos y licencias
            - Apoyo mutuo de diferentes fuentes
        
Github siendo como la wikipedia de la programacion ,contiene una gran cantidad de algoritmos los cuales sirven como apoyo en proyectos de diferentes areas de informatica , siendo una herramienta muy importante para el trabajo informatico.

Git cuenta con una linea de comandos que facilita el uso de este , algunos comandos son:

1. Etapas iniciales.

Comando|Descripcion
---|---
`git init`|iniciar un repositorio vacio.
`git add`| Añade todos los archivos
`git add “nombre_de_archivo”`|Añade un archivo especifico al repositorio 
`git commit -am "mensaje"`| Confirma los cambios realizados al repositorio, "mensaje" sirve para agregar una descripcion al commit.
`git push origin my-new-branch`|Hace un push a una rama hacia un repositorio remoto para enviar una rama al repositorio GitHub
`git push --all origin`|Sube todas las ramas al repositorio remoto.

2. Checkeo y eliminacion de Archivos y ramas

Comando|Descripción
---|---
`git status`|Lista los archivos modificados, y los que no fueron incluídos por `add` o `commit`
`git remote -v`|Lista los repositorios remotos configurados dentro del directorio de llamada
`git branch`|Lista las ramas disponibles, y muestra la actual.
`git branch -d <branch_name>`|Elimina la rama especificada.
`git push origin :<branch_name>`|Elimina la rama especificada del repositorio remoto.

3. Modificaciones en el repositorio.

Comando|Descripción
---|---
`git pull`|Descargar y combinar los cambios del repositorio remoto con el local.
`git merge <branch_name>`|Combinar la rama especificada con la actual.
`git diff`|Muestra todos los conflictos de combinación
`git checkout -- <filename>`|Permite revertir cambios respecto a los últimos archivos confirmados con `git add`.
`git fetch origin && git reset --hard origin/master`|Revierte todos los cambios efectuados, y se alínea con los archivos del repositorio remoto.

Coloque los comandos que para mi eran de mayor importancia de Git pero existen muchos mas los cuales dan una gran manipulacion a los repositorios almacenados en esta plataforma.

Go es un lenguaje de código abierto, compilado y tipificado estáticamente según la tradición de Algol y C. Cuenta con características como recolección de basura, tipificación estructural limitada, funciones de seguridad de la memoria y programación concurrente de estilo CSP fácil de usar.

Instalacion 
```
#Instalar golang
sudo apt install golang

#revisar version
go version

#Go Environment
export GOROOT=/usr/local/go 
export GOPATH=$HOME/Projects/Proj1 
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH 
sudo apt remove erlang-examples
#configurar variables
go env 
```

## Codigo HOLA MUNDO
nombramos un archivo como hola_mundo.go
```
package main

import "fmt"

func main() {
    fmt.Println("Hello, 世界")
}
 
```
para ejecutarlo debemos usar

```
go run <nombre archivo>
```

> tambien es posible compilarlo y luego ejecutarlo
> par ello debemos usar ```go build <nombre_archivo>```
> y lo ejecutamos ```./nombre_archiivo```

en go para importar librerias tenemos que agregarlas a import("libreria")
un ejemplo
```
import (
	"fmt"
	"time"
        )
```

es necesario en cada codigo definir el paquete en el que trabajamos como se vio en hola mundo, definimos que estabamos en `package main`

un ejemplo un poco mas avanzando y enfocado en el lado fuerte de go
el siguente codigo crea un pequeño servidor que atenderá peticiones HTTP.
lo nombraremos ht.go
```
package main
import (
  "fmt"
  "net/http"
)
func manejador(w http.ResponseWriter, r *http.Request){
  fmt.Fprintf(w,"Hola, %s, ¡este es el servidor!", r.URL.Path)
}
func main(){
  http.HandleFunc("/", manejador)
  fmt.Println("El servidor se encuentra en ejecución")
  http.ListenAndServe(":8080", nil)}

```

para compilar y ejecutarlos 
```
go build ht.go
./ht
```
ahora podemos comprobar el servidor con
```
http://localhost:8080/ht
```

nos entregara el siguente mensaje
```
Hola, /codingornot, ¡este es el servidor!
```
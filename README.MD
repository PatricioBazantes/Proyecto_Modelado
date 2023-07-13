# Replicación, MongoDB, Flask API, Bootstrap

####Autores: Bazantes Patricio, Macas Anthony, Tamayo Pablo.

------------

Este proyecto consiste en un proceso ETL para extraer datos de una base de datos MongoDB, transformarlos según sea necesario y cargarlos en una nueva estructura de datos. Además, incluye dos aplicaciones web: una aplicación de CRUD (Crear, Leer, Actualizar, Eliminar) y una aplicación de lectura de datos.

##Proceso ETL
El proceso ETL se encarga de la extracción, transformación y carga de datos desde una base de datos MongoDB. Aquí se muestra el flujo del proceso:

- Extracción: Los datos se extraen de la base de datos MongoDB utilizando la biblioteca PyMongo. La conexión a la base de datos se realiza mediante la siguiente URL: mongodb://192.168.1.4:27021/. Los datos se extraen de la colección health en la base de datos ProyectV1.

- Transformación: Durante la transformación, se aplican las modificaciones necesarias a los datos extraídos.

- Carga: Los datos transformados se cargan en una nueva estructura de datos o se almacenan en una base de datos diferente según los requisitos del proyecto. En este caso, los datos se cargan en una colección MongoDB.

##Aplicaciones Web
El proyecto incluye dos aplicaciones web desarrolladas con Flask, un framework de Python para aplicaciones web:

###Aplicación de CRUD
Esta aplicación permite realizar operaciones de Crear, Leer, Actualizar y Eliminar (CRUD) sobre los datos almacenados en la colección MongoDB.

Características de la aplicación:

Agregar Documento: Permite agregar un nuevo documento a la base de datos. Los datos se ingresan a través de un formulario HTML y se guardan en la colección health.

Editar Documento: Permite editar un documento existente en la base de datos. Se selecciona el documento a editar y se presentan los campos en un formulario HTML prellenado con los valores actuales. Al guardar los cambios, se actualiza el documento correspondiente en la colección health.

Eliminar Documento: Permite eliminar uno o varios documentos seleccionados de la base de datos.

Visualizar Documentos: Muestra una tabla con los documentos almacenados en la base de datos. También ofrece opciones de filtrado por edad y la posibilidad de deshacer el filtro.

###Aplicación de Lectura de Datos
Esta aplicación permite visualizar los datos almacenados en la colección health de la base de datos.

Características de la aplicación:

Visualización de Datos: Muestra una tabla con todos los documentos almacenados en la base de datos. Los datos se cargan utilizando la biblioteca jQuery para realizar una solicitud AJAX al servidor y obtener la respuesta en formato JSON.

Filtrado por Edad: Permite filtrar los datos por edad seleccionando una opción en el campo de filtro. Al aplicar el filtro, se cargan en la tabla solo los documentos que cumplen con el criterio de edad seleccionado.

## Requisitos
Para ejecutar el proyecto, se requiere lo siguiente:

- Python 3.x instalado en el sistema.
- Las siguientes bibliotecas de Python instaladas: Flask, PyMongo y bson.
- Docker
- docker-compose
- Mongo Compass
- Editor de codigo (Recomendado Visual Code)

## Instalación
**1. Forma ** Clic en Code y download Zip.
**2. Forma** Clona este repositorio:
   

##Configuración
[![Configuracion](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEie0j_TBXANSRNFiHkHF4fzdfAs9uDx3DZH5EdWjTB9b7BE_s7kypiIdQN51yUKdAQAluufQp2WShmOdKikRYnaq7h6ILErsm3MXdTmAKIOnmDVhekd7j050cwcPhxpzCEY6oleXA7rDLy-1LwTEgYC8uJYzfAHIlxDBahIkTB7KoMiswXrQKUaEhYOS8aR/s320/33.JPG "Configuracion")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEie0j_TBXANSRNFiHkHF4fzdfAs9uDx3DZH5EdWjTB9b7BE_s7kypiIdQN51yUKdAQAluufQp2WShmOdKikRYnaq7h6ILErsm3MXdTmAKIOnmDVhekd7j050cwcPhxpzCEY6oleXA7rDLy-1LwTEgYC8uJYzfAHIlxDBahIkTB7KoMiswXrQKUaEhYOS8aR/s320/33.JPG "Configuracion")

Es la configuración para enlazar la red entre cada uno de los contenedores que se levantaron.

Se debe hacer una por cada conexión que se realizó.

Una para el CRUD
Otra para la lectura.

Una vez realizado, se deberá replicar las bases de datos.


##Base de datos
Ya cargado los contenedores requeridos, y configurado, se inicia nuevas conexiones con: los puertos 27020 y 27025. Como esta trabajando con replicacion, los demas puertos ya esta cargado las bases de datos por igual.

Se descarga Student Mental health.csv.
Se accede a la base de  Mongo Compass
Se define una nueva base de datos('ProyectV1')
Se define una nueva coleccion ('health')

##Estructura del Proyecto
El proyecto sigue la siguiente estructura de carpetas:

- compose crud/: Contiene el .yaml que se encarga de levantar los 3 contenedeores maestros para realizar el CRUD de los datos..
- compose read/: Contiene el .yaml que se encarga de levantar los 3 contenedeores maestros para la lectura de los datos.
- Proyecto: Contiene la aplicacion web que se encarga de realizar el CRUD
- Proyecto_Read: Contiene la segunda parte de la aplicacion web que se encarga de la lectura de los datos.

##Metodos usados en la aplicacion web
La aplicacion web de CRUD utiliza los siguientes metodos.
[![Codigo](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7R9ixEh23pLMNZ3hprunGqsxQkC_3czZpn9wx8KqNPCCTInDASQmiIc4I8UHqhPt8DcXWStT9QFa_RfB4ffZ6aAtbFVPFqWIsMKxC2NhSIgApb_UcciytXgcK8rQnMj2vntv07O4383WGiXuaAqLWkcRGyLPL8uRViAFSC4NXCmeAV6JmwyjLQNH6c5eK/s320/21.JPG "Codigo")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj7R9ixEh23pLMNZ3hprunGqsxQkC_3czZpn9wx8KqNPCCTInDASQmiIc4I8UHqhPt8DcXWStT9QFa_RfB4ffZ6aAtbFVPFqWIsMKxC2NhSIgApb_UcciytXgcK8rQnMj2vntv07O4383WGiXuaAqLWkcRGyLPL8uRViAFSC4NXCmeAV6JmwyjLQNH6c5eK/s320/21.JPG "Codigo")

La aplicacion de lectura solo ultiliza metodo para visulizar los datos
[![Codigo](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgIT9uI8SKU_-DcBK3uevOUS_49N1Dadqo1VbjbiFht7FGYHZHduzF8tkN4Z75rsBFMDUJ6kQVmpwodMgyzxTKosrGTfc6Hvfak3iMH5_GRqu-G6lHl5z5H0qtQBuJd5MOxoparHbLkRF9UKofZ0wq59Mk4-UOs1IDc3Ibcx9dsWXCh7FXNHnIfKmzmy3oC/s320/22.JPG "Codigo")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgIT9uI8SKU_-DcBK3uevOUS_49N1Dadqo1VbjbiFht7FGYHZHduzF8tkN4Z75rsBFMDUJ6kQVmpwodMgyzxTKosrGTfc6Hvfak3iMH5_GRqu-G6lHl5z5H0qtQBuJd5MOxoparHbLkRF9UKofZ0wq59Mk4-UOs1IDc3Ibcx9dsWXCh7FXNHnIfKmzmy3oC/s320/22.JPG "Codigo")


##Uso
Una vez ya corriendo los contenedores y ya cargado los datos a MongoBD en ambas instancias, se debe ejecutar el codigo de la aplicacion web, en la que se desee trabajar.
Si se requiere iniciar con la aplicacion por CRUD se ejecuta y se inicia con la vista principal que consiste en la lista de todos los documentos de la coleccion. Se podra agregar un nuevo documento haciendo clic en el boton que corresponde, Editar los datos en caso de requerirlos, y eliminar los datos, mediente un checkbox.

Si se desea iniciar por la aplicacion de lectura, unicamente se visualizara la lista con todos los documentos de la base de datos.

##Resultados

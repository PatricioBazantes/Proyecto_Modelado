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

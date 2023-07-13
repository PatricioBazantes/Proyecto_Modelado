Para crear el bloque de contenedores de la izquierda se debe ejecutar el docker-compose.yaml que se encuentra 
en la carpeta compose crud, depende de los equipos se podria tunear los contenedores.
Abrimos un terminal y cambiamos a la ruta de la carpeta compose crud
Ingresamos el comando: docker compose up -d 
Ahora se abran creado el conjunto de la izquierda de dockers de mongo
Vamos a ingresar por el terminal al contenedor de mongo principal con el comando:
mongosh mongodb://<Direccion_Ip>:27020
debes reemplazar con tu ip actual.
Ahora una vez ingresado debemos copiar lo siguiente:
rs.initiate(
  {
    _id: "replicaRead1",
    members: [
      { _id : 0, host : <Direccion_Ip>:27020" },
      { _id : 1, host : <Direccion_Ip>:27021" },
      { _id : 2, host : <Direccion_Ip>:27022" }
    ]
  }
)
Ahora ejecutamos: rs.status()
Si al ejecutar rs.status() todos salen como secondary debemos modificar las prioridades

conf = rs.config();
conf.members[0].priority = 2;
rs.reconfig(conf);

rs.status()

Para crear el bloque de contenedores de la derecha se debe ejecutar el docker-compose.yaml que se encuentra 
en la carpeta compose read, depende de los equipos se podria tunear los contenedores.
Abrimos un terminal y cambiamos a la ruta de la carpeta compose read
Ingresamos el comando: docker compose up -d 
Ahora se abran creado el conjunto de la derecha de dockers de mongo
Vamos a ingresar por el terminal al contenedor de mongo principal con el comando:
mongosh mongodb://<Direccion_Ip>:27025
debes reemplazar con tu ip actual.
Ahora una vez ingresado debemos copiar lo siguiente:
rs.initiate(
  {
    _id: "replicaRead1",
    members: [
      { _id : 0, host : <Direccion_Ip>:27025" },
      { _id : 1, host : <Direccion_Ip>:27026" },
      { _id : 2, host : <Direccion_Ip>:27027" }
    ]
  }
)
Ahora ejecutamos: rs.status()
Si al ejecutar rs.status() todos salen como secondary debemos modificar las prioridades

conf = rs.config();
conf.members[0].priority = 2;
rs.reconfig(conf);

rs.status()




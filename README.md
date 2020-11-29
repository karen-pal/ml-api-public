# Despliegue de sistemas predictivos
> Diplodatos 2019

## Instalar y ejecutar

```
$ docker-compose up --build -d
```

Para detener los servicios:

```
$ docker-compose down
```

## Tests

- Instalar un virtualenv con los requirements.txt del origen
```
virtualenv --python=python3.5 .env
source .env/bin/activate
pip install -r requirements.txt
```
- Correr los tests con nosetests
```
nosetests [<package_name>]
nosetests model
```

- Si no tienen python3.5 y no lo quieren instalar, pueden probar instanciando un container con python 3.5 montando un volumen para ver los cambios dinamicamente

```
docker run -v $(pwd):/src -it --net=host -w /src python:3.5 bash
pip install -r requirements.txt
nosetests [<package_name>]
```

Frontend running at
```
localhost:8100
```

# Stress tests
Probar con locust
Teniendo todas las cosas arriba:
instalar locust en algun virtualenv
```
pip install locust
```
correr locust en nuestra app
```
locust -f ./stress_test/locustfile.py
```

entrar a http://localhost:8089/

# Monitoreo
Levantar el nuevo docker compose de monitoreo
```
docker-compose -f docker-compose.yml.monitor up -d
docker-compose -f docker-compose.yml.monifor logs -f
```

ver la interfaz en
```
localhost:9000
```

admin, admin


definir input tipo GELF UDP
launch new input tipo GELF UDP. seleccionar nodo.
titulo udp gelf
start input

# grafana
http://localhost:3000/
grafana

admin,admin

data source -> elasticsearch
URL http://elasticsearch:9200 <-nombre del servicio
TIME field name sin arroba
save & test
armás dashboard



# Yelp API
Este proyecto no fue terminado al 100% por falta de tiempo; hicieron falta hacer las prueas unitarias y el dockerfile.

No me justifico pero dejo evidencias del performance de la **API** y de como construlle.

### REALMENTE ESTOY INTERESADO EN QUE PUEDAN VER EL CODIGO QUE SE HIZO

# Intrucciones
## _Paso 1_
En el archivo **docker-compose.yml** en las lineas 22 y 34 se sustituye por la direccion donde se encuentra
el proyeto, para obtener el ruta se puede hacer desde la terminal con el sig. comando.
```bash
pwd
```
El resultado se agrega sustituyando _YOUR_PATH_.


## _Paso 2_
Ya con los cambios hechos, para construir los contenedores del proyecto se requiere el sig. comando.
Cabe recalcar que se debe abrir una terminal en la ruta donde se encuentra el proyecto con el archivo
_docker-compose.yml_.
```bash
docker compose -p yelp up -d
```
## _Paso 3_
Ya que el proceso de docker compose haya terminado, se requiere que se adjunten los archivos del dataset _.json_ la carpeta script en especifico se encuentra en la ruta:
```bash
/yelp/scripts/data/
```
Ya que en esa carpeta el codigo hacer insersion a la DB busca desde esa ruta

## _Paso 4_
Lo siguiente que se debe hacer es crear las tablas en la base de datos, esto se logra con el sig. comando.

_paso 1.1_ Ingresar al contenedor de docker
```bash
docker exec -it yelp_code bash
```
_paso 1.2_ Dirigirse al la ruta del proyecto
```bash
cd home/
```
_paso 1.3_ instalar paquetes de python que requiere el proyecto
```bash
pip3 install -r requirements.txt
```
_paso 1.4_ Construir la base de datos
```bash
python3 manage.py migrate
```
_paso 1.5_ Ejecutar el comando "Esto toma tiempo en cargar"
```bash
python3 manage.py runscript insert_default_data
```
Nota para fines practicos solo se cargan 100k reseñas.
_paso 1.6_ Correr el servidor
```bash
python3 manage.py runserver 0:8000
```
## _Paso 5_
La documentacion de la API fue hecha en **POSTMAN**
- [Documentacion](https://documenter.getpostman.com/view/15229397/2s8YRmKDCt)

# Diagrama
![alt text](https://raw.githubusercontent.com/milhhdz/yelp/master/images/01_diagrama.png)

# Resultados
## _1_ Lista de los negocios
![alt text](https://raw.githubusercontent.com/milhhdz/yelp/master/images/02_list_business.png)
## _2_ Detalles del negocio
![alt text](https://raw.githubusercontent.com/milhhdz/yelp/master/images/03_retrieve_business.png)
## _3_ Lista de los usuarios
![alt text](https://raw.githubusercontent.com/milhhdz/yelp/master/images/04_list_users.png)
## _4_ Detalle del usuario
![alt text](https://raw.githubusercontent.com/milhhdz/yelp/master/images/05_retrieve_user.png)
## _5_ Lista de las reseñas
![alt text](https://raw.githubusercontent.com/milhhdz/yelp/master/images/06_list_reviews.png)
## _6_ Detalles de la reseña
![alt text](https://raw.githubusercontent.com/milhhdz/yelp/master/images/07_retrieve_review.png)
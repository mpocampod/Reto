# **Laboratorio y reto**

**Nombre:** Paulina Ocampo Duque <br>
**Curso:** Tópicos Especiales en Telemática <br>
**Título:** Map/Reduce en Python con MRJOB <br>

*******

**Tabla de Contenido**

1. [Descarga de AWS CLI](#AWS)
2. [Creación del bucket S3 en consola](#S3)
3. [Creación del clúster en consola](#Cluster) 
4. [Ejecución de la versión serial/secuencial de la aplicación de wordcount-local.py](#ejecución) 
5. [Ejecución del programa utilizando el paradigma Map/Reduce](#Map)<br>
6. [Reto 5](#reto)<br>

*******

<div id='AWS'/> 

### **1. Descarga de AWS CLI**
[Descarga AWS CLI](https://docs.aws.amazon.com/es_es/cli/latest/userguide/getting-started-install.html) <br>
*Nota: en mi caso descargue en el SO de MacOS

![Captura de Pantalla 2023-05-31 a la(s) 11 13 51 p  m](https://github.com/mpocampod/Reto/assets/68925248/480235b9-156e-4bdc-8bc8-75728c10cebd)

Para comprobar que el shell puede encontrar y ejecutar el comando aws en $PATH, utilice los siguientes comandos.
```sh
    which aws
```
![Captura de Pantalla 2023-05-31 a la(s) 11 16 41 p  m](https://github.com/mpocampod/Reto/assets/68925248/757fdffc-3a4b-4f82-a556-4d4b031a43d5)
```sh
    aws --version
```
![Captura de Pantalla 2023-05-31 a la(s) 11 16 58 p  m](https://github.com/mpocampod/Reto/assets/68925248/c31964fc-9084-49b1-839b-b2d67a863469)

Luego con las credenciales de IAM de nuestra sesion en AWS ejecutaremos los siguientes datos con el comando
```sh
    aws configure
```
![Captura de Pantalla 2023-05-31 a la(s) 10 57 34 a  m](https://github.com/mpocampod/Reto/assets/68925248/f2239dee-fa4a-484a-8be9-24801a21fc53)

*******

<div id='S3'/> 

### **2. Creación del bucket S3 en consola**

Después de configurar las credenciales, lo que haremos será crear el servicio de almacenamiento de objetos S3 a través del comando
```sh
    aws s3 mb s3://mpocampod-lab6-emr
```
![Captura de Pantalla 2023-05-31 a la(s) 11 38 35 p  m](https://github.com/mpocampod/Reto/assets/68925248/8be0689d-1426-4ea2-8b3c-139f50de612b)
 
 Y comprobaremos su creación y los S3 anteriormente creados con el comando 
 ```sh
    aws s3 ls
```
![Captura de Pantalla 2023-05-31 a la(s) 11 41 13 p  m](https://github.com/mpocampod/Reto/assets/68925248/876bd1a9-052c-411e-a014-f63df417002f)

En nuestra cuenta de AWS se debe ver asi

![Captura de Pantalla 2023-05-31 a la(s) 11 05 46 a  m](https://github.com/mpocampod/Reto/assets/68925248/b4fe3108-8912-4d61-9ed5-84adad2681b9)

*******
<div id='Cluster'/> 

### **3. Creación del clúster en consola**

Para la creación del clúster utilizamos el siguiente comando que nos dice las preferencias de lo que queremos incluir en nuestro clúster
 ```sh
aws emr create-cluster \
    --name cluster-retlab \
    --release-label emr-6.10.0 \
    --service-role EMR_DefaultRole \
    --ec2-attributes KeyName=emr1,InstanceProfile=EMR_EC2_DefaultRole \
    --applications Name=Hue Name=Spark Name=Hadoop Name=Sqoop Name=Hive \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large InstanceGroupType=TASK,InstanceCount=1,InstanceType=m4.large \
    --no-auto-terminate
```
**Configuración** <br>
**Name:** cluster-retlab <br>
**Amazon EMR release:** emr-6.10.0 <br>
**Applications:**
    - Hue 4.4.0
    - Spark 2.4.3
    - Hadoop 2.8.5
    - Sqoop 1.4.7
    - Hive 2.3.5 <br>
**Instance groups:**
Primary. m4.large.
Core. m4.large
Task. m4.large <br>
**IAM roles:**
Service Role: Seleccione EMR_DefaultRole
Instance profile: Seleccione EMR_EC2_DefaultRole

Una vez creado el clúster por linea de comandos en nuestra cuenta de AWS se debe ver así 
![Captura de Pantalla 2023-06-01 a la(s) 4 33 33 p  m](https://github.com/mpocampod/Reto/assets/68925248/bf08e5bb-5ed7-4901-a595-1b106b8cc363)

**EMR**
![Captura de Pantalla 2023-05-31 a la(s) 12 18 40 p  m](https://github.com/mpocampod/Reto/assets/68925248/8c3d2adb-a2a6-41d3-8978-3737f35561c5)

![Captura de Pantalla 2023-05-31 a la(s) 12 18 31 p  m](https://github.com/mpocampod/Reto/assets/68925248/4b27642e-a55b-4b74-9979-270fb71198ac)

**Instancias EC2**
![Captura de Pantalla 2023-05-31 a la(s) 12 19 49 p  m](https://github.com/mpocampod/Reto/assets/68925248/e67c9e8d-09a0-4fc7-a507-f1f00618e2b7)

*******
<div id='ejecución'/> 

### **4. Ejecución de la versión serial/secuencial de la aplicación de wordcount-local.py**

En primer lugar iniciaremos nuestra instancia EC2 principal con el siguiente comando, teniendo en cuenta que trabajaremos desde un ec2_user y no desde el root.

 ```sh
   ssh -i "emr.pem" ec2-user@ec2-54-160-244-71.compute-1.amazonaws.com 
```
![Captura de Pantalla 2023-05-31 a la(s) 12 38 39 p  m](https://github.com/mpocampod/Reto/assets/68925248/dbd87988-a862-4736-8ad8-ac207abb9ab4)

Una vez dentro de la consola, actualizaremos yum e instalaremos git, python, pip y mrjob
 ```sh
    sudo yum update -y
    sudo yum install git -y
    sudo yum install python-pip -y
    sudo pip install mrjob 
```
Y clonaremos el repositorio para poder ejectuar el programa
 ```sh
   git clone https://github.com/ST0263/st0263-2023-1.git
```
Una vez clonado se ejecutan los siguientes comandos
 ```sh
   cd st0263-2023-1/"Laboratorio N6-MapReduce"/wordcount
   python wordcount-local.py ../../datasets/gutenberg-small/*.txt > salida-serial.txt
   more salida-serial.txt
   sudo nano salida-serial.txt
```
Mostrandonos este resultado en pantalla

![Captura de Pantalla 2023-06-01 a la(s) 5 17 41 p  m](https://github.com/mpocampod/Reto/assets/68925248/2d657c31-8a7c-48a0-870c-21c060a45685)
 

<div id='Map'/> 

### **5. Ejecución del programa utilizando el paradigma Map/Reduce**
Ahora usando la libreria mrjob python local con el siguiente comando 
 ```sh
   python wordcount-mr.py ../../datasets/gutenberg-small/*.txt
```
Tendriamos este resultado

![Captura de Pantalla 2023-06-01 a la(s) 6 12 30 p  m](https://github.com/mpocampod/Reto/assets/68925248/c24f55ab-dbdc-4a99-a559-4d41d7084d96)

Por último crearemos una carpeta y copiaremos nuestro dataset en el emr con el siguiente comando 
* Ten en cuenta que debes iniciar otra consola con hadoop

 ```sh
   ssh -i "emr1.pem" hadoop@ec2-174-129-50-230.compute-1.amazonaws.com
```
 ```sh
   hdfs dfs -mkdir /user/admin/
   hdfs dfs -copyFromLocal /home/hadoop/st0263-2023-1/datasets/ /user/admin/
```
Y luego ejecutaremos el comando para ejecutar el programa en un entorno Hadoop
 ```sh
   python wordcount-mr.py hdfs:///user/admin/datasets/gutenberg-small/*.txt -r hadoop --output-dir hdfs:///user/admin/result3
```
Obteniendo el siguiente resultado

![Captura de Pantalla 2023-06-01 a la(s) 6 18 41 p  m](https://github.com/mpocampod/Reto/assets/68925248/35de39a3-7108-4eb6-8426-ed0fb4c2fcf5)

![Captura de Pantalla 2023-06-01 a la(s) 6 18 13 p  m](https://github.com/mpocampod/Reto/assets/68925248/d0dac2af-0713-4cc1-a1e4-30b2c7a3730c)
 

*******

<div id='reto'/> 

### **1. Reto 5**

*******

Parte del laboratorio realizado anteriormente es la base para la continuación del reto 5, empezamos clonando en la instancia principal ec2 el repositorio donde est'an almacenados los códigos.
 ```sh
      git clone https://github.com/mpocampod/Reto.git
      cd Reto/retoCodigos/
```

**Primer punto**
Realizar un programa en Map/Reduce, con hadoop en Python, que permita calcular de acuerdo a un conjunto de datos los siguientes puntos, en primer lugar comenzamos accediendo a la carpeta donde se encuentra la información

```sh
      cd dian
```
Luego copiamos los datos en un directorio

```sh
      hdfs dfs -put dataempleados.txt hdfs:///user/admin/dataempleados.txt
```
 a.  El salario promedio por Sector Económico (SE)
 
-Local
 
 ```sh
     python3 salario_sector_economico.py  dataempleados.txt	
```

<img width="1086" alt="Captura de pantalla 2023-06-01 a la(s) 9 36 41 p m" src="https://github.com/mpocampod/Reto/assets/68925248/ded9e8b7-9bbc-4c24-beee-d8d405a89e12">

 - EMR
```sh
    python salario_sector_economico.py hdfs:///user/admin/dataempleados.txt -r hadoop --output-dir hdfs:///user/admin/punto1a
```
Luego lo ejecutamos con el siguiente comando 
```sh
    hdfs dfs -cat /user/admin/punto1a/*
```

Y tenemos como resultado 


-S3
Para la creación en S3 utilizamos el siguiente comando
```sh
    python salario_sector_economico.py hdfs:///user/admin/dataempleados.txt -r hadoop --output-dir s3://mpocampod-lab6-emr/test1/1a
      hdfs dfs -cat s3://mpocampod-lab6-emr/test1/1a/*
```

Imagen 

 b. El salario promedio por Empleado
 
-Local
 
 ```sh
     python3 salario_empleado.py  dataempleados.txt	
```
<img width="1027" alt="Captura de pantalla 2023-06-01 a la(s) 9 47 06 p m" src="https://github.com/mpocampod/Reto/assets/68925248/5b616ce5-3b65-4770-b33d-dba64434ec24">


- EMR
```sh
    python salario_empleado.py hdfs:///user/admin/dataempleados.txt -r hadoop --output-dir hdfs:///user/admin/punto1b
```
Luego lo ejecutamos con el siguiente comando 
```sh
    hdfs dfs -cat /user/admin/punto1b/*
```

Y tenemos como resultado 


-S3
Para la creación en S3 utilizamos el siguiente comando
```sh
    python salario_empleado.py hdfs:///user/admin/dataempleados.txt -r hadoop --output-dir s3://mpocampod-lab6-emr/test1/1b
      hdfs dfs -cat s3://mpocampod-lab6-emr/test1/1b/*
```

Imagen

c. Número de SE por Empleado que ha tenido a lo largo de la estadística

-Local
 
 ```sh
     python3 sector_empleado.py  dataempleados.txt	
```

<img width="1050" alt="Captura de pantalla 2023-06-01 a la(s) 10 03 31 p m" src="https://github.com/mpocampod/Reto/assets/68925248/00a8b925-616e-45bb-9a31-8bb02b4524f0">


- EMR
```sh
    python sector_empleado.py hdfs:///user/admin/dataempleados.txt -r hadoop --output-dir hdfs:///user/admin/punto1c
```
Luego lo ejecutamos con el siguiente comando 
```sh
    hdfs dfs -cat /user/admin/punto1c/*
```

Y tenemos como resultado 


-S3
Para la creación en S3 utilizamos el siguiente comando
```sh
    python sector_empleado.py hdfs:///user/admin/dataempleados.txt -r hadoop --output-dir s3://mpocampod-lab6-emr/test1/1c
      hdfs dfs -cat s3://mpocampod-lab6-emr/test1/1c/*
```


**Segundo punto**
Realizar un programa en Map/Reduce, con hadoop en Python, que permita calcular de acuerdo a un conjunto de datos los siguientes puntos, en primer lugar comenzamos accediendo a la carpeta donde se encuentra la información

```sh
      cd bolsa
```
Luego copiamos los datos en un directorio

```sh
      hdfs dfs -put dataempresas.txt hdfs:///user/admin/dataempresas.txt
```
a. Por acción, dia-menor-valor, día-mayor-valor

-Local
```sh
        python accion_fecha.py  dataempresas.txt
```
<img width="990" alt="Captura de pantalla 2023-06-01 a la(s) 10 32 48 p m" src="https://github.com/mpocampod/Reto/assets/68925248/c1e18753-8b97-4b09-9f4a-b072172c705b">

-EMR
```sh
        python accion_fecha.py hdfs:///user/admin/punto2/dataset.txt -r hadoop --output-dir hdfs:///user/admin/punto2a
```
b. Listado de acciones que siempre han subido o se mantienen estables.

-Local
```sh
        python acciones_estables.py  dataempresas.txt
```
<img width="1051" alt="Captura de pantalla 2023-06-01 a la(s) 10 58 41 p m" src="https://github.com/mpocampod/Reto/assets/68925248/504f7fbe-85c0-4eb5-8f9f-4c1fd1f0575c">

c. DIA NEGRO: Día en el que la mayor cantidad de acciones tienen el menor valor de acción (DESPLOME), suponiendo una inflación independiente del tiempo.

-Local
```sh
        python dia_negro.py  dataempresas.txt
```
<img width="1050" alt="Captura de pantalla 2023-06-01 a la(s) 11 26 06 p m" src="https://github.com/mpocampod/Reto/assets/68925248/a95e9194-e881-48e7-a9a1-15ac1cd9e160">


**Tercer punto**

Realizar un programa en Map/Reduce, con hadoop en Python, que permita calcular de acuerdo a un conjunto de datos los siguientes puntos, en primer lugar comenzamos accediendo a la carpeta donde se encuentra la información

```sh
      cd peliculas
```
Luego copiamos los datos en un directorio

```sh
      hdfs dfs -put datapeliculas.txt hdfs:///user/admin/datapeliculas.txt
```
a. Número de películas vista por un usuario, valor promedio de calificación

-Local 
```sh
       python peliculas_usuario_promedio.py datapeliculas.txt
```
<img width="1106" alt="Captura de pantalla 2023-06-02 a la(s) 12 08 04 a m" src="https://github.com/mpocampod/Reto/assets/68925248/6fb66105-3186-408b-a1f3-6dfe016a0266">

b. Día en que más películas se han visto
-Local 
```sh
       python dia_mas_peliculas.py datapeliculas.txt
```
<img width="1072" alt="Captura de pantalla 2023-06-02 a la(s) 12 19 06 a m" src="https://github.com/mpocampod/Reto/assets/68925248/68da29ca-1e20-4d8b-91ef-668c4ca09616">

c. Día en que menos películas se han visto
-Local 
```sh
       python dia_menos_peliculas.py datapeliculas.txt
```
<img width="1061" alt="Captura de pantalla 2023-06-02 a la(s) 2 50 01 a m" src="https://github.com/mpocampod/Reto/assets/68925248/d4030168-869a-4687-ad9a-586ac7a474b8">

d. Número de usuarios que ven una misma película y el rating promedio
-Local 
```sh
       python usuarios_peliculas.py datapeliculas.txt
```
<img width="1088" alt="Captura de pantalla 2023-06-02 a la(s) 12 34 39 a m" src="https://github.com/mpocampod/Reto/assets/68925248/c4724e02-150c-4a9c-b067-7f21c06062cb">

f. Día en que peor evaluación en promedio han dado los usuarios

-Local 
```sh
       python peor_evaluacion.py datapeliculas.txt
```
<img width="1039" alt="Captura de pantalla 2023-06-02 a la(s) 12 40 51 a m" src="https://github.com/mpocampod/Reto/assets/68925248/2ab8212a-7f8a-4239-86a1-9d7bc75013b8">

f. Día en que mejor evaluación han dado los usuarios

Local 
```sh
       python mejor_evaluacion.py datapeliculas.txt
```
<img width="1067" alt="Captura de pantalla 2023-06-02 a la(s) 12 42 45 a m" src="https://github.com/mpocampod/Reto/assets/68925248/0b2ccc78-d384-4bf7-973c-f1f57ac36e3a">

g. La mejor y peor película evaluada por genero
-Local 
```sh
       python pelicula_genero.py datapeliculas.txt
```
<img width="1052" alt="Captura de pantalla 2023-06-02 a la(s) 12 55 28 a m" src="https://github.com/mpocampod/Reto/assets/68925248/d2792662-5c1c-4a24-966b-2faebcb4e37f">

*******


**REFERENCIAS** <br>
https://github.com/ST0263/st0263-2023-1/tree/main/Laboratorio%20N6-MapReduce
https://docs.aws.amazon.com/es_es/cli/latest/userguide/getting-started-install.html
*******


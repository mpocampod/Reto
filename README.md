# **Reto 6**

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
    --ec2-attributes KeyName=emr,InstanceProfile=EMR_EC2_DefaultRole \
    --applications Name=Hue Name=Spark Name=Hadoop Name=Sqoop Name=Hive \
    --instance-groups InstanceGroupType=MASTER,InstanceCount=1,InstanceType=m4.large InstanceGroupType=CORE,InstanceCount=2,InstanceType=m4.large InstanceGroupType=TASK,InstanceCount=1,InstanceType=m4.large \
    --no-auto-terminate
```
- Configuración
Name: cluster-retlab
Amazon EMR release: emr-6.10.0
Applications: 
§ Hue 4.4.0
§ Spark 2.4.3
§ Hadoop 2.8.5
§ Sqoop 1.4.7
§ Hive 2.3.5

Instance groups:
Primary. m4.large.
Core. m4.large
Task. m4.large

IAM roles:
Service Role: Seleccione EMR_DefaultRole.
Instance profile: Seleccione EMR_EC2_DefaultRole

Una vez creado el clúster por linea de comandos en nuestra cuenta de AWS se debe ver así 

**EMR**
![Captura de Pantalla 2023-05-31 a la(s) 12 18 40 p  m](https://github.com/mpocampod/Reto/assets/68925248/8c3d2adb-a2a6-41d3-8978-3737f35561c5)

![Captura de Pantalla 2023-05-31 a la(s) 12 18 31 p  m](https://github.com/mpocampod/Reto/assets/68925248/4b27642e-a55b-4b74-9979-270fb71198ac)

**Instancias EC2**
![Captura de Pantalla 2023-05-31 a la(s) 12 19 49 p  m](https://github.com/mpocampod/Reto/assets/68925248/e67c9e8d-09a0-4fc7-a507-f1f00618e2b7)

*******

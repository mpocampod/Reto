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
[Descarga AWS](https://docs.aws.amazon.com/es_es/cli/latest/userguide/getting-started-install.html) <br>
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
 ![Captura de Pantalla 2023-05-31 a la(s) 11 25 16 p  m](https://github.com/mpocampod/Reto/assets/68925248/9f26293f-9c72-4b43-ab59-3144ae41e7b7)

*******


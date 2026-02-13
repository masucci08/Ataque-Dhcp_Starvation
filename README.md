# Ataque-Dhcp_Starvation

**Estudiante:** Masucci Franco Rincón  
**Matrícula:** 2024-1250  
**Asignatura:** Seguridad de Redes  
**Fecha:** 13/02/2026  

**Link del video:*https://itlaedudo-my.sharepoint.com/:v:/g/personal/20241250_itla_edu_do/IQDqDMBW5A-eQalVSdPDmZXAASxAv5qU3oMLhEoZbmFfHGw*

---

### Descripción y Topología 

El laboratorio se ha desplegado en un entorno virtualizado utilizando **GNS3**, simulando una infraestructura de red corporativa vulnerada desde el interior.

### Detalles de la Topología

<img width="521" height="302" alt="image" src="https://github.com/user-attachments/assets/973f36d1-6b4f-43d8-b383-4c296712c79b" />


* **Direccionamiento IP:** Subred `10.12.50.0/24`.

* **Segmento de Red:** `10.12.50.0/24`
* **Gateway (Víctima DoS):** Router Cisco (`10.12.50.1`)
* **Atacante:** Kali Linux (`eth0`)

| Dispositivo | Rol | Estado Inicial |
| :--- | :--- | :--- |
| **Router Gateway** | Servidor DHCP | Pool activo (254 IPs libres) |
| **Switch L2** | Infraestructura | Sin seguridad |
| **Kali Linux** | Atacante | Generador de tráfico |


### Objetivo del Script
Demostrar la vulnerabilidad de un servidor DHCP que no cuenta con mecanismos de validación de identidad (como Port Security). El objetivo es denegar el servicio a nuevos clientes legítimos impidiendo que obtengan una dirección IP.



### Parámetros Usados
El script utiliza la librería **Scapy** para la inyección de paquetes en capa 2/3.

* **Interfaz de Inyección:** `eth0`
* **Generación de MAC:** Función `RandMAC()` para aleatoriedad criptográfica.
* **Estructura del Paquete:**
    * `Ethernet`: Src=Random / Dst=Broadcast (`ff:ff:ff:ff:ff:ff`)
    * `IP`: Src=`0.0.0.0` / Dst=`255.255.255.255`
    * `UDP`: Sport=68 / Dport=67
    * `BOOTP`: Client Hardware Address (chaddr) aleatorio.
    * `DHCP Options`: Message-Type = `Discover`.

## Evidencia de Ejecución
## 1-
<img width="467" height="279" alt="tabla cdpvacia" src="https://github.com/user-attachments/assets/aa6fdd03-2f98-47c9-b43a-0c7aa154e9a6" />




## 2-
<img width="301" height="241" alt="ejecucion scapy" src="https://github.com/user-attachments/assets/1c044ad6-b447-467f-96b8-23d58dcd8e87" />





## 3-
<img width="459" height="272" alt="tabla cdlfull" src="https://github.com/user-attachments/assets/5518d5ea-19b6-4283-950f-017930def08e" />





---

### Requisitos para utilizar la herramienta.
Tener python3 instalado en la maquina atacante


### Medidas de Mitigación
Para proteger la infraestructura contra estos vectores de ataque, se recomiendan las siguientes configuraciones de endurecimiento (Hardening):

 ```bash
Desabilitar Cdp con el comando en el modo global:
### *NO CDP RUN*

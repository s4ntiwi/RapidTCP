# RapidTCP

RapidTCP es una herramienta en Python que escanea **todos los puertos TCP (1-65535)** de un objetivo y devuelve un output claro con los servicios y versiones detectadas.

## 🚀 Características
- Escanea **todos los puertos TCP** en un host.
- Detecta **servicios y versiones** utilizando Nmap.
- Salida de resultados en formato claro y legible.

## 📌 Requisitos

Antes de ejecutar el script, asegúrate de tener instalados:

- **Python 3.x**
- **Nmap** (para la detección de servicios y versiones)
- **Librería `python-nmap`**

Para instalar los requisitos en Linux:
```bash
sudo apt install nmap
pip install python-nmap
```

## 🛠 Instalación y Uso

1. Clona este repositorio:
```bash
git clone https://github.com/s4ntiwi/rapidtcp.git
cd rapidtcp
```

2. Ejecuta el escáner:
```bash
python rapidtcp.py
```

3. Ingresa la IP o dominio del objetivo cuando se te solicite.

## 📌 Ejemplo de Uso

```
Ingresa la IP o dominio a escanear: 192.168.1.1

Escaneando todos los puertos TCP (1-65535)...

PUERTO 22 - SSH - Version: OpenSSH 8.2p1
PUERTO 80 - HTTP - Version: Apache 2.4.41
PUERTO 443 - HTTPS - Version: nginx 1.18.0
```

## ⚠️ Disclaimer
Este código debe usarse **solo con fines educativos o con autorización**. No me hago responsable del mal uso de esta herramienta.

---
✍️ Desarrollado por SANTI


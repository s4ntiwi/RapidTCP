import socket
import nmap

def scan_ports(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, '1-65535', arguments='-sV -T4')  # Escaneo completo de puertos TCP
    
    results = []
    for host in scanner.all_hosts():
        for port in scanner[host]['tcp']:
            service = scanner[host]['tcp'][port]
            port_info = f"PUERTO {port} - {service['name'].upper()} - Version: {service.get('version', 'Desconocida')}"
            results.append(port_info)
    
    return results

def main():
    target = input("Ingresa la IP o dominio a escanear: ")
    
    print("\nEscaneando todos los puertos TCP (1-65535)...\n")
    results = scan_ports(target)
    
    if results:
        for result in results:
            print(result)
    else:
        print("No se encontraron puertos abiertos o servicios detectables.")

if __name__ == "__main__":
    main()

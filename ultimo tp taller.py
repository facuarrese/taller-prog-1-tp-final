import os
from collections import Counter

if not os.path.exists('server_log.txt'):
    print("El archivo 'server_log.txt' no existe. Asegúrate de descargarlo.")
    exit()

with open('server_log.txt', 'r') as file:
    logs = file.readlines()

ip_count = Counter()
for line in logs:
    try:
        ip = line.split()[0]
        ip_count[ip] += 1
    except IndexError:
        continue

print("IPs y número de accesos:")
for ip, count in ip_count.items():
    print(ip, ":", count)

# Contar accesos por página
page_count = Counter()
for line in logs:
    try:
        page = line.split()[6]
        page_count[page] += 1
    except IndexError:
        continue

most_visited = page_count.most_common(3)
print("\nLas 3 páginas más visitadas:")
for page, count in most_visited:
    print(page, ":", count)

total_accesses = len(logs)
success_count = sum(1 for line in logs if " 200 " in line)
success_percentage = (success_count / total_accesses) * 100
print(f"\nPorcentaje de accesos exitosos (código 200): {success_percentage:.2f}%")
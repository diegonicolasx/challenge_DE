from  q1_memory import q1_memory
from q1_time import q1_time

file_path = "data/farmers-protest-tweets-2021-2-4.json"

top_ten_data = q1_memory(file_path)

print("Top 10 fechas con más tweets y su usuario más activo.")

for date, username in top_ten_data:
    print(f"Fecha: {date}, Usuario más activo: {username}")


top_ten_data = q1_time(file_path)

print("Top 10 fechas con más tweets y su usuario más activo.")
for date, username in top_ten_data:
    print(f"Fecha: {date}, Usuario más activo: {username}")
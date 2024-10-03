from  q1_memory import q1_memory

file_path = "data/farmers-protest-tweets-2021-2-4.json"

top_ten_data = q1_memory(file_path)

print("Top Ten Dates and Their Most Active Users:")
for date, username in top_ten_data:
    print(f"Date: {date}, Most Active User: {username}")
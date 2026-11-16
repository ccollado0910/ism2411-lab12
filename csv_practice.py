import csv

# --- Exercise 1 ---
# Check that data/sales.csv is there and has a header plus 12 data rows
with open("data/sales.csv") as file:
    lines = file.readlines()

print("Opened data/sales.csv")
print(f"Header: {lines[0].strip()}")
print(f"Data rows: {len(lines) - 1}")

# --- Exercise 2 ---
with open("data/sales.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# Every value prints in quotes, so they are all strings, even the numbers

# --- Exercise 3 ---
with open("data/sales.csv") as file:
    reader = csv.reader(file)
    header = next(reader)
    print(f"Header: {header}")
    for row in reader:
        print(row)

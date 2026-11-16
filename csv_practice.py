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

# --- Exercise 4 ---
total_revenue = 0

with open("data/sales.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        total_revenue += line_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

# --- Exercise 5 ---
original_count = 0
written_count = 0

with open("data/sales.csv") as infile, open("data/cleaned.csv", "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])

    for row in reader:
        original_count += 1
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        if line_total > 100:
            writer.writerow([row[0], f"{price:.2f}", quantity, f"{line_total:.2f}"])
            written_count += 1

print(f"Wrote {written_count} of {original_count} rows to data/cleaned.csv")

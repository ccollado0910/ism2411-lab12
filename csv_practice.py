# Self Assessment Questions
# Q1: In Excel I would have to type the total formula, drag it down, filter for orders over $100, and copy them to a new sheet, and I would have to do all of that again every time I got a new file. With Python I write the steps once and just run the script on any new file, and it works the same on 12 rows or a million. Excel is still easier when I just want to look at the data, fix one cell, or make a quick chart without writing code.
# Q2: At my restaurant job, a script could run at closing every night and add the date and that day's total sales to a log file. Append mode is the right tool because each night adds a new line and keeps all the nights before it, so the manager gets a running history. If it used "w" mode, every run would erase the file and only the last night would be left.

import csv
from datetime import datetime

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

# --- Exercise 6 ---
# csv.reader is fine for small files where I know the column order, like row[1] for price.
# csv.DictReader is better when there are a lot of columns or the order might change, because row["price"] is easier to read.
dict_total = 0

with open("data/sales.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        line_total = price * quantity
        dict_total += line_total
        print(f"{row['product']}: {quantity} units × ${price:.2f} = ${line_total:.2f}")

print(f"Total revenue: ${dict_total:.2f}")
print(f"Same as Exercise 4: {round(dict_total, 2) == round(total_revenue, 2)}")

# --- Exercise 7 ---
summary = {}

with open("data/sales.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row["product"]
        line_total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + line_total

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

# --- Exercise 8 ---
# "a" adds a new line to the end each run instead of erasing the file like "w" would
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("data/run_log.txt", "a") as log:
    log.write(f"{now} | Total revenue: ${total_revenue:.2f}\n")

print(f"Logged this run to data/run_log.txt at {now}")

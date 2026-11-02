import csv

book_records = [
    {"title": "Python Basics", "price": "5000"},
    {"title": "Learning Django", "price": "6500"},
]

with open("books.csv", "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["title", "price"])
    writer.writeheader()
    writer.writerows(book_records)

print("Saved records to books.csv")

"""
DictWriter writes dictionaries into a CSV file.
writeheader() writes the column names; writerows() writes the records.
"""
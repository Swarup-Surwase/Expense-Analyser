import csv 
from datetime import datetime
from collections import defaultdict

categories = {
    "Food" : ["swiggy", "zomato", "restaurant", "cafe", "zepto"],
    "Travel" : ["ola", "rapido", "uber"],
    "Subscriptions" : ["netflix", "prime", "jio hotstar"],
    "Shopping" : ["amazon", "flipkart", "myntra", "meesho"],
    "Bills": ["loksewa", "electricity", "recharge"],
}

def categoriez(description):
    description = description.lower()
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in description:
                return category
    return "Other"



transactions = []


with open("demo_transactions.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)
    print("COLUMNS:", reader.fieldnames)
    for row in reader:
        if row["Debit"].strip() == "":
            continue

        date = datetime.strptime(row["Date"], "%d/%m/%Y")
        description = row["Details"]
        amount = float(row["Debit"].replace(",", ""))

        transactions.append({
            "date": date,
            "description": description,
            "amount": amount,
            "category": categoriez(description)
        })

for t in transactions:
    print(t["date"].strftime("%d %b %Y"), "|", t["description"], "|","₹",t["amount"], "|", t["category"])
    

category_totals = defaultdict(float)

for t in transactions:
    category_totals[t["category"]] += t["amount"]

print()
print("Spendings by categories =>")

for category, total in category_totals.items():
    print(category, ":" , total)


month_totals = defaultdict(float)

for t in transactions:
    month = t["date"].strftime("%Y-%m")
    month_totals[month] += t["amount"]

print()
print("Spendings by months =>")

for month in sorted(month_totals):
    print(month, ":", month_totals[month]) 

print()
print("Top 3 Categories =>")
top_categories = sorted(category_totals.items(), key=lambda item: item[1], reverse=True)[:3]
for cateogry, total in top_categories:
    print(category, ":", total)

print()
print("Top 5 Expenses =>")
top_expenses = sorted(transactions, key=lambda t: t["amount"],reverse = True)[:5]
for t in top_expenses:
    print(t["date"].strftime("%d %b %Y"), "|", t["description"], "|", t["amount"])

print()
average = sum(t["amount"] for t in transactions) / len(transactions)
thresold = average * 2

print("Your average spending is =>", round(average, 2))
print()
found = False
print("Unusual spends (above", round(thresold, 2), ") =>")
for t in transactions:
    if t["amount"] > thresold:
        found = True
        print("⚠️😭 ", t["amount"], "|", t["date"].strftime("%d %b %Y"), "|", t["description"])

if not found:
    print()
    print("🥳 Good news..! There are No Unusual Transactions.")

print()

with open("report.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["🛒 SPENDING BY CATEGORY =>"])
    writer.writerow([])
    writer.writerow(["Category", "Total"])
    writer.writerow([])
    for category, total in sorted(category_totals.items(), key=lambda item: item[1], reverse=True):
        writer.writerow([category, "₹",total])

    writer.writerow([])
    writer.writerow([])
    writer.writerow(["📅 SPENDING BY MONTH =>"])
    writer.writerow([])
    writer.writerow(["Month", "Total"])
    writer.writerow([])
    for month in sorted(month_totals):
        writer.writerow([month, "₹",month_totals[month]])

    writer.writerow([])
    writer.writerow([])
    writer.writerow(["😭 UNUSUAL SPENDS =>"])
    writer.writerow([])
    writer.writerow(["Date", "Description", "Amount"])
    writer.writerow([])
    for t in transactions:
        if t["amount"] > thresold:
            writer.writerow(["⚠️ ",t["date"].strftime("%d %b %Y"), "₹",t["amount"], t["category"]])

print()
print("Report saved to report.csv")
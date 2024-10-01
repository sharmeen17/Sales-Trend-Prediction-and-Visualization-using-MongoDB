import pymongo
import matplotlib.pyplot as plt

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["salesDB"]
sales_data = db["salesData"]

# Fetch daily sales data
daily_sales = list(sales_data.aggregate([
    {"$group": {"_id": "$date", "totalRevenue": {"$sum": "$revenue"}}},
    {"$sort": {"_id": 1}}
]))

# Extract dates and revenues
dates = [entry["_id"] for entry in daily_sales]
revenues = [entry["totalRevenue"] for entry in daily_sales]

# Plot sales trend
plt.plot(dates, revenues, marker='o')
plt.title('Daily Sales Revenue')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


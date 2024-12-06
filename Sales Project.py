# -*- coding: utf-8 -*-
"""noman.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M_Ip-4AxXBPY2V8Q9szTbTQAu9QJIwDs
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'dataset_15_Furniture Sales.csv'  # Ensure this file is in the same directory
data = pd.read_csv(file_path)

data['Date'] = pd.to_datetime(data['Date'])  # Convert Date column to datetime

numerical_cols = ['Quantity', 'Price', 'Discount', 'Revenue']
Q1 = data[numerical_cols].quantile(0.25)
Q3 = data[numerical_cols].quantile(0.75)
IQR = Q3 - Q1
outliers = ((data[numerical_cols] < (Q1 - 1.5 * IQR)) | (data[numerical_cols] > (Q3 + 1.5 * IQR))).sum()

print("Data Information:")
print(data.info())

print("\nData Description:")
print(data.describe())

revenue_by_product = data.groupby('Product')['Revenue'].sum()

revenue_by_region = data.groupby('Region')['Revenue'].sum()

discount_by_customer = data.groupby('Customer_Type')['Discount'].mean()

plt.figure(figsize=(8, 5))
plt.bar(revenue_by_product.index, revenue_by_product.values, color='skyblue')
plt.title('Total Revenue by Product')
plt.ylabel('Revenue')
plt.xlabel('Product')
plt.tight_layout()
plt.savefig('revenue_by_product.png')
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(revenue_by_region.index, revenue_by_region.values, color='salmon')
plt.title('Total Revenue by Region')
plt.ylabel('Revenue')
plt.xlabel('Region')
plt.tight_layout()
plt.savefig('revenue_by_region.png')
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(discount_by_customer.index, discount_by_customer.values, color='green')
plt.title('Average Discount by Customer Type')
plt.ylabel('Average Discount')
plt.xlabel('Customer Type')
plt.tight_layout()
plt.savefig('discount_by_customer_type.png')
plt.show()
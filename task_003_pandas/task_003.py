import pandas as pd

data = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6],
    "customer_id": [101, 102, 101, 103, 102, 103],
    "order_date": ["2024-01-01", "2024-01-02", "2024-01-03",
        "2024-01-04", "2014-01-05", "2024-01-06"],
    "product": ["Apples", "Bananas", "Oranges",
        "Apples", "Bananas", "Oranges"],
    "amount": [100, 200, 150, 50, 300, 100]
})

# Задачи:
# 1. Найти суммарный объем продаж ('amount') для каждого продукта
# 2. Отфильтровать продукты с суммарными продажами больше 200

# 1
product_data = data.groupby('product', as_index=False)['amount'].sum()
product_data.columns = ['product','total_amount']

# 2
top_product_data = product_data[product_data['total_amount'] >= 200]
top_product_data.columns = ['top_product','total_amount']


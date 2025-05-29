import pandas as pd

data = pd.DataFrame({
    "customer_id": [101, 102, 103, 104],
    "order_date": ["2024-01-01", "2024-01-02", None, "2024-01-04"],
    "amount": [100, 200, 150, None]
})


# Задачи:
# 1. Заменить пропущенные даты в колонке 'order_date'
#    на последнее непропущенное значение даты из педыдущих строк
# 2. Заменить пропущенные значения в колонке 'amout'
#    на среднее значение по этой колонке


data_date_fill = pd.DataFrame(data=data)

# 1
data_date_fill['order_date'] = data_date_fill['order_date'].ffill()

# 2
data_date_fill['amount'] = data_date_fill['amount'].fillna(value=data_date_fill['amount'].mean())


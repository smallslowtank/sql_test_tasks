import pandas as pd
from pandasql import sqldf
import numpy as np


# В таблице user_actions сохраняются действия покупателей в интернет магазине, структура таблицы

# user_id    - id пользователя
# product_id - id товара
# action     - действие, просмотр товара, сохранение в корзину, покупка
# time       - время совершения события
# date       - дата события

# Для каждого дня рассчитайте, какой процент просмотров товаров завершился покупкой

all_user_ids = np.arange(1, 1001)
all_product_ids = np.arange(1, 101)
n = 10000
user_ids    = np.random.choice(all_user_ids, n)
product_ids = np.random.choice(all_product_ids, n)
start_date = pd.to_datetime('2022-01-01')
times = pd.date_range(start_date, periods=n, freq='1min')
user_actions = pd.DataFrame({'user_id': user_ids,
                             'product_id': product_ids,
                             'time': times})
user_actions['action'] = 'view'
user_actions.head()
def generate_funel_actions(user_id, product_id, time):
    to_cart = 0.2
    to_purchase = 0.4

    df = pd.DataFrame()

    if np.random.binomial(1, to_cart, 1)[0]:
        df = pd.DataFrame({
                           'user_id'   : user_id,
                           'product_id': product_id,
                           'time'      : time + pd.Timedelta(5, unit='s'),
                           'action'    : 'add to cart'}, index=[0])

        if np.random.binomial(1, to_purchase, 1)[0]:
            df_purchase = pd.DataFrame({
                           'user_id'   : user_id,
                           'product_id': product_id,
                           'time'      : time + pd.Timedelta(10, unit='s'),
                           'action'    : 'purchase'}, index=[0])

            df = pd.concat([df, df_purchase])
    return df
to_cart_df = pd.DataFrame()
for index, row in user_actions.iterrows():
    user_df = generate_funel_actions(row['user_id'], row['product_id'], row['time'])
    to_cart_df = pd.concat([to_cart_df,user_df])
user_actions = pd.concat([user_actions,to_cart_df])
user_actions = user_actions.sort_values('time')
user_actions['date'] = user_actions.time.dt.date
user_actions.head()
q = """SELECT date,
              views,
              carts,
              purchases,
              100 * purchases / views as purchase_percantage
       FROM (
           SELECT date,
            count(case when action = 'view'        then 1 else NULL end) as views,
            count(case when action = 'add to cart' then 1 else NULL end) as carts,
            count(case when action = 'purchase'    then 1 else NULL end) as purchases
           FROM user_actions
           GROUP BY date);"""
sqldf(q)

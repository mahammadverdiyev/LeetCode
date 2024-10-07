import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    customers_never_ordered = merged[merged['customerId'].isna()]
    result = customers_never_ordered[['name']].rename(columns={'name': 'Customers'})
    return result
    
import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    store_df = store[store.amount > 500]
    store_df = store_df["customer_id"].nunique()
    store_df = pd.DataFrame({'rich_count': [store_df]})
    return store_df
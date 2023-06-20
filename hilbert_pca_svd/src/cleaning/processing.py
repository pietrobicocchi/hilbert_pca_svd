import numpy as np
import pandas as pd


def raw_to_dataframes(df):
    df["datadate"] = pd.to_datetime(df["datadate"])
    df = df[['GVKEY', 'datadate', 'saleq', 'prccq']]
    aggregated = df.groupby([df["datadate"], df["GVKEY"]]).agg({"saleq": "sum", "prccq": "first"}).unstack()

    sales = aggregated["saleq"].resample("Q").sum()
    prices = aggregated["prccq"].resample("Q").last()

    return sales, prices


def tailored_clean(sales, sales_keys):
    sales = sales.replace(0, np.nan)

    def drop_companies(df, keys):
        return df.loc[:, df.columns.intersection(keys)]

    sales = drop_companies(df=sales, keys=sales_keys)  # Dropping companies
    sales = sales.fillna(0)

    log_ret = np.log(sales).diff()
    log_ret.replace([np.inf, -np.inf], np.nan, inplace=True)

    resc_log_ret = (log_ret - log_ret.mean()) / log_ret.std()
    resc_log_ret = resc_log_ret.fillna(0)

    return resc_log_ret
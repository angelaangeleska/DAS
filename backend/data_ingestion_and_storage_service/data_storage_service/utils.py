from django.db import connection

def create_table_for_stock_code(code):
    """Creates a table for the given stock code if it doesn't already exist."""
    table_name = f"{code}_stocks"
    with connection.cursor() as cursor:
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id SERIAL PRIMARY KEY,
                date DATE,
                open_price FLOAT,
                high_price FLOAT,
                low_price FLOAT,
                close_price FLOAT,
                volume INTEGER,
                dividend FLOAT,
                stock_splits FLOAT
            );
        """)
    print(f"Table '{table_name}' created (if not already existing).")


def insert_data_into_table(code, stock_data):
    """Inserts stock data into the corresponding table."""
    table_name = f"{code}_stocks"

    records = [
        (
            row.name.date(),
            float(row['Open']),
            float(row['High']),
            float(row['Low']),
            float(row['Close']),
            int(row['Volume']),
            float(row.get('Dividends', 0.0)),
            float(row.get('Stock Splits', 0.0))
        )
        for _, row in stock_data.iterrows()
    ]

    with connection.cursor() as cursor:
        cursor.executemany(
            f"""
            INSERT INTO {table_name} (date, open_price, high_price, low_price, close_price, volume, dividend, stock_splits)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """,
            records
        )
    print(f"Inserted {len(records)} rows into '{table_name}'.")


"""           

---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------

"""

def create_table_for_stock_news(code):
    """Creates a news table for the given stock code if it doesn't already exist."""
    table_name = f"{code}_news"
    with connection.cursor() as cursor:
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                summary TEXT
            );
        """)
    print(f"Table '{table_name}' created (if not already existing).")

def insert_data_into_news_table(code, news_data):
    """Inserts stock news into the corresponding table."""
    table_name = f"{code}_news"

    records = [
        (
            row.title,
            row.summary
        )
        for _, row in news_data.iterrows()
    ]

    with connection.cursor() as cursor:
        cursor.executemany(
            f"""
            INSERT INTO {table_name} (title, summary)
            VALUES (%s, %s);
            """,
            records
        )
    print(f"Inserted {len(records)} rows into '{table_name}'.")
import duckdb
import pandas as pd
from faker import Faker

fake = Faker()
df = pd.DataFrame({
    "name": [fake.name() for _ in range(3)],
    "amount": [10.5, 20.0, 30.25],
})
print(df)

con = duckdb.connect()  # in-memory database
con.register("sample", df)
print(con.execute("SELECT SUM(amount) AS total FROM sample").fetchdf())
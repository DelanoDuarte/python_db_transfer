import psycopg2

# Connect to the source database
source_conn = psycopg2.connect(
    dbname='source',
    user='root',
    password='root',
    host='localhost',
    port='5432'
)
source_cursor = source_conn.cursor()

# Connect to the destination database
destination_conn = psycopg2.connect(
    dbname='target',
    user='root',
    password='root',
    host='localhost',
    port='5433'
)
destination_cursor = destination_conn.cursor()

# Assuming we're migrating a single table named 'users'
source_table = 'users'
destination_table = 'users'

# Fetch data from the source table
source_cursor.execute(f"SELECT * FROM {source_table}")
data_to_migrate = source_cursor.fetchall()

# Close the source database connection
source_conn.close()

# Insert data into the destination table
for row in data_to_migrate:
    # Assuming the schema of the destination table is the same as the source table
    destination_cursor.execute(f"INSERT INTO {destination_table} VALUES (%s, %s, %s, %s)", row)

# Commit changes and close the destination database connection
destination_conn.commit()
destination_conn.close()

print("Migration completed successfully.")

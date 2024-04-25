import psycopg2


def dump_schema(connection_params, schema_name, dump_file):
    try:
        conn = psycopg2.connect(**connection_params)
        cursor = conn.cursor()

        # Dump the schema definition
        with open(dump_file, 'w') as f:
            cursor.copy_expert(f"COPY (SELECT * FROM information_schema.tables WHERE table_schema = '{schema_name}') TO STDOUT WITH CSV HEADER", f)

        conn.commit()
        print(f"Schema '{schema_name}' dumped successfully to {dump_file}")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error dumping schema:", error)

    finally:
        if conn is not None:
            cursor.close()
            conn.close()

def restore_schema(connection_params, schema: str, dump_file):
    try:
        conn = psycopg2.connect(**connection_params)
        cursor = conn.cursor()

        # Restore the schema definition
        with open(dump_file, 'r') as f:
            cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {schema}")
            cursor.copy_expert(f"COPY {schema} FROM STDIN WITH CSV HEADER", f)

        conn.commit()
        print(f"Schema '{schema}' restored successfully from {dump_file}")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error restoring schema:", error)

    finally:
        if conn is not None:
            cursor.close()
            conn.close()

def dump_database(connection_params, dump_file):
    try:
        conn = psycopg2.connect(**connection_params)
        cursor = conn.cursor()

        with open(dump_file, 'w') as f:
            cursor.copy_expert(f"COPY (SELECT * FROM {connection_params['table']}) TO STDOUT WITH CSV HEADER", f)

        conn.commit()
        print(f"Database dumped successfully to {dump_file}")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error dumping database:", error)

    finally:
        if conn is not None:
            cursor.close()
            conn.close()

def restore_database(connection_params, dump_file):
    try:
        conn = psycopg2.connect(**connection_params)
        cursor = conn.cursor()

        with open(dump_file, 'r') as f:
            cursor.copy_expert(f"COPY {connection_params['table']} FROM STDIN WITH CSV HEADER", f)

        conn.commit()
        print("Database restored successfully")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error restoring database:", error)

    finally:
        if conn is not None:
            cursor.close()
            conn.close()

# Example usage
source_connection_params = {
    'dbname': 'source',
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'port': '5432'
}

destination_connection_params = {
    'dbname': 'target',
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'port': '5433'
}

dump_file = 'database_dump.csv'

# Dump entire schema
dump_schema(source_connection_params, 'public', dump_file)

# Dump the source database
# dump_database(source_connection_params, dump_file)

# Restore the dump file into the destination database
# restore_database(destination_connection_params, dump_file)
restore_schema(destination_connection_params, 'public', dump_file)

print("Migration completed successfully.")

import subprocess
import os

def backup_db(host, port, username, password, database, backup_path):
    """
    Backup a PostgreSQL database.
    
    Args:
        host (str): PostgreSQL host.
        port (str): PostgreSQL port.
        username (str): PostgreSQL username.
        password (str): PostgreSQL password.
        database (str): Name of the database to backup.
        backup_path (str): Path to save the backup file.
    """
    # Construct the pg_dump command
    command = [
        'pg_dump',
        '-h', host,
        '-p', port,
        '-U', username,
        '-d', database,
        '-Fc',  # Custom format
        '-f', backup_path
    ]

    # Set the PGPASSWORD environment variable to pass the password
    os.environ['PGPASSWORD'] = password

    # Execute the pg_dump command
    subprocess.run(command)

def restore_db(host, port, username, password, database, backup_path):
    """
    Restore a PostgreSQL database from a backup file.
    
    Args:
        host (str): PostgreSQL host.
        port (str): PostgreSQL port.
        username (str): PostgreSQL username.
        password (str): PostgreSQL password.
        database (str): Name of the database to restore into.
        backup_path (str): Path to the backup file.
    """
    # Construct the pg_restore command
    command = [
        'pg_restore',
        '-h', host,
        '-p', port,
        '-U', username,
        '-d', database,
        '-c',  # Clean (drop) database objects before recreating them
        backup_path
    ]

    # Set the PGPASSWORD environment variable to pass the password
    os.environ['PGPASSWORD'] = password

    # Execute the pg_restore command
    subprocess.run(command)

# Example usage
if __name__ == "__main__":
    # Set your PostgreSQL connection details
    host = 'localhost'
    port = '5432'
    username = 'root'
    password = 'root'
    database = 'source'
    
    # Set your PostgreSQL connection details
    d_host = 'localhost'
    d_port = '5433'
    d_username = 'root'
    d_password = 'root'
    d_database = 'target'

    # Backup path
    backup_path = 'backup_file.dump'

    # Backup the database
    backup_db(host, port, username, password, database, backup_path)

    # Restore the database
    restore_db(d_host, d_port, d_username, d_password, d_database, backup_path)

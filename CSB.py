# this is a schema create bot 
# it will create schema in the database
from api import cur


def create_schema(schema_name):
    query = f"SELECT schema_name FROM information_schema.schemata WHERE schema_name = '{schema_name}';"
    cur.execute(query)
    schema_exists = cur.fetchall()

    if not schema_exists:
            cur.execute(f'CREATE SCHEMA "{schema_name}";')
            print(f"Schema '{schema_name}' has been created.")


create_schema("employee")
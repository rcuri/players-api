import psycopg2
import os


def get_player_by_name(player_name):
  credential = {
    'username': os.environ.get('POSTGRES_PROD_USERNAME'),
    'password': os.environ.get('POSTGRES_PROD_PASSWORD'),
    'host': os.environ.get('POSTGRES_PROD_HOST'),
    'db': os.environ.get('POSTGRES_PROD_DB')
  }
  connection = psycopg2.connect(
    user=credential['username'],
    password=credential['password'],
    host=credential['host'],
    database=credential['db']
  )
  cursor = connection.cursor()
  query = f"SELECT * FROM player JOIN stat ON player.player_id = stat.player_id WHERE to_tsvector(player_name) @@ plainto_tsquery('{player_name}');"
  cursor.execute(query)
  results = cursor.fetchone()
  if not results:
    return []
  colnames = [desc[0] for desc in cursor.description]
  cursor.close()
  connection.commit()
  player_dict = {}
  for key, val in zip(colnames, results):
    player_dict[key] = val
  return [player_dict]

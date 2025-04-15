import pandas as pd
import numpy as np
import mysql.connector
import json

# Loading data from json file
with open('quotes.json') as f:
    data = json.load(f)

# Converting it to DataFrame
df = pd.DataFrame(data)

# Filtering quotes with more than 2 tags
df['num_tags'] = df['tags'].apply(lambda x: len(x))
df_filtered = df[df['num_tags'] > 2].copy()

# Calculating text length
df_filtered['text_length'] = df_filtered['text'].apply(lambda x: np.char.str_len(x))

# Connecting to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='Ali',
    password='root1234',
    database='scrap_database'
)

cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS quotes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text TEXT,
    author VARCHAR(255),
    tags TEXT,
    num_tags INT,
    text_length INT
)
""")

# Inserting into table
for _, row in df_filtered.iterrows():
    cursor.execute("""
        INSERT INTO quotes (text, author, tags, num_tags, text_length)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        row['text'],
        row['author'],
        ','.join(row['tags']),
        row['num_tags'],
        int(row['text_length'])
    ))

conn.commit()
cursor.close()
conn.close()
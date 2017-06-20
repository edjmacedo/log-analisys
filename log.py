#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

def get_most_popular_articles():
    db_cursor.execute("""
                        SELECT
                          slug,
                          count(log.path)
                        AS
                          sum
                        FROM
                          articles,
                          log
                        WHERE
                          log.path = '/article/'
                        ||
                          articles.slug
                        GROUP BY
                          articles.slug
                        ORDER BY
                          sum
                        DESC LIMIT 3;
                        """)
    return db_cursor.fetchall()


DBNAME = "news"
db_connection = psycopg2.connect(database=DBNAME)
db_cursor = db_connection.cursor()

print("What are the most popular three articles of all time?")
most_popular_articles = get_most_popular_articles()
for i in most_popular_articles:
    print('"{}" — {} views'.format(i[0], i[1]))

db_connection.close()

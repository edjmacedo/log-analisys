#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

# get the three most popular article
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

# get the most article author of all time
def get_most_popular_author():
    db_cursor.execute("""
                        SELECT
                          authors.name,
                          count(log.path) as views
                        FROM
                          articles,
                          authors,
                          log
                        WHERE
                          log.path=CONCAT('/article/', articles.slug)
                        AND
                          articles.author=authors.id
                        GROUP BY
                          authors.id
                        ORDER BY
                          views
                        DESC
                        """)
    return db_cursor.fetchall()

# Get error request
def get_error_requested():
    db_cursor.execute("""
                        SELECT
                          TO_CHAR(DATE(time), 'Mon DD, YYYY') as date,
                          ROUND(COUNT(CASE WHEN status!='200 OK' THEN 1 END)
                          *100.0/COUNT(status), 2) as p_err
                        FROM
                          log
                        GROUP BY
                          date(time)
                        HAVING
                          (COUNT(CASE WHEN status!='200 OK' THEN 1 END)
                           *100.0/COUNT(status))>1
                        ORDER BY
                          p_err DESC
                        """)
    return db_cursor.fetchall()

# Database connection
DBNAME = "news"
db_connection = psycopg2.connect(database=DBNAME)
db_cursor = db_connection.cursor()

# Question 1
print("What are the most popular three articles of all time?")
most_popular_articles = get_most_popular_articles()
for i in most_popular_articles:
    print('"{}" — {} views'.format(i[0], i[1]))

# Question 2
print("Who are the most popular article authors of all time?")
most_popular_author = get_most_popular_author()
for i in most_popular_author:
    print('"{}" — {} views'.format(i[0], i[1]))

# Question 3
print("On which days did more than 1% of requests lead to errors?")
error_requested = get_error_requested()
for i in error_requested:
    print('"{}" — {} %'.format(i[0], i[1]))

# Close database connection
db_connection.close()

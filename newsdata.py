#!/usr/bin/env python

# Import DB library we are using
import psycopg2


# What are the most popular three articles of all time?
Q1_title = ("What are the most popular three articles of all time?")
Q1 = (
    "select articles.title, count(*) as views "
    "from articles inner join log on log.path "
    "like concat('%', articles.slug, '%') "
    "where log.status like '%200%' group by "
    "articles.title, log.path order by views desc limit 3")

# Who are the most popular article authors of all time?
Q2_title = ("Who are the most popular article authors of all time?")
Q2 = (
    "select authors.name, count(*) as views from articles inner "
    "join authors on articles.author = authors.id inner join log "
    "on log.path like concat('%', articles.slug, '%') where "
    "log.status like '%200%' group "
    "by authors.name order by views desc")

# On which days did more than 1% of requests lead to errors
Q3_title = ("On which days did more than 1% of requests lead to errors?")
Q3 = (
    "select day, perc from ("
    "select day, round((sum(requests)/(select count(*) from log where "
    "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
    "perc from (select substring(cast(log.time as text), 0, 11) as day, "
    "count(*) as requests from log where status like '%404%' group by day)"
    "as log_percentage group by day order by perc desc) as final_query "
    "where perc >= 1")


def connect(database_name="news"):
    """Connect to the PostgreSQL database. Returns a database connection """
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print ("Unable to connect to the database")


def get_query_results(query):
    """Return query results"""
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


def print_query_results(query_results):
    """Format how Q1 & Q2 results will display"""
    print (query_results[1])
    for index, results in enumerate(query_results[0]):
        print (
            "\t", index+1, ' ', results[0],
            "\t - ", str(results[1]), "views")


def print_error_results(query_results):
    """Format how Q3 results display"""
    print (query_results[1])
    for results in query_results[0]:
        print ("\t", results[0], ' ', str(results[1]) + "% errors")


if __name__ == '__main__':
    # Storing query results
    articles_results = get_query_results(Q1), Q1_title
    authors_results = get_query_results(Q2), Q2_title
    error_days = get_query_results(Q3), Q3_title

    # Printing query results
    print_query_results(articles_results)
    print_query_results(authors_results)
    print_error_results(error_days)

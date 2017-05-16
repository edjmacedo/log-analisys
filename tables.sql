Authors
name | bio | id

Articles
author | title | slug | lead | body | time | id

log
path | ip | method | status | time | id



First question:

select articles.slug, articles.title, authors.name from authors, articles where authors.id = articles.author;

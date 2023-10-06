# IDS Mini Project 5: CRUD Operations with SQLite

#### By Daniel Medina
![ccid workflow](https://github.com/medinardaniel/ids706-miniproj-5/actions/workflows/cicd.yml/badge.svg)

## Project Description
In this project, I created a MySQL database hosted in Azure. I obtained soccer league data in the form of csv files
from GitHub to then connect to the Azure database server and create two tables. I apply a complex SQL query to get
the total number of yellow cards among teams from the English Premier League and Spanish League in the 2018-2019
season.

## Explanation of the SQL query

This SQL query is retrieving the top 10 teams with the highest number of home yellow cards from the laliga and epl tables. Here's a step-by-step explanation of what the query is doing:

The query starts by selecting the HomeTeam column and the sum of the home_yellow_cards column from a subquery called all_teams.
The all_teams subquery is created by combining the HomeTeam and home_yellow_cards columns from the laliga and epl tables using the UNION ALL clause. This creates a single table that contains all the home teams and their corresponding yellow cards from both leagues.
The GROUP BY clause groups the results by the HomeTeam column, so that the sum of the yellow cards is calculated for each team.
The ORDER BY clause sorts the results in descending order based on the total number of home yellow cards.
The LIMIT clause limits the results to the top 10 teams with the highest number of home yellow cards.
In summary, this query retrieves the top 10 teams with the highest number of home yellow cards by combining the laliga and epl tables, grouping the results by team, and sorting the results by the total number of home yellow cards.


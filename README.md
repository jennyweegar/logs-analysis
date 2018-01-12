# Logs-Analysis
Project #3 for FSND Udacity

## About
This is the third project for the Udacity Full Stack Nanodegree. In this project we used a live database with over a million rows to explore refine and build complex SQL queries to draw relevant business conclusions from the data. The project mimics building an internal reporting tool for a newpaper site to discover what kind of articles the site's readers enjoy. Building informative summaries from logs is a practical task that often comes up in the web dev world. The database contains newspaper articles, as well as the web server log for the site.

## The Questions
1.) What are the most popular three articles of all time? <br>
2.) Who are the most popular article authors of all time? <br>
3.) On which days did more than 1% of requests lead to errors? <br>

## Materials Needed <br>
Python 3: https://www.python.org/downloads/ <br>
Vagrant: https://www.vagrantup.com/downloads.html <br>
Viewbox: https://www.virtualbox.org/wiki/Download_Old_Builds_5_1 <br>

## How To Run This Program <br>
You will need to download all materials listed above. Once downloaded clone this repository to your machine. Launch Vagrant VM by running ```vagrant up``` in your terminal (this may take quite a long time to run) and then logon to Vagrant with ```vagrant ssh```.

Next, download the [sql file needed to run the query here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Move this file into the vagrant directory, which is shared with your virtual machine.

Load the data needed by running the command ```psql -d news -f newsdata.sql``` to connect to the database. Take a look around the files and tables in tthis shared directory. Once you have browsed the files and are ready to run the program <br>```cd /vagrant``` to change directories into the vagrant directory.

Finally run ```python newsdata.py``` to commence the query and run the program. <br>
The results of the three questions will be printed out in plain text in your terminal.

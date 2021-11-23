#!/bin/bash 

# How many requests were there from each ip?

#awk '{print $1}' ~/SSA/apache_logs.txt | sort | uniq -c | sort -gr | head -n 100

less ~/SSA/apache_logs.txt | sort | cut -d' ' -f1 | uniq -c  | sort -gr




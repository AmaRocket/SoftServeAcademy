#!/bin/bash

# What is the most requested page?

awk '{print $7}' ~/SSA/apache_logs.txt | sort | uniq -c | sort -gr | head -n 1


# '{print $7}' 7 - colmn with pages



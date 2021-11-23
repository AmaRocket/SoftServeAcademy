#!/bin/bash

# What time did site get the most requests?

awk '{print $4}' ~/SSA/apache_logs.txt | uniq -c | sort -gr | head -n 10

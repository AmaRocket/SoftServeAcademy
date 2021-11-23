#!/bin/bash

# What search bots have accessed the site? (UA + IP)

awk '{print $15}' ~/SSA/apache_logs.txt | grep bot | uniq -c | sort -gr | tr -d + | head -n 5| sed -e 's/^.\{,3\}//;s/.\{,3\}$//'


# grep bot - seach pattern in 15th colmn
# tr -d +  - separate symbol "+"  in beetween of address bot
# sed -e... - delete last symbols in address

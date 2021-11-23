#!/bin/bash

# What non-existent pages were clients referred to?

#grep '302' ~/SSA/apache_logs.txt | awk '{print $7}' | uniq -c| head -n 1 


grep '302' ~/SSA/apache_logs.txt  |awk '{print $7}'| sort | uniq -c 





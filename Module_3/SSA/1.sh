#!/bin/bash

# From which ip were the most requests?

awk '{print $1}' ~/SSA/apache_logs.txt | sort | uniq -c | sort -gr | head -n 1 

# Команда awk находит и заменяет текст в файлах по заданному шаблону 

# sort -gr — отсортируем строки (покажет список с самого большого (нужно для корректной работы следующей команды)

# uniq -c — покажем уникальные строки + подсчитаем количествово вхождений этих строк (флаг -с)

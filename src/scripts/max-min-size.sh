#!/bin/bash

file_name=input
max_size_line=0
min_size_line=0
owner_max_size=0
owner_min_size=0

find_max(){
    echo "Executing find max size column"
    while IFS= read -r line; do
    size_line=$(echo $line | awk '{print $5}')
    if [ $size_line -gt $max_size_line ]; then
        max_size_line=$size_line
        owner_max_size=$line
    fi
    done < $file_name
    echo $owner_max_size
}

find_min(){
    echo "Executing find min size column"
    while IFS= read -r line; do
    size_line=$(echo $line | awk '{print $5}')
    if [ $min_size_line -eq 0 ]; then
        min_size_line=$size_line
        owner_min_size=$line
    fi
    if [ $size_line -lt $min_size_line ]; then
        min_size_line=$size_line
        owner_min_size=$line
    fi
    done < $file_name
    echo $owner_min_size
}

if [ $# -gt 0 ]; then
    if [ $1 == "-min" ]; then
        find_min
    else
        echo "Wrong args! $1 is unknow as args."
    fi
else
    find_max
fi

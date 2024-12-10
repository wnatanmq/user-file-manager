#!/bin/bash

file_name=input

if [ $# -gt 0 ]; then
    if [ $1 = "-desc" ]; then
        sorted_name=$(sort input -r)
        printf "%s\n" "${sorted_name}"
    else
        echo "the following $1 is a unknow arg."
    fi
else
    sorted_name=$(sort input)
    printf "%s\n" "${sorted_name}"
fi

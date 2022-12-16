#!/bin/bash
read -p "Enter year to generate files for: " folder
for i in {2..25}
  do 
     touch "${folder}/D${i}P1.py"
     touch "${folder}/D${i}P2.py"
done

#!/bin/zsh

list=$(find $1 -type f -name "*.jpeg");
# echo $list
# loop through the items in the list
list=("${(f)list}")

for file in $list;
do 
echo "Processing $file"
exiftool -all= "$file";
done

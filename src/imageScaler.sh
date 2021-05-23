#!/bin/zsh

# find all the images in given directory
list=$(find $1 -type f -name "*.jpeg");
list=("${(f)list}");

# get list of all sub directories
dlist=$(ls -d $1*/)
dlist=("${(f)dlist}")

# size directories
slist=('1200' '1600' '200' '400' '600' '800')

# make those directories in the different image size directories
for sdir in $slist
do
    for dir in $dlist
    do
        echo "Making directory $sdir in $dir"
        # mkdir ../$sdir/$dir
    done
done
# # loop list > scale image > store scaled image in appropriate directory
# for file in $list;
# do 
# echo "Processing $file"
# # find output path
# done
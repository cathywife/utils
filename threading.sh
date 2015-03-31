#!/bin/bash


thread_num=200


tmp_fifo_file=/tmp/$$.fifo
mkfifo $tmp_fifo_file
exec 7<>$tmp_fifo_file
rm -f $tmp_fifo_file


for (( i=0;i<$thread_num;i++ ));do
    echo ""
done >&7


for ip in $iplist
do
    read -u7
    {
    #######################################
    ##########srcipt by yourself###########
    #######################################
    echo "" >&7
    }&
done
wait
exec 7>&-

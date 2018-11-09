#!/bin/bash

# 监听硬盘

# 参数
watch="/dev/sda2" # 监听硬盘盘符
warningLimit=80 # 触发监听百分比
interval=$[60*60] # 监控间隔

# 处理
while true
do
    percent=`df -h | grep $watch | awk '{print $5}'`
    percent=${percent:0:${#percent}-1}
    if [ $percent -gt 80 ]; then
        (echo "[`date`]硬盘${watch}当前占用${percent}%,超过警戒线${warningLimit}%"; sleep 1) | telnet 192.168.119.187 9999 > /dev/null 2>&1
    fi
    sleep $interval
done

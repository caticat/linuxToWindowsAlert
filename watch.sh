#!/bin/bash

# 监听硬盘

# 参数
watch="/dev/sda2" # 监听硬盘盘符
warningLimit=80 # 触发监听百分比
interval=$[60*60] # 监控间隔
ip="192.168.119.187"
port=9999

# 处理
lastWarningPercent=0 # 保证不会因为同一个百分比连续不断的弹框
while true
do
    percent=`df -h | grep $watch | awk '{print $5}'`
    percent=${percent:0:${#percent}-1}
    if [ $percent -gt $warningLimit ]; then
    	if [ $percent -gt $lastWarningPercent ]; then
        	(echo "[`date`]硬盘${watch}当前占用${percent}%,超过警戒线${warningLimit}%"; sleep 1) | telnet $ip $port > /dev/null 2>&1
        fi
    fi
    lastWarningPercent=$percent
    sleep $interval
done

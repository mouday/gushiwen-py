#!/bin/bash

# created by Peng Shiyu
# at 2021-03-10
# 生成 service
# 依赖：
# $ pip install pycase
# use eg:
# $ bash create_service.sh <table_name>

#############################
# 生成service
#############################
table_name=$1

base_dir='gushiwen/service'
service_filename="${base_dir}/${table_name}_service.py"

# 如果存在就不覆盖
if [ -e $service_filename ]; then
    echo "service_filename exists: ${service_filename}"
    exit 0
fi

class_name=`pycase ${table_name}`

cat template/service.tpl \
| sed -e "s/<class_name>/${class_name}/" \
| sed -e "s/<table_name>/${table_name}/" \
> $service_filename;
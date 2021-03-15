
本项目旨在学习Python Web技术栈，仿照[古诗文网](https://www.gushiwen.cn/)做的测试站点

## 启动

```bash
# clone项目
git clone https://github.com/mouday/gushiwen-py.git

# 安装依赖
pip install -r requirements.txt

# 手动创建数据表
python -m script create_tables

# 启动开发环境
python dev.py

# or 启动生产环境
python main.py
```

## 主要用到的库

- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
- jinja: [https://jinja.palletsprojects.com/](https://jinja.palletsprojects.com/)
- peewee: [http://docs.peewee-orm.com/](http://docs.peewee-orm.com/) 

## 预览地址：

[https://8a7pui.deta.dev/](https://8a7pui.deta.dev/)

手动更新测试数据: [https://8a7pui.deta.dev/update-data](https://8a7pui.deta.dev/update-data)

## 开发工具增强

使用脚本生成Service文件
```bash
python -m script gen service new_table_name

# 或者
python -m script gen --file_type=service --file_name=new_table_name
```

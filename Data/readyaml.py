# 读取 yaml 文件
import yaml

with open("data2.yaml", "r",encoding="utf-8")as f:
    data = yaml.safe_load(f)
    print("输出的数据：", data)
    print("输出的类型：", type(data))

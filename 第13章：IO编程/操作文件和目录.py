import os
'''
#print(os.name) # 操作系统类型
print(os.uname())
print(os.environ) # 所有环境变量
print(os.environ.get('PATH')) # 获取指定的环境变量
'''

# 文件/目录操作
abs_path = os.path.abspath('.') # 当前目录的绝对路径
print('当前目录的绝对路径：%s' % abs_path)

new_path = os.path.join('/tmp', 'foobar') # 组成完整路径
os.mkdir(new_path) # 创建目录
print('已创建目录：%s' % new_path)
os.rmdir(new_path) # 删除目录
print('已删除目录：%s' % new_path)

pyfiles = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(pyfiles)

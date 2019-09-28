from PIL import Image
import os, sys, time, show_process


### 开场白
print('-'*80)
print(' '*10 +'本程序用于类似微信头像加国旗功能.' + ' '*10)
print('\n请将头像 和 背景 与本程序放在同一目录下，比如同时存放在桌面。\n')
print('by 阿甘 ^-^')
print('-'*80)

# 读取图片
# 获取于当前程序存放在同一目录下的文件绝对路径 
head_name = input('>>>请输入头像的文件名(请加上后缀名)：') 
head_address = '%s\\'%os.getcwd() + head_name# 获取于当前程序存放在同一目录下的文件绝对路径 
flag_name = input('>>>请输入背景图片的名称(请加上后缀名)：') 
flag_address = '%s\\'%os.getcwd() + flag_name

flag = Image.open(flag_address)
head = Image.open(head_address)

# 计算缩放比列
ratio = head.width/flag.width/4
size = (int(flag.width*ratio), int(flag.height*ratio))

# 缩放国旗图片
flag = flag.resize(size, Image.ANTIALIAS)

# 计算坐标
position = (head.width-flag.width, head.height-flag.height)

# 合成图片 并保存
head.paste(flag, position)
head.save('%s\\'%os.getcwd() + "add_flag.jpg", 'jpeg')

## 显示进度
max_steps = 100
process_bar = show_process.ShowProcess(max_steps, 'OK')
for i in range(max_steps):
    process_bar.show_process()
    time.sleep(0.01)


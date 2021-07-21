# -*- coding: utf-8 -*-

"""
Copyright () 2020

All rights reserved

FILE: image_word.py
AUTHOR: tianyuningmou
DATE CREATED:  @Time : 2021/7/20 10:16 上午

DESCRIPTION:  .

VERSION: : #1 
CHANGED By: : tianyuningmou
CHANGE:  : 
MODIFIED: : @Time : 2021/7/20 10:16 上午
"""

from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (50, 50), "yellow")
draw_table = ImageDraw.Draw(im=image)
draw_table.text(xy=(5, 15), text=u'王璐', fill='#000000', font=ImageFont.truetype('Hiragino Sans GB.ttc', 20))

image.show()  # 直接显示图片
# image.save('天宇.png', 'PNG')  # 保存在当前路径下，格式为PNG
# image.close()

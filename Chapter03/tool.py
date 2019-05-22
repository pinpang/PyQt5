# -*- coding: utf-8 -*-

'''
    【简介】
	ui转换成py的转换工具
     
'''

import os 
# import os.path 

# UI文件所在的路径 
root = './'  # 不使用与内置函数同名的变量命名

# 列出目录下的所有ui文件
def listUiFile():
	return [f for f in os.listdir(root) if f.endswith('.ui')]
	# 如果文件数量巨大，考虑使用下面的生成器作为返回值
	# return (f for f in os.listdir(root) if f.endswith('.ui'))


# 把后缀为ui的文件改成后缀为py的文件名	
def transPyFile(filename): 
	return os.path.splitext(filename)[0] + '.py' 

# 调用系统命令把ui转换成py
def runMain():
	uiList = listUiFile()
	for uifile in uiList :
		pyfile = transPyFile(uifile)
		cmd = 'pyuic5 -o {pyfile} {uifile}'.format(pyfile=pyfile,uifile=uifile)  
		#print(cmd)
		os.system(cmd)

###### 程序的主入口		
if __name__ == "__main__":  	
	runMain()

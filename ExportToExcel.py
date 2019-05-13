import os
import csv

pic_folder = input("请输入保存图片的文件夹路径：")
out = open("pictureListOutput.csv",'a',newline='')
csv_write = csv.writer(out)
for path,childpath,files in os.walk(pic_folder):
    for i in range(len(files)):
        if files[i][-3:] == 'jpg' or  files[i][-3:] == 'JPG' or files[i][-3:] == 'png' or files[i][-3:] == 'PNG':
            list = str(files[i])
            csv_write.writerow([files[i]])

print("写入完成")
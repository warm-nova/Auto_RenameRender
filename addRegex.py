import os
import csv
import re, os, fnmatch

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def find_continuous_num(astr, c):
    num = ''
    try:
        while not is_number(astr[c]) and c < len(astr):
            c += 1
        while is_number(astr[c]) and c < len(astr):
            num += astr[c]
            c += 1
    except:
        pass
    if num != '':
        return int(num)


def comp2filename(file1, file2):
    smaller_length = min(len(file1), len(file2))
    continuous_num = ''
    for c in range(0, smaller_length):
        if not is_number(file1[c]) and not is_number(file2[c]):
            # print('both not number')
            if file1[c] < file2[c]:
                return True
            if file1[c] > file2[c]:
                return False
            if file1[c] == file2[c]:
                if c == smaller_length - 1:
                    # print('the last bit')
                    if len(file1) < len(file2):
                        return True
                    else:
                        return False
                else:
                    continue
        if is_number(file1[c]) and not is_number(file2[c]):
            return True
        if not is_number(file1[c]) and is_number(file2[c]):
            return False
        if is_number(file1[c]) and is_number(file2[c]):
            if find_continuous_num(file1, c) < find_continuous_num(file2, c):
                return True
            else:
                return False
    # if file1 < file2:
    #     return True
    # else:
    #     return False


def sort_insert(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j > 0 and lst[j - 1] > x:
            # while j > 0 and comp2filename(x, lst[j-1]):
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = x
    return lst


def sort_insert_filename(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        # while j > 0 and lst[j-1] > x:
        while j > 0 and comp2filename(x, lst[j - 1]):
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = x
    return lst


def file_name_sort(all_file_list):
    new_list = []
    # all_file_list.sort(key=lambda x: int(x.split('.')[0].split('_')[2]))
    # for file in all_file_list:
    #     pass

    return new_list


pic_folder = input("请输入原图片所在的文件夹路径：")
output_folder = input("请输入渲染图的文件夹路径，保证图片相对顺序相同：")

pics=[]

pics = os.listdir(pic_folder)
sorted_yuantu = sort_insert_filename(pics)
print(sorted_yuantu)

#改名成按数字
render_pics = os.listdir(output_folder)
for i in range(len(render_pics)):
    temp = str(render_pics[i])
    s = re.findall(r'\((.*?)\)', temp)
    try:
        os.rename(os.path.join(output_folder,temp),os.path.join(output_folder,s[0]))
    except:
        print("请保证您的文件名是:字母(数字)  如：17zuoye(1).jpg的格式,才能进行提取")
        break

final_output_pics = os.listdir(output_folder)
sorted_final = sort_insert_filename(final_output_pics)
print(sorted_final)
for i in range(len(sorted_final)):
    os.rename(os.path.join(output_folder,sorted_final[i]),os.path.join(output_folder,sorted_yuantu[i]))



select_regex = input("文件名写入完成，是否要修改后缀（Y/N）")
if select_regex=="Y" or select_regex=='y':
    inputreg = input("请输入要添加的后缀:")
    for path, childpath, files in os.walk(output_folder):
        for i in range(len(files)):
            filesNewName = files[i][:-4] + inputreg + files[i][-4:]
            os.rename(os.path.join(output_folder,files[i]),os.path.join(output_folder,filesNewName))
else:
    print("程序结束.")
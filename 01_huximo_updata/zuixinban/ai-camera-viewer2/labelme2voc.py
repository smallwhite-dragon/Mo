import os
import cv2
import json
import codecs
import shutil
import random
import numpy as np

from glob import glob

# 标签路径E:\aeg-paddle\huximo_photos\4821
labelme_path = "E:/aeg-paddle/led_photos/DME004/"  # 原始labelme标注数据路径
saved_path = "E:/aeg-paddle/save_voc/DME004_voc/"  # 保存路径

# 设定验证集大小
split_num = 360

# 创建要求文件夹
if not os.path.exists(saved_path + "Annotations"):
    os.makedirs(saved_path + "Annotations")
if not os.path.exists(saved_path + "JPEGImages/"):
    os.makedirs(saved_path + "JPEGImages/")
if not os.path.exists(saved_path + "ImageSets/Main/"):
    os.makedirs(saved_path + "ImageSets/Main/")

# 获取待处理文件
files = glob(labelme_path + "*.json")
files = [i[:-5] for i in files]
label_list = []

# 读取标注信息并写入 xml
for json_file_ in files:
    json_filename = json_file_ + ".json"
    json_file = json.load(open(json_filename, "r", encoding="utf-8"))
    height, width, channels = cv2.imread(json_file_ + ".jpg").shape
    with codecs.open(saved_path + "Annotations/"+json_file_.split('\\')[-1] + ".xml", "w", "utf-8") as xml:
        xml.write('<annotation>\n')
        xml.write('\t<folder>' + 'UAV_data' + '</folder>\n')
        xml.write('\t<filename>' + json_file_ + ".jpg" + '</filename>\n')
        xml.write('\t<source>\n')
        xml.write('\t\t<database>The UAV autolanding</database>\n')
        xml.write('\t\t<annotation>UAV AutoLanding</annotation>\n')
        xml.write('\t\t<image>flickr</image>\n')
        xml.write('\t\t<flickrid>NULL</flickrid>\n')
        xml.write('\t</source>\n')
        xml.write('\t<owner>\n')
        xml.write('\t\t<flickrid>NULL</flickrid>\n')
        xml.write('\t\t<name>ChaojieZhu</name>\n')
        xml.write('\t</owner>\n')
        xml.write('\t<size>\n')
        xml.write('\t\t<width>' + str(width) + '</width>\n')
        xml.write('\t\t<height>' + str(height) + '</height>\n')
        xml.write('\t\t<depth>' + str(channels) + '</depth>\n')
        xml.write('\t</size>\n')
        xml.write('\t\t<segmented>0</segmented>\n')
        for multi in json_file["shapes"]:
            points = np.array(multi["points"])
            xmin = min(points[:, 0])
            xmax = max(points[:, 0])
            ymin = min(points[:, 1])
            ymax = max(points[:, 1])
            label = multi["label"]
            # # /--4820系列
            # if str(label).endswith('-hxm'):
            #     xmin = max(xmin-5, 0)
            #     ymin = max(ymin-5, 0)
            #     xmax = min(xmax+5, 640)
            #     ymax = min(ymax+5, 480)
            #     label = '4820-hxm'
            # else:
            #     label = '4820'
            # # --/
            if label not in label_list:
                label_list.append(label)
            if xmax <= xmin:
                pass
            elif ymax <= ymin:
                pass
            else:
                xml.write('\t<object>\n')
                xml.write('\t\t<name>'+label+'</name>\n')
                xml.write('\t\t<pose>Unspecified</pose>\n')
                xml.write('\t\t<truncated>1</truncated>\n')
                xml.write('\t\t<difficult>0</difficult>\n')
                xml.write('\t\t<bndbox>\n')
                xml.write('\t\t\t<xmin>' + str(xmin) + '</xmin>\n')
                xml.write('\t\t\t<ymin>' + str(ymin) + '</ymin>\n')
                xml.write('\t\t\t<xmax>' + str(xmax) + '</xmax>\n')
                xml.write('\t\t\t<ymax>' + str(ymax) + '</ymax>\n')
                xml.write('\t\t</bndbox>\n')
                xml.write('\t</object>\n')
                print(json_filename, xmin, ymin, xmax, ymax, label)
        xml.write('</annotation>')


# 复制图片到 VOC2007/JPEGImages/下
image_files = glob(labelme_path + "*.jpg")
print("copy image files to VOC007/JPEGImages/")
for image in image_files:
    shutil.copy(image, saved_path + "JPEGImages/")

# 生成 label list 文件
with open(os.path.join(saved_path, 'label_list.txt'), 'w') as f:
    for label in label_list:
        f.write(label+'\n')


# 读取数据列表
imgs = os.listdir(os.path.join(saved_path, 'JPEGImages'))
datas = ['JPEGImages/%s Annotations/%s\n' %
         (img, img[:-4]+'.xml') for img in imgs]

# 打乱
random.shuffle(datas)

# 写入文件
with open(os.path.join(saved_path, 'train_list.txt'), 'w') as f:
    for line in datas[:-split_num]:
        f.write(line)
with open(os.path.join(saved_path, 'val_list.txt'), 'w') as f:
    for line in datas[-split_num:]:
        f.write(line)

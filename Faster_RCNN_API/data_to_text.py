import csv
import os
import numpy as np
from shutil import copy2,rmtree
list_map=[
    ('01','bg'),
    ('02','bg'),
    ('03','shuangxing?'),
    ('04','bg'),
    ('05','bg'),
    ('06','bg'),
    ('07','bg'),
    ('08','bg'),
    ('09','bg'),
    ('10','bg'),
    ('11','bg'),
    ('12','Stop'),
    ('13','bg'),
    ('14','bg'),
]
dict_map = dict(list_map)

def get_txt_from_folder(new_txt,path):
    for folder in os.listdir(path):
        if 'label' in folder:
            # label files folder.
            label_folder_full_path = os.path.join(path,folder)
            for label_txt in os.listdir(label_folder_full_path):
                # get video number
                print(label_txt)
                basename = os.path.basename(os.path.join(label_folder_full_path,label_txt))
                video_number = basename.split('.')[0]
                with open(new_txt,'a+') as f:
                    writer = csv.writer(f)
                    with open(file = os.path.join(label_folder_full_path,label_txt),mode = 'r+') as txt_file:
                        reader = csv.reader(txt_file,delimiter = '_')
                        # Skip the header
                        next(reader)
                        for line in reader:
                            # Get useful information
                            frame_num = line[0]
                            cls = line[1]
                            llx = line[2]
                            lly = line[3]
                            urx = line[-2]
                            ury = line[-1]
                            # write to new file
                            new_line=[]
                            #TODO:image folder path 'imgs' should be changed as your need, This is not pythonic.
                            img_dir = os.path.join(path,'img')
                            frame_num = int(frame_num)
                            img_basename=video_number+'_'+str(frame_num)+'.png'
                            img_path=os.path.join(img_dir,img_basename)
                            new_line.append(img_path)
                            new_line.append(llx)
                            new_line.append(lly)
                            new_line.append(urx)
                            new_line.append(ury)
                            real_class = dict_map.get(cls)
                            new_line.append(real_class)
                            writer.writerow(new_line)
def mkdir_if_not_exists(fullpath):
    if not os.path.exists(fullpath):
        os.makedirs(fullpath)

def split_files_into_corresponding_folders(original_label_folder,new_folder,img_folder,ratio=0.8):
    # Create folders.
    train_folder = os.path.join(new_folder,'train')
    valid_folder = os.path.join(new_folder, 'valid')
    train_label_path = os.path.join(train_folder,'label')
    valid_label_path = os.path.join(valid_folder,'label')
    train_img_path = os.path.join(train_folder,'img')
    valid_img_path = os.path.join(valid_folder,'img')
    mkdir_if_not_exists(train_label_path)
    mkdir_if_not_exists(valid_label_path)
    mkdir_if_not_exists(train_img_path)
    mkdir_if_not_exists(valid_img_path)

    # Random split the train and valid for label folder.
    original_list = os.listdir(original_label_folder)
    number = len(original_list)
    num_train_split = int(np.floor(number * ratio))
    np.random.shuffle(original_list)
    train_labels_txt_list=original_list[0:num_train_split]
    valid_labels_txt_list=original_list[num_train_split:-1]
    dst = train_label_path
    for file_name in train_labels_txt_list:
        full_path = os.path.join(original_label_folder,file_name)
        copy2(full_path,dst)
    dst = valid_label_path
    for file_name in valid_labels_txt_list:
        full_path = os.path.join(original_label_folder,file_name)
        copy2(full_path,dst)
    # Image split
    for file_name in train_labels_txt_list:
        n1,n2 = file_name.split('.')[0].split('_')
        for img_name in os.listdir(img_folder):
            nn1, nn2 = img_name.split('.')[0].split('_')[0:2]
            if  (nn1,nn2)== (n1,n2):
                copy2(os.path.join(img_folder,img_name),train_img_path)

    # Image split
    for file_name in valid_labels_txt_list:
        n1,n2 = file_name.split('.')[0].split('_')
        for img_name in os.listdir(img_folder):
            nn1, nn2 = img_name.split('.')[0].split('_')[0:2]
            if  (nn1,nn2)== (n1,n2):
                copy2(os.path.join(img_folder,img_name),valid_img_path)





if __name__ == '__main__':

    # Only excute once
    # new_folder = '/home/frank/big_Od'
    # rmtree(new_folder)
    # split_files_into_corresponding_folders(original_label_folder='/home/frank/OD/ShoushouCycleGAN/virtual2real/labels/unreal',
    #                                        new_folder=new_folder,
    #                                        img_folder='/home/frank/OD/ShoushouCycleGAN/virtual2real/virtual_img')
    valid_path = '/home/frank/big_Od/valid'
    train_path = '/home/frank/big_Od/train'
    new_txt = '/home/frank/big_Od/new_text.txt'

    get_txt_from_folder(new_txt=new_txt,path=train_path)
    get_txt_from_folder(new_txt=new_txt,path=valid_path)

    # Find that all the 300 frame is missing. So remove them.
    clean_txt = '/home/frank/big_Od/clean_text.txt'
    with open(clean_txt,'w+') as w:
        writer = csv.writer(w)
        with open(new_txt,'r+') as f:
           reader = csv.reader(f)
           for line in reader:
               if '300' not in line[0]:
                   writer.writerow(line)
    # Replace
    clean_txt = '/home/frank/big_Od/clean_text.txt'
    with open(clean_txt,'w+') as w:
        writer = csv.writer(w)
        with open(new_txt,'r+') as f:
           reader = csv.reader(f)
           for line in reader:
               if '300' not in line[0]:
                   writer.writerow(line)



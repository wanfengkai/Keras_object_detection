import csv
import os
#TODO here I only simplely do it twice,
path = '/home/frank/Keras_object_detection/valid'
# path = '/home/frank/Keras_object_detection/train'
new_txt = './new_text.txt'

for folder in os.listdir(path):
    if 'labels' in folder:
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
                        img_dir = os.path.join(path,'imgs')
                        frame_num = int(frame_num)
                        img_basename=video_number+'_'+str(frame_num)+'.png'
                        img_path=os.path.join(img_dir,img_basename)
                        new_line.append(img_path)
                        new_line.append(llx)
                        new_line.append(lly)
                        new_line.append(urx)
                        new_line.append(ury)
                        new_line.append(cls)
                        writer.writerow(new_line)


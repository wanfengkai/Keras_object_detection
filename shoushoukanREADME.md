# Step by Step readme


1. 把所有想要用来做训练以及测试的数据放到一个文件夹中

    eg:
    Assume ***~/TrainA*** and ***~/TestB*** contains all virtual images.
    Want to put them into one folder named **~/Virtual**

    cp ~/TrainA/*  ~/Virtual
    
    cp ~/TestB/*  ~/Virtual

2. cd Faster\_RCNN\_API

    打开 data\_to\_text.py

    根据代码中的注释进行调整。
    只需要修改以下三个参数：
    new\_folder
    
    original\_label\_folder
    
    img\_folder


3. 训练

在train\_frcnn.py文件的最后，把 **train\_path**，  **output\_weight\_path**改为自己定义的即可。

 其中， train_path 就是 **clean\_txt.txt** 的全路径。

 output\_weight\_path 就是 你想要保存的模型的路径 包括其文件名 如: **~/weights/weight1.hdf5**



4.测试

在test\_frcnn.py文件最后的，test\_image\_list 是你唯一需要修改的，把其中的路径指向你想要测试的文件夹即可。



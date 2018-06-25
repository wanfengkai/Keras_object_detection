"""
Configuration file for Faster-RCNN to match original implementation
Present just for legacy. All of the variables can be changed using Train_frcnn() method
"""
import math


class Config:

    def __init__(self):


        self.verbose = True

        # setting for train augmentation
        self.use_horizontal_flips = False
        self.use_vertical_flips = False
        self.rot_90 = False

        # anchor box scales
        self.anchor_box_scales = [128, 256, 512]

        # anchor box ratios
        self.anchor_box_ratios = [[1, 1], [1./math.sqrt(2), 2./math.sqrt(2)], [2./math.sqrt(2), 1./math.sqrt(2)]]

        # size to resize the smallest side of the image
        self.im_size = 600

        self.img_scaling_factor = 1.0

        # number of ROIs at once
        self.num_rois = 32

        # stride at the RPN (this depends on the network configuration)
        self.rpn_stride = 16 #for vgg block5

        self.balanced_classes = False

        # scaling the stdev
        self.std_scaling = 4.0
        self.classifier_regr_std = [8.0, 8.0, 4.0, 4.0]

        # overlaps for RPN
        self.rpn_min_overlap = 0.3
        self.rpn_max_overlap = 0.7

        # overlaps for classifier ROIs
        self.classifier_min_overlap = 0.1
        self.classifier_max_overlap = 0.5
        
        # nms threshold
        self.rpn_nms_threshold = 0.7 # from original implementation code
        self.test_roi_nms_threshold = 0.3 # from original implemtation code (use while testing in the last classifier's output)

        # placeholder for the class mapping, automatically generated by the parser
        self.class_mapping = None
        
        self.weights_all_path = 'model_frcnn.hdf5'
        
        # Number of top scoring boxes to keep before apply NMS to RPN proposals
        self.TRAIN_RPN_PRE_NMS_TOP_N = 12000
        # Number of top scoring boxes to keep after applying NMS to RPN proposals
        self.TRAIN_RPN_POST_NMS_TOP_N = 2000
        
        ## Number of top scoring boxes to keep before apply NMS to RPN proposals
        self.TEST_RPN_PRE_NMS_TOP_N = 6000
        ## Number of top scoring boxes to keep after applying NMS to RPN proposals
        self.TEST_RPN_POST_NMS_TOP_N = 300

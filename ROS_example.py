#!/usr/bin/env python3

import roslib
import sys
import rospy
import cv2
import pyqrcode
import qrcode
import mask_detector
import detect_mask_image
import numpy as np
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError

# call the class
def main(args):
    bridge = CvBridge()
    rospy.init_node('test',anonymous=True)
    qr_code_pub = rospy.Publisher('/service/qrcode',String,queue_size=10)
    mask_pub  = rospy.Publisher('/service/mask',String,queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        qrcode_img = cv2.imread('qr5.jpg',-1)
        
        qr_code_pub.publish(detectQRCode(qrcode_img))
        detect_mask_image()
        #cv_image = cv2.imread('test.png',-1)
        #cv_image = cv2.inRange(cv_image,(200,200,200),(255,255,255))
        #if cv_image != None:
        #cv2.imshow('window',np.array(cv_image,dtype = np.uint8))
        #cv2.waitKey(3)
        #print(np.shape(cv_image),type(cv_image[0][0]))
        #out, bbox,_ = cv2.QRCodeDetector(cv_image)
        #if data:
        #   print("QRCode detected: ", out)
        #print(np.shape(cv_image))
        rate.sleep()
    cv2.destroyAllWindows()

def detectQRCode(img):
        #cv2.imshow('window',cv2.resize(img,(960,540)))
        #cv2.waitKey(3)
        detector = cv2.QRCodeDetector()
        out, data,_ = detector.detectAndDecode(img)
        print(out)
        return out
        


# run the code if the node is called
if __name__ == '__main__':
    main(sys.argv)

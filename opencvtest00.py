# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:23:51 2021

@author: DJ
"""

import cv2
test = cv2.imread("D:\\year3\\SDP\\face-mask-detector\\examples\\example_01.png")
print(test.shape)

cv2.waitKey(0)
cv2.imshow('Amanda', test)
cv2.waitKey(1000)
cv2.destroyAllWindows()
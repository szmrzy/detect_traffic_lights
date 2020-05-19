import cv2
import enum
import imutils
import numpy as np

from scipy.spatial import distance

"""
inspired : https://www.pyimagesearch.com/2016/02/15/determining-object-color-with-opencv/
"""
class Color(enum.Enum):
  Red = 'Red'
  Green = 'Green'
  Other = 'Other'

class ObjectColorDetect:
  def __init__(self):
    self.__colorNames = [Color.Red, Color.Green, Color.Other]
    matrix = np.zeros((len(self.__colorNames), 1, 3), dtype='uint8')
    matrix[0] = (255, 0, 0)
    matrix[1] = (0, 255, 0)
    matrix[2] = (0, 0, 0)
    self.__matrix = cv2.cvtColor(matrix, cv2.COLOR_RGB2LAB)

  def find_color(self, image, contour):
    mask = np.zeros(image.shape[:2], dtype = 'uint8')
    cv2.drawContours(mask, [contour], -1, 255, -1)
    mean = cv2.mean(image, mask = mask)[:3]
    minDist = (np.inf, None)
    for (i, row) in enumerate(self.__matrix):
      dist = distance.euclidean(row[0], mean)
      if dist < minDist[0]:
        minDist = (dist, i)
    return self.__colorNames[minDist[1]]
        
  def detect_color(self, image):  
    #prepare to recognize collor
    resized = imutils.resize(image, height=300, width=300)
    blurredImg = cv2.GaussianBlur(resized, (5, 5), 0)  
    grayImg = cv2.cvtColor(blurredImg, cv2.COLOR_BGR2GRAY)
    # take image tresh; [0] is tresh value = 60
    threshImg = cv2.threshold(grayImg, 60, 255, cv2.THRESH_BINARY)[1] 
    # convert to CIE Lab 
    labImg = cv2.cvtColor(blurredImg, cv2.COLOR_BGR2LAB)
    
    contours = cv2.findContours(threshImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    if contours == []:
      raise Exception('Not detect collored object!')
    colorMap = {}
    for contour in contours:
      color = self.find_color(labImg, contour)
      colorMap[color] = colorMap.get(color, 0) + 1
    color = max(colorMap, key = colorMap.get)
    if color == Color.Other:
      raise Exception('Can not detect color!')
    return color
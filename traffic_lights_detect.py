import cv2
import numpy as np

from object_color import ObjectColorDetect, Color

class TrafficLights:

  def __init__(self, image):
    if isinstance(image, str):
      self.__image = cv2.imread(image)
    elif isinstance(image, np.ndarray):
      self.__image = image
    if self.__image is None:
      raise Exception('Bad initial value')

  def filter_color(self, color: Color):
    hsvImg = cv2.cvtColor(self.__image, cv2.COLOR_BGR2HSV)
    mask, lower, upper = None, None, None
    # prepare mask
    if color == Color.Red:
      lower, upper = (170,120,70), (180,255,255)
      mask = cv2.inRange(hsvImg, lower, upper)
    elif color == Color.Green:
      lower, upper = (36, 25, 25), (86, 255,255)
      mask = cv2.inRange(hsvImg, lower, upper)
    # aply mask 
    hsvImg = cv2.bitwise_and(hsvImg, hsvImg, mask = mask)
    # places with color between mask lower & upper
    return cv2.inRange(hsvImg, lower, upper)

  def detect_shiny(self):
    # change brightnes 
    gama = 2.0
    table = np.array([((i/255.0)**gama) * 255.0 for i in np.arange(0,256)]).astype('uint8')
    lutImg = cv2.LUT(self.__image, table)
    return cv2.bitwise_and(self.__image, lutImg)

  def traffic_light_on(self, color: Color):
    filteredImg = self.filter_color(color)
    filteredImg = cv2.cvtColor(filteredImg, cv2.COLOR_GRAY2BGR)
    return cv2.bitwise_and(filteredImg, self.detect_shiny())

  def get_image(self):
    return self.__image

def main():
  trafficLights = None
  colorToDetect = Color.Red
  cbjectColorDetect = ObjectColorDetect()
  img = 'img\\'
  names = ['lights1.png','lights2.png','lights3.png','lights4.png','lights5.png','lights6.png','giraffe.png']
  for name in names:
    imgOrg = cv2.imread(img + name)
    try:
      trafficLights = TrafficLights(imgOrg)
    except Exception as e:
      print(e)
    image = trafficLights.traffic_light_on(colorToDetect)
    try:
      color = cbjectColorDetect.detect_color(image)
      print(f"Detect {color.value} color!")
    except Exception as e:
        print(e)

    cv2.imshow('Image orginal', imgOrg)
    cv2.imshow('After detect',  image)
    cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == "__main__":
  main()

import cv2
import numpy as np
import unittest
from traffic_lights_detect import * 
from object_color import *

class TestTrafficLights(unittest.TestCase): 

  def test_get_image_is_same(self):
    trafficLights = TrafficLights('img\giraffe.png')
    expected = cv2.imread('img\giraffe.png')
    self.assertTrue(np.all(expected == trafficLights.get_image()))

  def test_get_image_is_different(self):
    trafficLights = TrafficLights('img\lights1.png')
    expected = cv2.imread('img\giraffe.png')
    self.assertFalse(np.all(expected == trafficLights.get_image()))

  def test_initialize_str(self):
    trafficLights = TrafficLights('img\lights1.png')
    expected = cv2.imread('img\lights1.png')
    self.assertTrue(np.all(expected == trafficLights.get_image()))

  def test_initialize_ndarray(self):
    expected = cv2.imread('img\lights1.png')
    trafficLights = TrafficLights(expected)
    self.assertTrue(np.all(expected == trafficLights.get_image()))

  def test_initialize_bad_type(self):
    badType = list()
    self.assertRaises(Exception, TrafficLights, badType)

  def test_initialize_cannot_init(self):
    self.assertRaises(Exception, TrafficLights, 'bad_image_name')

  def test_traffic_lights_1_red(self):
    trafficLights = TrafficLights('img\lights1.png')
    image = trafficLights.traffic_light_on(Color.Red)
    self.assertEqual(Color.Red, ObjectColorDetect().detect_color(image))

  def test_traffic_lights_1_green(self):
    trafficLights = TrafficLights('img\lights1.png')
    image = trafficLights.traffic_light_on(Color.Green)
    self.assertRaises(Exception, ObjectColorDetect().detect_color, image)

  def test_traffic_lights_2_red(self):
    trafficLights = TrafficLights('img\lights2.png')
    image = trafficLights.traffic_light_on(Color.Red)
    self.assertRaises(Exception, ObjectColorDetect().detect_color, image)

  def test_traffic_lights_2_green(self):
    trafficLights = TrafficLights('img\lights2.png')
    image = trafficLights.traffic_light_on(Color.Green)
    self.assertRaises(Exception, ObjectColorDetect().detect_color, image)

  def test_traffic_lights_3_red(self):
    trafficLights = TrafficLights('img\lights3.png')
    image = trafficLights.traffic_light_on(Color.Red)
    self.assertRaises(Exception, ObjectColorDetect().detect_color, image)

  def test_traffic_lights_3_green(self):
    trafficLights = TrafficLights('img\lights3.png')
    image = trafficLights.traffic_light_on(Color.Green)
    self.assertEqual(Color.Green, ObjectColorDetect().detect_color(image))

  def test_traffic_lights_4_red(self):
    trafficLights = TrafficLights('img\lights4.png')
    image = trafficLights.traffic_light_on(Color.Red)
    self.assertEqual(Color.Red, ObjectColorDetect().detect_color(image))

  def test_traffic_lights_4_green(self):
    trafficLights = TrafficLights('img\lights4.png')
    image = trafficLights.traffic_light_on(Color.Green)
    self.assertRaises(Exception, ObjectColorDetect().detect_color, image)

  def test_traffic_lights_5_red(self):
    trafficLights = TrafficLights('img\lights5.png')
    image = trafficLights.traffic_light_on(Color.Red)
    self.assertRaises(Exception, ObjectColorDetect().detect_color, image)

  def test_traffic_lights_5_green(self):
    trafficLights = TrafficLights('img\lights5.png')
    image = trafficLights.traffic_light_on(Color.Green)
    self.assertEqual(Color.Green, ObjectColorDetect().detect_color(image))

  def test_traffic_lights_6_red(self):
    trafficLights = TrafficLights('img\lights6.png')
    image = trafficLights.traffic_light_on(Color.Red)
    self.assertEqual(Color.Red, ObjectColorDetect().detect_color(image))

  def test_traffic_lights_6_green(self):
    trafficLights = TrafficLights('img\lights6.png')
    image = trafficLights.traffic_light_on(Color.Green)
    self.assertRaises(Exception, ObjectColorDetect().detect_color, image)
    
  def test_detect_red_giraffe(self):
    trafficLights = TrafficLights('img\giraffe.png')
    image = trafficLights.traffic_light_on(Color.Red)
    self.assertRaises(Exception, ObjectColorDetect().detect_color, image)

if __name__ == "__main__":
  unittest.main()
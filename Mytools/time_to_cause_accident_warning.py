# -*- coding: utf-8 -*-
"""time_to_cause_accident & accident_warning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17zSl_BV_PdB186gBmQIMiltuWGI2rpqg

#input speed：km/hr
#input distance：m
"""

def time_to_cause_accident(speed, distance):#, obj_class, friction_coefficient=0.8, reaction_time=0.75):
  speed = speed * 1000 / 3600 #(km/hr to m/s)
  '''
  reaction_distance = reaction_time * speed
  stopping_distance = speed**2 /(2*9.8*friction_coefficient)
  safety_distance = reaction_distance + stopping_distance
  '''
  time = distance/speed
  return time #second


'''
obj_class：  0   1    2  3     5   7
       person bicycle car motorcycle bus truck

bus and truck：safety time >= 3s
else：safety time >= 2s
'''

def accident_warning(obj_class, time):
  if obj_class <= 4:
    if time < 2:
      warning_sign = True
    else:
      warning_sign = False
  else:
    if time < 3:
      warning_sign = True
    else:
      warning_sign = False
  return warning_sign

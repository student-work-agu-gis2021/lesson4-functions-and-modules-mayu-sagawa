#Problem 1
def fahr_to_celsius(temp_fahrenheit):
  """
  purpose: To convert the input temperature from degrees Fahrenheit to degrees Celsius.
  parameters:temp_fahrenheit.
  returned values: converted_temp.
  """
  converted_temp = (temp_fahrenheit-32)/1.8
  return converted_temp

#Problem 2
def temp_classifier(temp_celsius):
  """
  the purpose of function: To reclassify into integer numbers 0-3 based on criteria.
  parameters: temp_celsius.
  returned values: from 0 to 3
  """
  if temp_celsius < -2:
    return 0
  elif (temp_celsius>=-2)and(temp_celsius<2):
    return 1
  elif (temp_celsius>=2)and(temp_celsius<15):
    return 2
  elif temp_celsius>=15:
    return 3

#docstring
"""
 purpose: To classify a dataset of temperatures in Fahrenheit into four different classes.
 parameters: temp_fahrenheit and temp_celsius
 returned values: converted_temp and from 0 to 3
"""
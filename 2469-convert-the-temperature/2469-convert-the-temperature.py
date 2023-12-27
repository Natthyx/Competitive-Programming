class Solution:
    def convertTemperature(self, celsius):
        arr = []
        kelvin = celsius + 273.15
        fahrenheit = celsius* 1.80 + 32.00
        arr.append(kelvin)
        arr.append(fahrenheit)
        return arr

        
        
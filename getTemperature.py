import random 
import string 
import json
from datetime import datetime

contents = []
index = -1

def getTemperature() -> dict:
    # read dataset and convert to list of temperatures
    with open('data/temperature_dataset.txt') as f:
        contents = f.read()
    list_of_metrics = contents.split()

    global index
    index += 1
    
    return {
      'temperature':list_of_metrics[index],
      'time': index,
    }

# only for testing purpose
# if __name__ == '__main__':
#   print(getTemperature())
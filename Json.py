#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Daniel.Karapandov
#
# Created:     05/08/2022
# Copyright:   (c) Daniel.Karapandov 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
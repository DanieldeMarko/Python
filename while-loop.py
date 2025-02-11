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

#With the while loop we can execute a set of statements as long as a condition is true.
i = 0
while i < 10:
  i += 1
  if i == 3:
    continue
  print(i)


  i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
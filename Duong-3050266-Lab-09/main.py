"""
Author: Cody Duong
KUID: 3050266
Date: 2022-11-14
Lab: lab09
Last modified: 2022-11-14
Description: Entry file into lab9
"""


if __name__ == "__main__":
  import os
  from src.Hospital import *

  file_name: str = input("Enter the name of the hospital records file (records.txt): ")
  if file_name == "":
      file_name = "records.txt"
  while not os.path.isfile(file_name):
      # raise ValueError("Invalid file")
      file_name = input("File was not found, please try again (records.txt): ")
      if file_name == "":
          file_name = "records.txt"

  Hospital().run(file_name)
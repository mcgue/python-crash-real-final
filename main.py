# Final project for Crash Course Python on Coursera
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# Get file
file_contents = open(r"dick.txt","r")

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')
    print(file_contents)
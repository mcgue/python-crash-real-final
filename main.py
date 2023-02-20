# Final project for Crash Course Python on Coursera
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
import io
import sys

# Open file and put text into file
with open('moby-dick.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

contents = contents.replace('\n', ' ')
contents = contents.replace('.', ' ')

# Create list
contents_into_list = []

# Replace newline

contents_into_list = contents.split(" ")

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
#                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her",
#                       "hers", "its", "they", "them", "their", "what", "which", "who", "whom", "this",
#                       "that", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had",
#                       "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
#                       "where", "how", "all", "any", "both", "each", "few", "more", "some", "such",
#                       "no", "nor", "too", "very", "can", "will", "just"]

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print(contents_into_list)
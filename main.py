# Final project for Crash Course Python on Coursera
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
import io
import sys

# Open file and put text into file
with open('moby-dick.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

# Replace newlines and periods with blank spaces
contents = contents.replace('\n', ' ')
contents = contents.replace('. ', ' ')

# Create list
contents_into_list = []

# Split into list by spaces
contents_into_list = contents.split(" ")

# punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her",
                       "hers", "its", "they", "them", "their", "what", "which", "who", "whom", "this",
                       "that", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had",
                       "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                       "where", "how", "all", "any", "both", "each", "few", "more", "some", "such",
                       "no", "nor", "too", "very", "can", "will", "just", "gutenberg", "ebook"]

# Blank list
contents_interesting = []

# Add words with only alpha characters and not in uninteresting list
for word in contents_into_list:
    word = word.lower()
    if word not in uninteresting_words:
        if word.isalpha():
            contents_interesting.append(word)

# Blank dictionary
contents_counts = {}


if __name__ == '__main__':
    print(contents_interesting)
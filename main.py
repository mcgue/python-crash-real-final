# Final project for Crash Course Python on Coursera
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
import io
import sys

# Open file and put text into file
with open('moby-dick.txt', 'r', encoding='utf-8') as f:
    file_contents = f.read()

# Replace newlines and periods with blank spaces
file_contents = file_contents.replace('\n', ' ')
file_contents = file_contents.replace('. ', ' ')

# Create list
#file_contents = []

# Split into list by spaces
file_contents = file_contents.split(" ")

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
for word in file_contents:
    word = word.lower()
    if word not in uninteresting_words:
        if word.isalpha():
            contents_interesting.append(word)

# Blank dictionary
contents_counts = {}

# Create dictionary with unique words and their frequency count
for word in contents_interesting:
    if word in contents_counts:
        contents_counts[word] +=1
    else:
        contents_counts[word] = 1

#wordcloud
def word_cloud(dict)
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dict)
    return cloud.to_array()

if __name__ == '__main__':
    print(contents_counts)
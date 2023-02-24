# Final project for Crash Course Python on Coursera
# Finished, although could simplify code
import wordcloud
from matplotlib import pyplot as plt

def calculate_frequencies(file_contents):
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "for",
                           "hers", "its", "they", "them", "their", "what", "which", "who", "whom", "this", "into",
                           "that", "am", "are", "was", "were", "be", "been", "being", "have", "has", "had", "one",
                           "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "on", "so",
                           "where", "how", "all", "any", "both", "each", "few", "more", "some", "such", "there",
                           "no", "nor", "too", "very", "can", "will", "just", "gutenberg", "ebook", "not", "in"]

    # Replace newlines and periods with blank spaces
    file_contents = file_contents.replace('\n', ' ')
    file_contents = file_contents.replace('. ', ' ')

    # Split into list by spaces
    file_contents = file_contents.split(" ")

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

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(contents_counts)
    return cloud.to_array()

if __name__ == '__main__':
    # Open file and put text into file
    with open('moby-dick.txt', 'r', encoding='utf-8') as f:
        file_contents = f.read()
    # Run function to create word cloud
    myimage = calculate_frequencies(file_contents)
    plt.imshow(myimage, interpolation='nearest')
    plt.axis('off')
    plt.show()

    print('Yay!')
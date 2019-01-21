# import os, zipfile and matplotlib modules
import os
import zipfile
import matplotlib.pyplot as plt
# initialize empty lists
word_list = []
word_frequency = []
words = []
frequencies = [] 
bad_chars = ',./?<>;\':[]"!@#$%^&*()`~'
# request file path from user
file_path = input('Please provide the file path: ')
# loop through the directory with the os module
for file in os.listdir(file_path):
    # if encountered file is a text file, open the file amd split sentences into individual words
    if file.endswith(".txt"):
        word_list2 = open(file_path + '\\' + file).read()
        # remove "bad characters" from file
        for b in bad_chars:
            word_list2 = word_list2.replace(b,'')
        word_list2 = word_list2.split()
        # append each word in lower case form to the word_list
        for word in word_list2:
            word_list.append(word.lower())
        print (word_list2)
    # if encountered file is a zip file, open the file with the zipfile module
    # and look for text files
    if file.endswith(".zip"):
        compressed_file = zipfile.ZipFile(file_path + "\\" + file)
        for item in compressed_file.namelist():
            # if encountered file is a text file, open the file, decode the file
            # append each word in lower case form to the word_list
            if item.endswith(".txt"):
                with compressed_file.open(item) as f:
                    f = f.read().decode('utf-8')
                    # remove "bad characters" from file
                    for b in bad_chars:
                        f = f.replace(b,'')
                    f = f.split()
                    # append each word in lower case form to the word_list
                    for word in f:
                        word_list.append(word.lower())
# count occurence of each word and append the frequency to word_frequency list
for word in word_list:
    word_frequency.append(word_list.count(word))
# pair each word with it's corresponding frequency
pairs = list(zip(word_list, word_frequency))
# seperate unique words with their frequency, append to appropriate lists
for i in range(len(pairs)):
    word = pairs[i][0]
    freq = pairs[i][1]
    if word not in words:
        words.append(word)
        frequencies.append(freq)

# label the histogram
plt.xlabel('Word Count')
plt.ylabel('Frequency')
# plot the histogram
plt.hist(frequencies)
# show the histogram plot
plt.show()

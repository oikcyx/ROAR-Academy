#Exercise 1: 
with open("motto.txt", "w") as file:
    file.write("Fiat Lux!\n")

with open("motto.txt", "r") as file:
    content = file.read()
    print("File content:", content)

with open("motto.txt", "a") as file:
    file.write("Let there be light!\n")

with open("motto.txt", "r") as file:
    content = file.read()
    print("File content:", content)

#Exercise 2:
from matplotlib import image
from matplotlib import pyplot
import numpy as np
import os

path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/' + 'lenna.bmp'
data = image.imread(filename)
result = data.copy()

result = data[:101, :101, :] = 0

# use pyplot to plot the image
pyplot.imshow(result, cmap = 'gray', vmin = 0, vmax = 255)
pyplot.show()


#Exercise 3: 
import PyPDF2
import re 

file_handle = open("Sense-and-Sensibility-by-Jane-Austen.pdf", "rb") 
pdfReader = PyPDF2.PdfFileReader(file_handle) 

frequency_table = dict()

for page_number in range(pdfReader.numPages):
    page_object = pdfReader.getPage(page_number)
    page_text = page_object.extractText()
    lines = page_text.split('\n')

    for line in lines:
        new_line = re.sub(r'[^\w\s]', '', line)
        words = new_line.split()
        for word in words:
            lowercase_word = word.lower()
            if lowercase_word.isalpha() and not lowercase_word.startswith(("https", "www")):
                frequency_table[lowercase_word] = frequency_table.get(lowercase_word, 0) + 1
        
file_handle.close()

for word, count in frequency_table.items():
    print(word, count)
# import libraries --------------------------------------
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image

# Initialize text data (Read from text files-------------
dataset = open("obama.txt", "r").read()
dataset2 = open("Trump.txt", "r").read()

# Method for creating word cloud of obama speech data----
def create_word_cloud_obama(string):
   # Use cloud image mask to outline words
   maskArray = npy.array(Image.open("cloud.png"))
   # configure cloud
   cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
   # generate cloud from input string
   cloud.generate(string)
   # save file as .png image
   cloud.to_file("ObamaWordCloud.png")

# Method for creating word cloud for trump speech data----
def create_word_cloud_trump(string):
   # Use cloud image mask to outline words
   maskArray = npy.array(Image.open("cloud.png"))
   # configure cloud
   cloud = WordCloud(background_color = "white", max_words = 200, mask = maskArray, stopwords = set(STOPWORDS))
   # generate cloud from input string
   cloud.generate(string)
   # save file as .png image
   cloud.to_file("TrumpWordCloud.png")

# Convert upper case to lowercase--------
dataset = dataset.lower()
dataset2 = dataset2.lower()

# Call methods with text parameter to create word clouds-----
create_word_cloud_obama(dataset)
create_word_cloud_trump(dataset2)

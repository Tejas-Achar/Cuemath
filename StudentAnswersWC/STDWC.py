# import libraries --------------------------------------
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image
from collections import namedtuple

# Get student names --------------------------------------
studentName1 = input("Enter First student name : ")
studentName2 = input("Enter Second student name : ")

# Get student Answers ------------------------------------
dataset = input("Enter First student's answer : ")
dataset2 = input("Enter Second student's answer : ")

# Create Student Named Tuples ----------------------------
studentanswers = namedtuple('Student',['Name','Answer'])
s1 = studentanswers(studentName1,dataset)
s2 = studentanswers(studentName2,dataset2)


#Function to find common and uncommon words----------------
def find_common_words(string1,string2):
   list1 = string1.split(" ")
   list2 = string2.split(" ")
   # Generate Common List----------------------------------
   commonlist = list(set([i for i, j in zip(list1, list2) if i == j]))
   commonString = ""
   for i in commonlist:
       commonString = commonString + i
   #Generate uncommon list ---------------------------------
   uncommonlist = list(set([i for i, j in zip(list1, list2) if i != j]))
   uncommonString = ""
   for i in uncommonlist:
       uncommonString = uncommonString + i
   print(commonlist)
   print(uncommonlist)
   print(list2)
   # If no common words
   if len(commonlist) == 0:
       commonString = "NoCommonAnswerWords"
   # If no uncommon words
   if len(uncommonlist) == 0:
       uncommonString = "NoUncommonAnswerWords"

   # Create common words word cloud-----------------------------
   create_word_cloud(commonString,"Common Answer Words","green")
   # Creat uncommon words word cloud----------------------------
   create_word_cloud(uncommonString," UnCommon Answer Words","red")


# Method for creating word cloud of answer data-------
def create_word_cloud(string1,filename,color):
   # Use cloud image mask to outline words
   maskArray = npy.array(Image.open("cloud.png"))
   # configure cloud

   cloud = WordCloud(background_color = "white",color_func=lambda *args, **kwargs: color, max_words = 500, mask = maskArray, stopwords = set(STOPWORDS))

   # generate cloud from input string
   cloud.generate(string1)
   # save file as .png image
   cloud.to_file(filename+".png")


# Convert upper case to lowercase--------
dataset = dataset.lower()
find_common_words(s1.Answer,s2.Answer)

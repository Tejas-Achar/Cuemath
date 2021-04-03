from tkinter import*
from textblob import TextBlob
import tweepy

mykeys = open("auth4","r").read().splitlines()
api_key = mykeys[0]
api_key_secret = mykeys[1]
api_token = mykeys[2]
api_token_secret = mykeys[3]

auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(api_token,api_token_secret)

api = tweepy.API(auth_handler,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


root = Tk()
root.geometry('500x500')
root.title("TA")
label_0 = Label(root, text="Twitter Analyser",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
label_1 = Label(root, text="Search Query",width=20,font=("bold", 10))
label_1.place(x=68,y=130)
entry_1 = Entry(root)
entry_1.place(x=240,y=130)
label_2 = Label(root, text="No of results",width=20,font=("bold", 10))
label_2.place(x=68,y=180)
entry_2 = Entry(root)
entry_2.place(x=240,y=180)
label_3 = Label(root, text="Result : ",width=20,font=("bold", 10))
label_3.place(x=68,y=230)
label_4 = Label(root, text="",width=65,font=("bold", 10))
label_4.place(x=7,y=260)


def call_result(label_result, entry_1, entry_2):
    search_term = (entry_1.get())
    tweet_amount = int(entry_2.get())
    result = ""

    tweets = tweepy.Cursor(api.search, q=search_term, lang="en").items(tweet_amount)

    polarity = 0
    positive = 0
    neutral = 0
    negative = 0
    positiveTweets = []
    negativeTweets = []
    neutralTweets = []
    for tweet in tweets:
        final_text = tweet.text.replace('RT', '')
        if final_text.startswith(' @'):
            position = final_text.index(':')
            final_text = final_text[position + 2:]
        if final_text.startswith("@"):
            position = final_text.index(' ')
            position = final_text[position + 2:]
        analysis = TextBlob(final_text)
        tweet_polarity = analysis.polarity
        if tweet_polarity > 0:
            print(type(final_text))
            positiveTweets.append(final_text)
            positive += 1
        elif tweet_polarity < 0:
            negativeTweets.append(final_text)
            negative += 1
        else:
            # f = open("Neutral.txt", "w+").writelines(str(final_text))
            neutralTweets.append(final_text)
            neutral += 1

        polarity += analysis.polarity

    # print(polarity)

    x = "Positive tweets = "+str(positive)
    y = "Negative tweets = "+str(negative)
    z = "Neutral tweets = "+str(neutral)

    f1 = open("Positive.txt", "w+")
    f1.writelines(positiveTweets)
    f1.close()

    f2 = open("Negative.txt", "w+")
    f2.writelines(neutralTweets)
    f2.close()

    f3 = open("Neutral.txt", "w+")
    f3.writelines(neutralTweets)
    f3.close()

    print(x, y, z)
    result = x + " | " + y + " | " + z
    label_result.config(text=result)
    return


Button(root, text='Submit',width=20,bg='brown',fg='white',command=lambda:call_result(label_result=label_4,entry_1=entry_1,entry_2=entry_2)).place(x=180,y=380)
# it is use for display the registration form on the window
root.mainloop()

import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize() :
 url = utext.get('1.0', "end").strip()
 article = Article(url) #creating object
 article.download()
 article.parse() # article disect into parts they need
 article.nlp()

 title.config(state = 'normal')
 author.config(state = 'normal')
 publication.config(state = 'normal')
 summary.config(state = 'normal')
 sentiment.config(state = 'normal')

 title.delete(1.0, 'end')
 title.insert('1.0', article.title)

 author.delete(1.0, 'end')
 author.insert('1.0', article.authors)

 publication.delete(1.0, 'end')
 publication.insert('1.0', article.publish_date)

 summary.delete(1.0, 'end')
 summary.insert('1.0', article.summary)

 analysis = TextBlob(article.text)  # give the full text just not the summery
 sentiment.delete(1.0, 'end')
 sentiment.insert('1.0', f'Polarity : {analysis.polarity}, Sentiment : {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "nutral"}')

 title.config(state='disabled')
 author.config(state='disabled')
 publication.config(state='disabled')
 summary.config(state='disabled')
 sentiment.config(state='disabled')

root = tk.Tk() # calling constructor
root.title('SuMMARIZER')
root.geometry('1200x600')
#For the Title block

tlabel = tk.Label(root, text = "Title")
tlabel.pack()

title = tk.Text(root, height = 2,  width = 140)
title.config(state = 'disabled', bg = '#91D8E4')
title.pack()

#For the author block

alabel = tk.Label(root, text = "Author")
alabel.pack()

author = tk.Text(root, height = 2,  width = 140)
author.config(state = 'disabled', bg = '#91D8E4')
author.pack()

# For the publication date block

plabel = tk.Label(root, text = "Pubication Date")
plabel.pack()

publication = tk.Text(root, height = 2, width = 140)
publication.config(state = 'disabled', bg = '#91D8E4')
publication.pack()

#For the summery block

slabel = tk.Label(root, text = "Summery")
slabel.pack()

summary = tk.Text(root, height = 20,  width = 140)
summary.config(state = 'disabled', bg = '#91D8E4')
summary.pack()

# for the sentiment analysis block

selabel = tk.Label(root, text = "Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height = 2,  width = 140)
sentiment.config(state = 'disabled', bg = '#91D8E4')
sentiment.pack()

# For the url block

ulabel = tk.Label(root, text = "Put the url")
ulabel.pack()

utext = tk.Text (root, height = 2,  width = 140)
utext.pack()

#For the button section

btn = tk.Button(root, text = "Summarize", command = summarize)
btn.pack()

root.mainloop()


# Tested url
# url : https://edition.cnn.com/travel/article/dhaka-bangladesh-public-transport-metro-intl-hnk/index.html
# url : https://www.nytimes.com/2022/12/28/world/europe/ukraine-russia-peace-talks.html


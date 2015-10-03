from flask import Flask, render_template, session, redirect, url_for, flash, request, abort, send_file 
from hackernews import HackerNews
from flask_material import Material
from IPython import embed
from stop_words import get_stop_words
import csv 
#from metamind.api import ClassificationModel, set_api_key

stopwords = get_stop_words('english')
stopwords = map(str,stopwords)
stopwords = map(lambda x: x.lower(), stopwords)

data_file = 'wordcount.csv'
  
app = Flask(__name__)
Material(app)

hn = HackerNews()

#set_api_key("39W42KN7ZKFYcWewQLewjxIWd8wfsICtcbyD8SxQZC42gEvGmA")

@app.route('/')
def index():  
  
  #recursive method to remove Unicode bullshit
  def byteify(input):
    if isinstance(input, dict):
        return {byteify(key):byteify(value) for key,value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
      
  stories = {}
  posts = []
  x=0
  #get the top 10 stories on HN, push into a dict with name and score
  for story_id in hn.top_stories(limit=100):
    story = hn.get_item(story_id)
    stories[x] = {}
    stories[x]['name'] = [story.title]
    stories[x]['score'] = [story.score]
    x+=1
  
  stories = byteify(stories)
  
  key_words={}
  #refine the story dict
  for x in stories:
    posts.append(stories[x])
    for word in stories[x]:
        if word.lower() not in stopwords:
            try:
              key_words[word.lower()] = key_words[word.lower()] + 1
            except:
              key_words[word.lower()] = 1

  with open(data_file, 'wb') as f:  # Just use 'w' mode in 3.x
      w = csv.DictWriter(f, key_words.keys())
      w.writeheader()
      w.writerow(key_words)
      w.close()
      
  #MetaMind call
#  sentiment = byteify(ClassificationModel(id=155).predict("hackathon", input_type="text"))

  #render index.html template and passes posts dict
  return render_template('index.html', posts=posts[:10])

@app.route('/wordcloud/')
def wordcloud():
  return "wordcloud"
  

def hello_world():
    return 'Hello Jenkins!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
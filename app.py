from flask import Flask, render_template, session, redirect, url_for, flash, request, abort, send_file 
from hackernews import HackerNews
from flask_material import Material
from metamind.api import ClassificationModel, set_api_key
from IPython import embed


  
app = Flask(__name__)
Material(app)

hn = HackerNews()

set_api_key("39W42KN7ZKFYcWewQLewjxIWd8wfsICtcbyD8SxQZC42gEvGmA")



@app.route('/')
<<<<<<< HEAD
@app.route('/index') 
def index():  
  
    
  
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
  for story_id in hn.top_stories(limit=10):
    story = hn.get_item(story_id)
    stories[x] = {}
    stories[x]['name'] = [story.title]
    stories[x]['score'] = [story.score]
    x+=1
  
  stories = byteify(stories)
  
  for x in stories:
    posts.append(stories[x])
      
  
  sentiment = byteify(ClassificationModel(id=155).predict("hackathon", input_type="text"))


  return render_template('index.html', title='HN Feeder', posts=posts, user='Salil')
                           

def hello_world():
    return 'Hello Jenkins!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
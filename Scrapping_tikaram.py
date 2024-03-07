# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/getTimeStories', methods=['GET'])
def get_time_stories():
    try:
        # Fetch HTML content from Time.com
        u = "https://time.com"
        response = requests.get(u)
        response.raise_for_status()  # Raise an exception for bad responses

        # Parse HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the latest 6 stories
        time_latest_stories = []
        for story in soup.find_all(class_='latest-stories__item')[:6]:
            title = story.find('h3').text.strip()
            l = u + story.find('a')['href'].strip()
            time_latest_stories.append({'title': title, 'link': l}, {'Updated'})
        
        
        return jsonify(time_latest_stories)

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

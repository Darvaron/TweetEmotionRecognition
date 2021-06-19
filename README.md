# TweetEmotionDetection
Emotion detection in tweets in real time from a given hashtag.

### Installation
```
pip install -r requirements.txt
```

You need to have your own tokens, create a file called TOKENS.txt that contains those tokens next to the project folder.
```
CONSUMER_KEY
CONSUMER_SECRET
ACCESS_TOKEN
ACCESS_TOKEN_SECRET
```
### How data is preproccesed  
- The tweet is lowercased.  
- '\n' are replaced by ' ' for all the '\n' in the tweet, if there's a '\n' at the end it is replaced by ''
- duplicated spaces are deleted.  
- '' are deleted.  
- for each word:  
    * Some symbols are removed from the tweets in certain cases. (for example, periods at the end of the words)
    * The word is classified in: word, user, url, hashtag or unidentified.  
    * The string is reaplced by its value, \<usermention>, \<url>, \<hashtag> or its value respectively.  
- The tweet is passed to sequence (one hot encoding and word embedding) and finally truncated and padded.
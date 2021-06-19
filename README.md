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
    * ..., ’, ', “, ”, .”, (, ", ), !, ? are removed from the word.  
    * ,, \, ., ;, :, ‘, ’, ", ', ! are removed at the end - some are redundant.  
    * The word is classified in: word, user, url, hashtag or unidentified.  
    * The word is reaplce by word, <usermention>, <url>, <hashtag>, word respectively.  
- Then is passed to sequence (one hot encoding and word embedding) and finally truncated and padded.
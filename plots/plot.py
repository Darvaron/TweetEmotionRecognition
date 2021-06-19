import matplotlib.pyplot as plt
from collections import Counter

'''
Plots data from the current session
'''

plt.rcParams["figure.figsize"] = (15, 15)

labels = []
words = []
tweets_saved = []

def plot_fig():
    plt.cla()
    plt.clf()

    plt.subplot(2, 2, 1)
    types = set(labels)
    count = [labels.count(i) for i in types]
    plt.pie(count, labels=types, shadow=True)
    plt.subplot(2, 2, 2)
    plt.hist(labels, color='purple', bins=11)
    plt.ylabel('Number of tweets')
    plt.xlabel('Emotions')
    plt.title('Classes')
    plt.subplot(2, 2, 3)
    tweet_lenght = [len(x.split(' ')) for x in tweets_saved]
    plt.hist(tweet_lenght, bins=len(set(tweet_lenght)), color='skyblue')
    plt.ylabel('Number of tweets')
    plt.xlabel('Number of words')
    plt.title('Length of tweets')
    plt.subplot(2, 2, 4)
    words = [x.split(' ') for x in tweets_saved]
    words_num = sum([len(l) for l in words])
    counter = Counter(words[0])
    for i in words[1:]:
        counter.update(i)

    common_words = counter.most_common(10)
    nwords = [w for w, q in common_words]
    qwords = [q for w, q in common_words]

    plt.bar(nwords, qwords, color='green')
    plt.ylabel('Number of times')
    plt.xlabel('Words')
    plt.title('10 most common words')
    plt.show()
    print('Total words: {}'.format(words_num))
    plt.show()





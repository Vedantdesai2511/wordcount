from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import numpy as np
import operator

def home(request):
    return render(request, 'home.html')


def count(request):
    # fulltext = request.GET['fulltext']
    # print(fulltext)
    return render(request, 'count.html')


def countaction(request):
    # fulltext = request.GET['fulltext']
    #
    # wordlist = fulltext.split()
    #
    # worddictionary = {}
    #
    # for word in wordlist:
    #     if word in worddictionary:
    #         #Increase
    #         worddictionary[word] += 1
    #     else:
    #         #add to the dictionary
    #         worddictionary[word] = 1
    #
    # sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    fulltext = request.GET['fulltext']
    print(fulltext)
    text_list = fulltext.split()
    set_ = set(text_list)
    count_dict = {}
    import re
    for i in set_:
        findall_ = re.findall(i, fulltext)
        count_dict[i] = len(findall_)

    # index = np.arange(len(list(count_dict)))
    # print(index)
    df = pd.DataFrame(count_dict.items(), columns=['Word', 'Count'])
    # df = pd.DataFrame.from_dict(count_dict, orient=index)
    # np.argmax(df)
    max_index = np.argmax(df['Count'])
    maximimusedword = df['Word'][max_index]
    print(maximimusedword)
    #
    # return render(request, 'countaction.html',
    #               {'fulltext': fulltext, 'count': len(wordlist), 'sortedwords': sortedwords, 'count_dict': count_dict.items()})
    return render(request, 'countaction.html', {'fulltext': fulltext, "text_list": len(text_list), 'maximimusedword': maximimusedword,'count_dict': count_dict.items(), 'df': df['Word'].values})


def home_(request):
    return HttpResponse("Hello there!!")


def about(request):
    return render(request, 'about.html')

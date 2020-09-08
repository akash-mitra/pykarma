import urllib.request, json

def getTopicCount(topic):

    uri = 'https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=' + topic
    text = ''
    with urllib.request.urlopen(uri) as url:
        data = json.loads(url.read().decode())
        text = str(data['parse']['text'])

    return text.count(topic)



topic = 'pizza'
print (getTopicCount(topic))
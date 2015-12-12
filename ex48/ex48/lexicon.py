directions = ['north', 'south', 'east', 'west',
              'down', 'up', 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stop_words = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']


def scan(input_string):
    input_words = input_string.split()
    result = []
    for word in input_words:
        if word.lower() in directions:
            result.append(('direction', word))
        elif word.lower() in verbs:
            result.append(('verb', word))
        elif word.lower() in stop_words:
            result.append(('stop', word))
        elif word.lower() in nouns:
            result.append(('noun', word))
        else:
            try:
                result.append(('number', int(word)))
            except ValueError:
                result.append(('error', word))
    return result

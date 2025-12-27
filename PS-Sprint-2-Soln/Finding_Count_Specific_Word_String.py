def count_word_string(str):
    words = str.split()
    word_count = {}
    for word in words:
        word = word.lower().strip('.,!?;"\'()[]{}')
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

input_string = "Hello world! This is a test. Hello again, world."
result = count_word_string(input_string)
from textblob import TextBlob
#   documentation
#   the libary use is textblob .. you must first install textblob libray
words = TextBlob(input( 'enter the word to correct: ' ))

words = words.correct()
print(words)



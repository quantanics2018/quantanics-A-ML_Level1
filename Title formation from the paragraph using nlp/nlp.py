import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.tokenize.treebank import TreebankWordDetokenizer

nltk.download('punkt')
nltk.download('stopwords')

# Sample paragraph
paragraph = """
Natural language processing (NLP) is a subfield of artificial intelligence that focuses on the interaction between computers and humans through natural language. It involves various tasks such as text generation, machine translation, sentiment analysis, and more. NLP has applications in chatbots, search engines, and language understanding systems.
"""

# Tokenize sentences
sentences = sent_tokenize(paragraph)

# Tokenize words and remove stopwords
stop_words = set(stopwords.words("english"))
word_tokens = [word for sent in sentences for word in word_tokenize(sent) if word.lower() not in stop_words]

# Calculate word frequency
freq_dist = FreqDist(word_tokens)

# Select top words based on frequency
num_top_words = 5
top_words = [word for word, _ in freq_dist.most_common(num_top_words)]

# Generate the title
title = TreebankWordDetokenizer().detokenize(top_words)

print("Original Paragraph:\n", paragraph)
print("\nGenerated Title:\n", title)

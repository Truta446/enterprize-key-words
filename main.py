import matplotlib.pyplot as plt
import nltk
import re
from collections import Counter
from nltk.corpus import stopwords
from profanity_check import predict
from wordcloud import WordCloud

def generate_cloud_words(text: str, qty_key_words: int) -> None:
  nltk.download('stopwords')

  text = text.split()

  stopwordsNltk = stopwords.words('portuguese')

  words = []

  for word in text:
    if word not in stopwordsNltk and word != '' and predict([word]) != 1:
      words.append(word)

  count = Counter(words)
  most_common = count.most_common(qty_key_words)

  words = [x[0] for x in most_common]

  z = lambda x: re.compile('\#').sub('', re.compile('rt @').sub('@', x, count=1).strip())
  words = z(str(words).replace("'", ""))

  wordCloud = WordCloud(width=2400, height=1600, margin=0).generate(words)
  plt.figure(figsize=(20, 11))
  plt.imshow(wordCloud, interpolation='bilinear')
  plt.axis("off")
  plt.margins(x=0, y=0)
  wordCloud.to_file("cloud.png")

  print(f'\nPalavras capturadas: {most_common}')

def main() -> None:
  qty_key_words = int(input('Quantas palavras chave deseja obter: '))

  with open('to-read.txt', mode='r', encoding='utf8') as f:
    text = f.read()

  text = text.lower()

  trash = ['.', ',', ';', ':', '?', '!', '\'', '"', '“', '”', '(', ')', '@', '#', '%', '¨', '&', '*', '/', '\\', '-', '+', '\n']

  for t in trash:
    text = text.replace(t, " ")

  words = str(len(text.split()))
  letters = str(len(text))

  print(f"\nO texto contém {words} palavras e {letters} letras.\n")

  generate_cloud_words(text, qty_key_words)

if __name__ == "__main__":
  main()

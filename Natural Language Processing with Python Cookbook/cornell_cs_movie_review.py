from nltk.corpus import CategorizedPlaintextCorpusReader
from random import randint

reader = CategorizedPlaintextCorpusReader(R'dataset/Cornell_CS_Movie_Review/Review/tokens',R'.*\.txt', cat_pattern = R'(\w+)_cv/*')
print(reader.categories())
print(len(reader.fileids()))

posFiles = reader.fileids(categories='pos')
# print(len(posFiles))
negFiles = reader.fileids(categories='neg')
# print(len(negFiles))

fileP = posFiles[randint(0,len(posFiles)-1)]
fileN = negFiles[randint(0,len(posFiles)-1)]

for w in reader.words(fileP):
    print(w + ' ', end = '')
    if w is '.' :
        print()

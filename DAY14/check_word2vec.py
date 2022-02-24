from gensim.models import word2vec

model=word2vec.Word2Vec.load("toji.model")
result = model.wv.most_similar(positive=["집"])

print(result)
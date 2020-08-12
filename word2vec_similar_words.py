import time
import codecs
from konlpy.tag import Okt
from gensim.models import word2vec

print("Application has started @ " + time.strftime('%c', time.localtime(time.time())))

f = open("요한복음.txt", mode='rt', encoding='utf-8')
text = f.read()
f.close()
print(text)
print('\n//Done: The file has been read.\n')

twiter = Okt()
results = []
lines = text.split('\n')
for line in lines:
    sentence_list = twiter.pos(line, norm=True, stem=True)
    word_list = []
    for word in sentence_list:
        if not word[1] in ['josa', 'Eomi', 'Punctuation']: #각각 조사, 어미, 구두점(".") 제외
            word_list.append(word[0])
    line_processed = (' '.join(word_list)).strip()
    results.append(line_processed)
    print(line_processed)



morpheme_file = 'bible_morpheme_processed.txt'
with open(morpheme_file, 'w', encoding='utf-8') as fp:
    fp.write('\n'.join(results))
print('\n//Done: Morpheme file has been created.\n')

"""
workers = 병렬처리할 CPU 갯수, Default = 3
iter = 동일 데이터 러닝 전체 반복 횟수 (epochs), Default = 5
batch_words = 사전구축시 한번에 읽는 단어 수, Default = 10000
size = 한 단어에 대한 벡터 스페이스 크기, Default = 100
window = 단어 유사도 고려시 최대 단어 거리, Default = 5
sg = 1 = Skip-Gram 사용, Default = 0 (CBOW)
hs = 1 = Hierarchical Softmax 사용, Default = 0 (Negative Sampling)
min_count = 1 = 단어 등장 횟수가 1보다 작은 단어 무시 (즉 1 경우 모든 단어 사용)
"""
data = word2vec.LineSentence(morpheme_file)
model = word2vec.Word2Vec(data, size=1000, window=10, sg=1, hs=1, min_count=1, batch_words=10000, iter=10, workers=4)
model.save('bible_word2vec_gensim.model') #용량이 클 수 있음 (말뭉치 포함)
print('\n//Done: Model has been saved.\n')



# 저장된 모델을 불러와서 사용
model = word2vec.Word2Vec.load("bible_word2vec_gensim.model")
# 긍정적(positive) / 부정적(nagative) 연관이 있는 단어 출력가능
similar_words = model.wv.most_similar(positive=["예수", "성령"], negative=["사람"])[0:5]
print(similar_words)



def print_array(arr):
    print("type:{}".format(type(arr)))
    print("shape: {}, dimension: {}, dtype:{}".format(arr.shape, arr.ndim, arr.dtype))
    print("Array's Data:\n", arr)

print_array(model.wv.__getitem__(["예수", "성령"]))

print("Application has ended @ " + time.strftime('%c', time.localtime(time.time())))

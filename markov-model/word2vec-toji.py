import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from gensim.models import word2vec

fp = codecs.open('BEXX0003.txt', 'r', encoding='utf-16')
soup = BeautifulSoup(fp, 'html.parser')
body = soup.select_one('body > text')
text = body.getText()

twiter = Twitter()
results = []
lines = text.split('\n')
for line in lines:
    malist = twiter.pos(line, norm=True, stem=True)
    r = []
    for word in malist:
        if not word[1] in ['josa', 'Eomi', 'Punctuation']:
            r.append(word[0])
    rl = (' '.join(r)).strip()
    results.append(rl)
    print(rl)



wakati_file = 'toji.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp:
    fp.write('\n'.join(results))

data = word2vec.LineSentence(wakati_file)
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save('toji.model')
print('ok')

"""
활용:
    유사한 단어를 확인할 때 most_similar() 메소드를 사용합니다.
    positive / nagative 매개변수를 붙여 호출할 수 있습니다.
결과:
    [('구석', 0.8189886808395386),
     ('제', 0.7966692447662354),
     ('점심', 0.7663639783859253),
     ('이지마', 0.7649472951889038),
     ('하모', 0.7538532018661499),
     ('말리다', 0.7532320022583008),
     ('그까짓', 0.7482759356498718),
     ('앙님', 0.745795488357544),
     ('물이', 0.745074987411499),
     ('날', 0.7414768934249878)]
"""
model.most_similar(model.most_similar(positive=["집"])) #'집'과 긍정적인 연관이 있는 단어 출력

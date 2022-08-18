import collections
import re

#[^은 not \w는 문자] 그래서 위 정규식은 단어 문자가 아닌 모든 문자를 공백으로 치환하는 역할을 한다.
#그리고 모든 문자를 소문자로 바꾸고 띄어쓰기를 기준으로 split해서 words 에 저장한다.
#만약에 banned에 있는 문자가 아니라면말이다.

def mostCommonWord(self,paragraph:str, banned: list[str]) ->str:
    words = [word for word in re.sub(r'[^\w]',' ',paragraph)
             .lower().split()
                if word not in banned]
#콜렉션에 있는 counter 라는 함수는 아이템에 대한 개수를 계산해 딕셔너리로 리턴하는 함수이다.
#여기서 가장 많이 쓰인 단어를 하나 결정해서 리스트의 결과로 [(ball,2)] 이라고 리턴한다.
#리턴값이 리스트와 튜플로 되어있기 때문에 [0][0]으로 접근해서 ball을 리턴한다.
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(mostCommonWord(paragraph,paragraph,banned))
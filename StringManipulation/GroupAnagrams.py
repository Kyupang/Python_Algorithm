import collections


def groupAnagrams(self, strs:list[str]) -> list[list[str]]:
    anagrams = collections.defaultdict(list)

    #밑에있는 과정을 풀이해보자면
    #eat를 정렬하고 리스트로 풀어진 아이를 하나의 문자열로 만든다.
    #그것을 aet라고 나왔을 때 이것을 키로 활용하면
    #각각의 똑같은 알파벳을 가지는 원소들은 하나의 키에 몰리게 된다.
    #따라서 각각의 리스트로 분류가 되는 것을 볼 수 있다.
    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())
    #anagrams는 딕셔너리고 그 값의 values들만 리턴한다.
a = ["eat", "tea", "tan", "ate" ,"nat", "bat"]
print(a)
print(groupAnagrams(a,a))

c = ['ccc','aaaa', 'bgagg', 'bbh']
#x[0]은 문자열의 첫번째 알파벳, x[-1]은 마지막 알파벳
print(sorted(c,key=lambda x:(x[0],x[-1])))
#c를 정렬하는데 문자열의 첫번쨰를 기준으로 오름차순 정렬하되 같은 알파벳이 나오면
# 마지막 알파벳을 기준으로 오름차순 정렬한다.
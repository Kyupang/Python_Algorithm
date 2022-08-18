def reorderLogFiles(self, logs: list[str]) ->list[str]:
    letters, digits = [],[]
    #logs 안에있는 요소를 두 가지 리스트로 나눌 것이다.
    #일단 띄어쓰기를 기준으로 2번째 인덱스 요소를 구분할 것이다.
    #만약 그게 숫자면  logs에 있는 인덱스를 기준으로 digits에 append 할 것이다.
    #만약 그게 숫자가 아니라면 logs에 있는 인덱스를 기준으로 letters에 append 할 것이다.
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    #2개의 키를 람다 표현식으로 정렬
    #내용을 정리해보면 letters 리스트를 정렬할 것이다.
    #2개의 key를 정렬할 것인데 나누어 놓은 key중 두번쨰 있는 것을 오름차순으로 정렬 한 후
    #만약 2번쨰 key가 같을 경우 첫번쨰 키의 오름차순으로 정렬한다.
    letters.sort(key=lambda x: (x.split()[1], x.split()[0]))
    return letters + digits

logs = ["dig1 8 1 5 1","let1 art can", "dig2 3 6", "let2 own kit dig","let3 art zero"]
result = reorderLogFiles(logs,logs)
print(result)
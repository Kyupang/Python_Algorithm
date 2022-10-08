natural_num = set(range(1,10001))
generated_num = set()

for i in natural_num:
    for j in str(i):
        i += int(j)
    generated_num.add(i)

self_num = sorted(natural_num - generated_num)
for i in self_num:
    print(i)

# set은 진짜 집합처럼 사용할 수 있고 중복된 숫자가 들어갈 수 없다.
# union 을 할수도 있고 (+)
# complement를 할수도 있다.(-)
# str 은 하나의 어떤 열을 받으면 그것을 한 index 별로 잘라준다.
# 그래서 str(i) 로 리스트 처럼 접근할 수 있다.

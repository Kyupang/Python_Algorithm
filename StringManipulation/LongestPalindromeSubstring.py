class solution:
    def longestPalindrome(self, s: str) -> str:
        #팰린드롬 판별 및 투 포인터 확장
        #일단 지금의 예제는 홀수 팰린드롬이니 이것을 바탕으로 설명해보겠다.
        #처음에 0과 2에 포인터가 위치한다. 그리고는 팰린드롬을 찾으면 확장시킨다.
        #확장 결과가 끝나면 포인터가 두 개 다 이동을 한 상태이기 때문에
        #결과값인 left+1 에서 right전까지를 return 해야한다.
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        #해당사항이 없을 때 빠르게 리턴
        #배열의 글자수가 1이거나 처음부터 끝까지가 다 같을때
        if len(s) < 2 or s == s[::-1]:
            return s

        #원래 배열은 건들지 않고 새롭게 result를 만들어 리턴한다.
        #list의 가변성을 이용.
        result = ''


        #짝수의 경우 홀수의 경우 아무것도 없는경우중에 길이가 제일 긴 것을 리턴한다.
        #key =len 은 문자열의 길이를 기준으로 max를 뽑아낸다고 하는 것이다.
        for i in range(len(s)-1):
            result = max(result,
                         expand(i,i+1),
                         expand(i,i+2),
                         key= len)

        return result
sol = solution()
a = "babad"
print(sol.longestPalindrome(a))


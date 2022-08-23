class solution:
    def Trap(self,height:list[int])->int:
        #항상 예외처리
        if not height:
            return 0
        #볼륨은 리턴값이니 0으로 초기화
        #left, right는 포인터
        #left_max,right_max는 value
        volume = 0
        left,right = 0,len(height)-1
        left_max, right_max = height[left], height[right]

        #두 포인터가 만날때까지 이동
        while left < right :
            #max값을 저장함으로써 채워야할 물의 높이를 비교할 수 있다.
            left_max,right_max = max(height[left],left_max),\
                                 max(height[right],right_max)

            #항상 더 높은 쪽으로 포인터를 이동
            #이동 후 차이만큼 볼륨 저장
            if left_max<= right_max:
                volume+= left_max - height[left]
                left+=1
            else :
                volume+= right_max -height[right]
                right-=1

        return volume

    #이것은 이해하지 못했따...
    def Trap2(self,height: list[int])->int:
        stack =[]
        volume = 0

        for i in range(len(height)):
            #변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                #스택에서 꺼낸다.
                top = stack.pop()

                if not len(stack):
                    break
                #이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] -1
                waters = min(height[i],height[stack[-1]] - height[top])

                volume += distance* waters
            stack.append(i)
        return volume


sol = solution()
water = [0,1,0,2,1,0,1,3,2,1,2,1]
print(sol.Trap(water))
print(sol.Trap2(water))
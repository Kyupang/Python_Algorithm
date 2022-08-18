n = int(input())
numbers = input()
result = 0
if 1<= n and n <= 100 and len(numbers) == n:
    for i in range(n):
        result += int(numbers[i])
print(result)
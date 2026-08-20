class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stk = []
        for i in range(len(temperatures)):
            while bool(stk) and temperatures[i] > temperatures[stk[-1]]:
                j = stk.pop()
                answer[j] = i - j
            stk.append(i)
        return answer
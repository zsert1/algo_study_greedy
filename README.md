# algo_study_greedy

알고리즘 공부(greedy)

- 동빈나
- 백준

## greedy

### 구현

- 풀이는 떠 올리는 것 이지 소스코드 옮기기 하드
- 알고리즘 문제에서는 2차원 공간은 행렬로 처리
- ex 5행 5열  
   `for i in range(5): 
for j in range(5):
      print('(', j,',',')' ,end='') `
- 위치 확인 시에 동서남북이동 리스트로 만들어 놓기  
  dx=[0,-1,0,1]  
  dy=[1,0,-1,0]  
   동,서,남,북

# 행과 열이 숫자와 문자열 결합된 문제

- 숫자는 int로 변형하고 문자일 경우 **ord(문자)** 를 사용하여 아스키코드로 변경후 **ord('a')를 빼고 +1** 히여 좌표를 맞추어 준 후 시작

# 알파벳 정렬 문제

- 알파펫을 오름 차순으로 정렬하고 뒤에는 숫자를 더해 출력한다
- 문자열을 입력하였을 때 문자를 하나씩 확인
- 숫자인 경우 따로 합계
- 문자인 경우 따로 리스트에 저장(**isalpha**사용!!!)

---

## DP(다이나믹 프로그래밍,동적 계획법)

- 동적 계획법이라고 부른다.
- 동적이란 프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법
- **최적 부분 조건** (Optimal Substructure)
  - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아 큰 문제 해결가능
- **중복되는 문제** (Overlapping Subproblem)
  - 동일한 작은문제를 반복적으로 해결
- 피보나치 수열
  - 특정 번째 수를 구하기 위해 앞의 두 수를 더한 값이 n번째 수이다
  - **점화식**: 인접한 항들 사이의 관계식
  - 피보나치 수열의 점화식: a(n)= a(n-1)+a(n-2)
  - 첫 항과 두번째 항을 알면 모든 수를 구할 수 있다.
  - 배열이나 리스트를 통해 표현 가능하다
  - 단순 재귀함수로 피보나치 수열을 해결하면 지수 시간 복잡도 가지게 된다.
  - 단순 재귀를 돌리면 중복되는 부분문제 발생한다.
- **메모제이션**
  - 다이나믹 프로그래밍을 구현하는 방법 중 하나
  - **한 번 계산한 결과를 메로리 공간에 메모** 하는 기법
    - 캐싱이라고 한다
    - 피보나치 수열을 메모제이션을 적용하여 구하면 시간복잡도 O(N)으로 줄어든다
    - 같은 문제를 다시 호출하면 메모한 결과를 그대로 가져온다
    - 이전에 계산된 결과를 일시적으로 기록해 놓은 넙ㄹ은 개념 의미하므로 다이나믹 프로그래밍에 국한된 개념이 아니다.
  - 탑다운(메모제이션) 하향식이라고 하며 큰 문제를 해결하기 위해 작은 문제 재귀적으로 호출하여 작은 문제를 모두 해결하면 큰 문제를 해결한다.
- 보텀업 방식은 상향식이라 하며 작은 문제를 하나씩 해결해가며 해결한 값을 이용하여 다음 문제를 해결하는 방법(반복문 사용)
  - 결과 저장용 리스트는 **DP테이블** 이라고 부른다

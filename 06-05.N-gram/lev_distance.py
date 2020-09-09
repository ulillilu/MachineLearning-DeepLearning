# 레벤슈타인 거리 구하기
def calc_distance(a, b):
    ''' 레벤슈타인 거리 계산하기 '''
    if a == b: return 0
    a_len = len(a)
    b_len = len(b)
    if a == "": return b_len
    if b == "": return a_len
    # 2차원 표 생성 : 크기 = (a_len+1, b_len+1)
    matrix = [[] for i in range(a_len+1)] # [[], [], [] ...]의 배열이 요소인 배열
    for i in range(a_len+1): # 0으로 초기화
        matrix[i] = [0 for j in range(b_len+1)]
    # 0일 때 초깃값을 설정 : [[0, 1, 2, 3, ...], [1, 0, 0, ...], [2, 0, 0, ...] ...]
    for i in range(a_len+1): # 각 배열의 첫번째 요소 설정
        matrix[i][0] = i
    for j in range(b_len+1): # 첫 번째 배열의 요소 설정
        matrix[0][j] = j
    # 표 채우기
    for i in range(1, a_len+1):
        ac = a[i-1] # a의 i번째 문자
        for j in range(1, b_len+1):
            bc = b[j-1] # b의 j번째 문자
            cost = 0 if (ac == bc) else 1 # cost는 두 문자가 같은 경우 0 다르면 1
            matrix[i][j] = min([
                matrix[i-1][j] + 1,     # 문자 삽입
                matrix[i][j-1] + 1,     # 문자 제거
                matrix[i-1][j-1] + cost # 문자 변경
            ])
    return matrix[a_len][b_len]
# 실행
print(calc_distance("가나다라","가마바라"))

samples = ["신촌역","신천군","신천역","신발","마곡역"]
base = samples[0]
r = sorted(samples, key = lambda n: calc_distance(base, n))
for n in r:
    print(calc_distance(base, n), n)
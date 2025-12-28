# 00001 Two Sum

- Platform: LeetCode
- Difficulty: Easy
- Topics: Array, Hash Table
- Language: Python
- Date: 2025-12-28

## Approach
(내 풀이 흐름 요약 3~6줄. 정답 복붙이 아니라 “재현 가능한 이해”를 목표로 작성)

주어진 숫자 리스트를 중복을 고려하지 않고 딕셔너리에 숫자-인덱스 쌍으로 저장한다.
원본 숫자 리스트를 순회하며 조건을 체크한다.
```
    조건 1. target - nums[i]가 딕셔너리 키에 있는가?
    조건 2. 그 키의 인덱스가 현재 인덱스와 다른 인덱스인가?
```
조건을 만족하는 인덱스와 현재 인덱스를 반환한다.


## Complexity
- Time: O(n)
- Space: O(n)

## Edge Cases / Counterexamples
- [0,4,0], 0 -> [0,2] ✅
- [5,1,5], 10 -> [0,2] ✅
- [2,9,2,7], 4 -> [0,2] ✅
- [-3,1,-3,8], -6 -> [0,2] ✅
- [1,2,3,3], 6 -> [2,3] ✅

## Mistakes / Lessons
- 단순 2단 반복문으로 순회하려다가 topic의 hash table을 보고 힌트를 얻어 다른 풀이를 생각하게 되었다. 이런 습관을 줄여야 겠다.
- 문제의 제약 조건을 역이용하여 풀이한 것 같다. 좀 더 일반화된 풀이를 고민해보는것이 좋을 것 같다.

## Revisit
- [ ] 다시 풀기 (YYYY-MM-DD)
- Notes:
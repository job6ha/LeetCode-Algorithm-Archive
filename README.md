# LeetCode Archive (Solutions by Number)

LeetCode 풀이를 “번호 기반 단일 경로”에 아카이빙하는 저장소입니다.  
다중 토픽 문제를 폴더로 중복 분류하지 않고, **태그 기반 인덱싱(INDEX.md)** 으로 관리합니다.

- 실물(코드/노트): `solutions-by-number/`
- 분류/회고: `INDEX.md` (태그/난이도/언어/날짜)

---

## Goals

- 구현 감각 유지 및 회복(손코딩/디버깅 루틴 강화)
- 문제 유형(패턴) 단위로 회고 가능한 개인 지식베이스 구축
- 반례/경계조건/복잡도 중심의 정리 습관화

---

## Repository Structure

```

.
├─ solutions-by-number/
│  ├─ 0001-two-sum/
│  │  ├─ solution.py
│  │  └─ README.md
│  └─ ...
├─ INDEX.md
└─ README.md

````

---

## Naming Convention

### Problem directory
- `solutions-by-number/####-problem-slug/`
- 예) `solutions-by-number/0001-two-sum/`

### Files inside each problem directory
- 코드: `solution.<ext>`
  - 예) `solution.py`, `solution.cpp`, `solution.java`
- 문제 노트: `README.md` (해당 폴더 내부)

---

## Per-problem README Template

각 문제 폴더의 `README.md`는 아래 형식을 권장합니다.

```md
# ####. Problem Title

- Platform: LeetCode
- Difficulty: Easy / Medium / Hard
- Topics: #arrays-strings #hash-set (복수 가능)
- Language: Python (or others)
- Date: YYYY-MM-DD

## Approach
(내 풀이 흐름 요약 3~6줄. 정답 복붙이 아니라 “재현 가능한 이해”를 목표로 작성)

## Complexity
- Time:
- Space:

## Edge Cases / Counterexamples
- 
- 
- 

## Mistakes / Lessons
- 
- 

## Revisit
- [ ] 다시 풀기 (YYYY-MM-DD)
- Notes:
````

---

## Tagging Policy (INDEX.md)

다중 토픽 문제를 폴더로 중복 분류하지 않고, **태그로만 분류**합니다.
태그는 난립을 막기 위해 가능한 “고정된 세트”로 운영합니다.

권장 태그 예시:

* #arrays-strings
* #hash-set
* #two-pointers
* #sliding-window
* #stack-queue
* #binary-search
* #linked-list
* #tree
* #graph
* #heap
* #dp
* #greedy
* #backtracking
* #intervals
* #math

---

## Commit Convention

* `solve: LC #### - <title> (<lang>)`
* `fix: LC #### - <what>`
* `refactor: LC #### - <what>`
* `notes: LC #### - <what>`

예)

* `solve: LC 0001 - Two Sum (py)`
* `fix: LC 0121 - off-by-one`
* `notes: LC 0020 - add counterexamples`

---

## External Help Policy (AI / References)

이 저장소의 목적은 “스스로 재현 가능한 풀이 기록”입니다.

* 정답 코드/방향성(힌트) 기반의 기록은 지양합니다.
* AI 사용은 아래 용도로만 허용(권장):

  * 반례 제안
  * 시간/공간 복잡도 검증
  * 버그 의심 구간 지적

---

## Disclaimer

문제 원문은 LeetCode에 저작권이 있습니다.
이 저장소에는 문제 설명 원문 전체를 복사하지 않고, 링크/요약/개인 노트 중심으로 기록합니다.
# LeetCode / Algorithm Archive

코딩 감각 유지를 위해 풀이를 아카이빙하는 저장소입니다.  
정답을 “복붙”하기 위한 기록이 아니라, **내가 이해한 방식으로 재현 가능한 상태**를 남기는 것이 목적입니다.

---

## Repository Goals

- 코딩 감각 유지 및 구현 능력 회복
- 동일 유형 재등장 시 빠르게 회상할 수 있는 “개인 지식베이스” 구축
- 반례/경계조건/복잡도 관점의 정리 습관화

---

## Rules (중요)

### 1) 문제 풀이 원칙
- **최소 20~30분은 스스로 설계/구현 후** 제출 기록을 남긴다.
- 풀이 업로드는 “AC(정답)” 기준이 아니라 **의미 있는 시도(실패 포함)**도 가능하되, 반드시 아래 항목을 남긴다:
  - 실패 원인(버그, 경계조건, 복잡도, 문제 이해)
  - 수정 후 어떤 점이 달라졌는지(핵심 1~2줄)

### 2) 외부 도움(AI/블로그) 사용 규칙
- 정답/방향성 힌트를 그대로 옮기는 형태의 기록은 하지 않는다.
- AI는 아래 용도로만 사용한다:
  - 반례 제안
  - 시간/공간 복잡도 검증
  - 버그 의심 구간 지적
- 참고를 했다면, README나 풀이 노트에 **“참고 여부”만 명시**(링크는 선택).

### 3) 기록 품질 기준(최소 요건)
각 문제마다 아래 5가지를 반드시 남긴다.

- **Approach 요약(3~6줄)**: 내가 떠올린 핵심 아이디어/흐름
- **Complexity**: 시간/공간 복잡도
- **Edge Cases / Counterexamples**: 최소 3개
- **Mistakes / Lessons**: 실수 포인트 1~3개
- **Revisit**: 다시 풀어볼 날짜/상태(선택)

---

## Folder Structure

권장 구조는 다음 중 하나를 선택해 유지합니다.

### Option A) Topic-based (추천)
```

.
├─ algorithms/
│  ├─ arrays_strings/
│  ├─ hash_set/
│  ├─ stack_queue/
│  ├─ two_pointers/
│  ├─ binary_search/
│  ├─ trees/
│  ├─ graphs/
│  └─ dp/
├─ database/
├─ pandas/
└─ README.md

```

> 한 번 정하면 가능한 바꾸지 않는다(검색/회고 효율을 위해).

---

## File Naming Convention

- 문제 폴더명:  
  - `####-problem-slug/` (예: `0001-two-sum/`)
- 코드 파일명(언어별):
  - `solution.py`, `solution.cpp`, `solution.java` …
- 노트 파일명:
  - `README.md` (해당 문제 폴더 내부에 둔다)
- DB / pandas 문제:
  - `solution.sql` 또는 `solution.py` + `README.md`

---

## Problem Template (per-problem README)

각 문제 폴더의 `README.md`는 아래 템플릿을 따른다.

```md
# ####. Problem Title

- Link: (optional)
- Difficulty: Easy / Medium / Hard
- Topics: (tags)

## Approach
(내 풀이 흐름 요약 3~6줄)

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

## Commit Convention

가능하면 아래 형식을 따른다.

* `solve: LC #### - <title> (<lang>)`
* `fix: LC #### - edge case / bug`
* `refactor: LC #### - simplify`
* `notes: LC #### - add explanation`

예)

* `solve: LC 0001 - Two Sum (py)`
* `fix: LC 0121 - off-by-one`
* `notes: LC 0020 - add counterexamples`

---

## Index (Optional but Recommended)

문제 수가 늘어나면 루트에 인덱스를 추가한다.

* `INDEX.md` (전체 리스트 + 링크 + 태그 + 날짜)
* 또는 README에 표/리스트로 누적

필드 예시:

* Problem / Difficulty / Topic / Language / Date / Revisit

---

## License / Disclaimer

이 저장소는 개인 학습 기록이며, 문제 원문은 LeetCode에 저작권이 있습니다.
문제 설명 원문 전체를 복사하지 않고, 링크와 요약만 남깁니다.

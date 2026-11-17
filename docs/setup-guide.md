# 처음 설정 안내

컴퓨터 브라우저(크롬 권장)로 진행한다. 휴대폰은 화면이 달라 헷갈리기 쉽다.

## 1. GitHub 가입 (계정이 있으면 건너뜀)

1. https://github.com 접속 → 오른쪽 위 **Sign up**
2. 이메일, 비밀번호, **Username** 입력
   - Username은 사이트 주소에 들어간다: `https://<username>.github.io/aratech/`
   - 영문 소문자와 하이픈만. 예: `aratech-team`
3. 이메일로 온 인증 코드 입력
4. 요금제 질문이 나오면 **Free** (Continue for free)

## 2. 빈 저장소 만들기

1. 로그인한 상태에서 오른쪽 위 **＋** → **New repository**
2. 채울 칸
   - Owner: 내 계정
   - Repository name: `aratech`
   - 공개 여부: **Public** (무료로 사이트 주소를 쓰려면 Public이어야 한다)
   - **Add a README file: 체크하지 않음**
   - Add .gitignore: None / Choose a license: None
3. 초록색 **Create repository**
4. "Quick setup"이라는 빈 안내 화면이 나오면 성공. 주소창 주소가 `github.com/<username>/aratech`

## 3. Claude와 GitHub 연결

1. https://claude.ai/connect-github 접속 → GitHub 계정 연결 → **Authorize**
2. Claude GitHub App 설치 화면에서
   - **Only select repositories** 선택 → `aratech` 고르기
   - **Install**
3. 끝나면 Claude에게 `<username>/aratech`를 알려 준다. Claude가 파일을 올린다.
4. 저장소 페이지를 새로고침해서 `AGENTS.md`, `site/` 등이 보이면 완료

## 4. 사이트 주소 켜기 (한 번만)

1. 저장소 위쪽 메뉴 **Settings**(톱니바퀴) → 왼쪽 메뉴 **Pages**
2. Build and deployment → Source: **GitHub Actions**
3. 위쪽 **Actions** 탭 → "사이트 배포"
   - 빨간 X가 있으면(Pages를 켜기 전에 실행돼서 그렇다) 눌러서 **Re-run all jobs**
   - 노란 점은 진행 중, 초록 체크는 완료 (1~2분)
4. 완료되면 `https://<username>.github.io/aratech/` 에서 사이트가 열린다
   (Settings → Pages 맨 위에도 주소가 표시된다)

## 5. 실수로 지워지지 않게 막기 (권장)

에이전트가 대부분의 변경을 `main`에 바로 올리므로 "PR 필수" 규칙은 켜지 않는다. 대신 기록이 지워지는 것만 막는다.

1. Settings → **Rules** → **Rulesets** → **New ruleset** → **New branch ruleset**
2. Ruleset name: `main 보호`, Enforcement status: **Active**
3. Target branches → **Include default branch**
4. 체크: **Restrict deletions**, **Block force pushes** (나머지는 체크하지 않음. 특히 Require a pull request before merging은 끈다)
5. **Create**

검사(`check`)는 `main`에 올라올 때마다 자동으로 돌고, 오류가 있으면 사이트 배포가 멈춘다.

## 6. 가끔 하는 일: PR 승인

사업 핵심 변경만 PR로 온다: 가설 카드 확정, 7일차 판정, 가격·인원 확정, 대형 기획 결론, 작업 규칙 변경 (`AGENTS.md` §3-1).
나머지는 메인 에이전트가 바로 올리고, 무엇을 바꿨는지 대화에서 알려 준다. 되돌리고 싶으면 메인에게 "되돌려 줘"라고 하면 된다.

PR이 오면 메인이 링크와 볼 것을 알려 준다.

1. 링크를 열고 **Files changed** 탭에서 바뀐 내용 확인
2. 아래쪽 자동 검사(check)가 초록 체크인지 확인
3. PR 설명에 붙은 검수 결과가 "검수 통과"인지 확인
4. **Merge pull request** → **Confirm merge**
5. 1~2분 뒤 사이트에 반영

반려할 때는 메인에게 이유를 말하거나 PR 댓글에 적고 Merge하지 않는다.

## 7. 메인 에이전트와 일하기

사람은 **Claude Code 세션 하나(메인 에이전트)** 와만 대화한다. claude.ai의 Code 탭(웹·앱)에서 이 저장소를 골라 세션을 연다.
메인이 근거 수집, 계산, 렌즈 분석, 검수를 서브에이전트에게 나눠 맡기므로 Antigravity·Codex나 별도 Claude 채팅에 지시문을 붙여 넣을 필요가 없다.

지침서 PDF는 공개 저장소에 넣지 않는다. 권한을 제한한 구글 드라이브에 두고, 메인에게 링크를 알려 주면 구글 드라이브 연결로 읽는다.

claude.ai 일반 채팅의 Projects는 **필수가 아니다.** 휴대폰에서 지침서를 놓고 가볍게 묻고 싶을 때만 따로 만든다 (Projects → New project → 지침서 PDF와 `AGENTS.md` 올리기). 그 대화의 결과를 저장소에 반영할 때는 메인에게 넘긴다.

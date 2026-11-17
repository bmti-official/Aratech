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

## 7. Mac에 Gemini CLI 설치 (한 번만)

메인 에이전트(Claude)가 근거 수집과 렌즈 초안을 Gemini에게 맡기려면 Mac에 Gemini CLI가 있어야 한다. Gemini Pro 구독 계정으로 로그인한다.

1. **터미널 열기**: `⌘ + 스페이스` → `터미널` 입력 → Enter
2. **Node.js 확인**: 아래를 붙여 넣고 Enter
   ```bash
   node -v
   ```
   - `v20` 이상 숫자가 나오면 3번으로
   - `command not found`가 나오면 https://nodejs.org 에서 **LTS** 버전 macOS 설치 파일(.pkg)을 받아 설치한 뒤, 터미널을 닫았다가 다시 열고 `node -v`를 다시 확인
3. **Gemini CLI 설치**: 아래를 붙여 넣고 Enter. Mac 로그인 비밀번호를 물으면 입력한다 (입력해도 화면에 안 보이는 게 정상)
   ```bash
   sudo npm install -g @google/gemini-cli
   ```
4. **로그인**: 아래를 실행
   ```bash
   gemini
   ```
   - 처음 화면에서 색 테마는 아무거나 고르고 Enter
   - 로그인 방법은 **Login with Google** → 브라우저가 열리면 **Gemini Pro를 구독한 Google 계정**으로 로그인 → 허용
   - 터미널에 입력창이 나오면 성공. `/quit` 입력 후 Enter로 나온다
5. **확인**: 아래를 실행해 답이 나오면 끝
   ```bash
   gemini -p "안녕이라고만 답해"
   ```

## 8. 메인 에이전트와 일하기

사람은 **Mac에서 연 Claude Code 세션 하나(메인 에이전트)** 와만 대화한다. Gemini 로그인은 Mac에만 있으므로 메인도 Mac에서 열어야 Gemini에게 일을 시킬 수 있다.

1. 저장소를 Mac에 내려받기 (한 번만). 터미널에서:
   ```bash
   git clone https://github.com/bmti-official/Aratech.git ~/Aratech
   ```
   개발자 도구 설치 창이 뜨면 **설치**를 누르고, 끝나면 같은 명령을 다시 실행한다.
2. Claude 데스크톱 앱 → **Code** 탭 → 폴더로 `~/Aratech`(홈 폴더의 Aratech)를 고른다.
3. 그 세션에서 평소처럼 말한다. 메인이 필요할 때 Gemini와 Claude 서브에이전트에게 일을 나눠 준다.

웹·휴대폰의 클라우드 세션에서는 Gemini를 쓸 수 없다. 그때 메인은 Gemini 몫을 Claude가 대신해도 되는지 먼저 묻는다.

지침서 PDF는 공개 저장소에 넣지 않는다. 권한을 제한한 구글 드라이브에 두고, 메인에게 링크를 알려 주면 구글 드라이브 연결로 읽는다.

claude.ai 일반 채팅의 Projects는 **필수가 아니다.** 휴대폰에서 지침서를 놓고 가볍게 묻고 싶을 때만 따로 만든다. 그 대화의 결과를 저장소에 반영할 때는 메인에게 넘긴다.

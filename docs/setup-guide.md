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

## 5. 승인 없이 바뀌지 않게 막기 (권장)

1. Settings → **Branches** → **Add branch ruleset** (또는 Add rule)
2. Ruleset name: `main 보호`, Enforcement status: **Active**
3. Target branches → **Include default branch**
4. 체크: **Require a pull request before merging**, **Require status checks to pass** → Add checks에서 `check` 추가
5. **Create**

## 5-1. PR 자동 열기 허용 (한 번만)

에이전트가 브랜치만 올리면 GitHub이 PR을 자동으로 열게 하는 설정이다.

1. Settings → 왼쪽 **Actions** → **General**
2. 맨 아래 **Workflow permissions**
3. **Allow GitHub Actions to create and approve pull requests** 체크 → **Save**

## 6. 매번 하는 일: PR 승인

에이전트가 작업을 끝내면 PR(변경 요청)이 올라온다. 코드는 볼 필요 없다.

1. 저장소 **Pull requests** 탭 → 맨 위 PR 클릭
2. 1분쯤 뒤 달리는 **📋 변경 요약** 댓글을 읽는다 (무엇이 바뀌었는지 한국어 문장 + 검사 결과)
3. 댓글 맨 아래 "승인하는 사람이 할 일"을 따른다
   - 👍 간단한 변경 → 요약이 맞으면 **Merge pull request** → **Confirm merge**
   - 🔍 검수 필요 → "검수용 문구"를 펼쳐 복사 → 새 Claude 대화에 붙여 넣기 → "검수 통과"면 Merge
   - ❌ 검사 오류 → Merge하지 않고 댓글로 "고쳐 주세요"
4. 1~2분 뒤 사이트에 반영

맞지 않으면 Merge하지 말고 댓글 칸에 고칠 점을 한국어로 적는다.

## 7. Claude 프로젝트 만들기

1. claude.ai → 왼쪽 **Projects** → **New project** → 이름 `Aratech`
2. 프로젝트 지식(Project knowledge)에 지침서 PDF와 이 저장소의 `AGENTS.md` 올리기
3. 가설 카드, 종합, 회의 요약은 이 프로젝트 안에서 대화한다
4. 검수는 같은 프로젝트에서 **새 대화**를 열어 한다

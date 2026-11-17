> 메인 메모(2026-11-18): Gemini 수집본. 메인이 원문으로 확인한 값만 site/data/posts.json P001과 sources.json S007~S015에 반영했다. 이 파일의 Nabla 개인 요금, Abridge 150곳, Linked Evidence, Olive RPA 표현 등은 원문 미확인.

# 해외 의료 기록·청구 자동화 AI 기업 4곳 조사 자료

- **주제**: 의료 기록·청구 자동화 AI 해외 기업 4곳: Abridge(미국), Ambience Healthcare(미국), Nabla(프랑스·미국), Olive AI(미국, 폐업)
- **유형**: 유사 모델 (`posts.json` 분류 기준)
- **작성·확인일**: `2026-11-18`
- **등급 기준**: `A` (회사 공식 발표·보도자료·공시), `B` (언론 보도·업계 전문 매체), `null` (미확인)

---

## 1. 4개사 핵심 비교 요약표 (사실 기준)

| 기업명 (국가) | 제품 형태 | 주요 고객 | 수익 모델 | 배포 방식 | 최근 발표 기업 가치 (발표 시점) | 누적 투자금 (발표 시점) | 상태 | 출처 등급 |
|---|---|---|---|---|---|---|---|---|
| **Abridge** (미국) | 진료 대화 실시간 음성 인식(Ambient AI) 임상 노트 생성 + 원문 음성 근거 연결(Linked Evidence) + 진료 시점 코딩·사전 승인 연계 플랫폼 | 미국 대형 병원 네트워크(Health Systems)·상급종합병원 (Kaiser Permanente, Mayo Clinic, Johns Hopkins 등 150개 이상 의료기관) | B2B 엔터프라이즈 연간 라이선스 계약 (세부 단가 미확인) | EMR 네이티브 내장 (Epic Haiku·Hyperdrive 직접 연동 등) 및 모바일·웹 앱 | **$5.3B** (2025-06 시리즈 E 발표 기준) | 약 **$750M 이상** (2025-06 시리즈 E 보도 기준) | 운영 중 | A / B |
| **Ambience Healthcare** (미국) | 외래·응급실·입원 특화 실시간 임상 기록(AutoScribe) + 실시간 청구 코딩(AutoCode)·임상 문서 무결성(AutoCDI)·진료 의뢰(AutoRefer) 통합 AI | 미국 대형 의료기관·대학병원 (UCSF, Cleveland Clinic, Houston Methodist, Memorial Hermann 등) | B2B 엔터프라이즈 계약 (세부 단가 미확인) | EMR 워크플로우 내장 연동 (Epic, Oracle Cerner, athenahealth 등) | **$1.25B** (2025-07 시리즈 C 보도 기준) | 약 **$343M** (2025-07 시리즈 C 발표 후 합산 보도 기준) | 운영 중 | A / B |
| **Nabla** (프랑스·미국) | 다국어 진료 음성 기반 임상 노트 자동 생성(Nabla Copilot) 및 코딩·EHR 명령 실행을 돕는 에이전틱 AI 어시스턴트 | 개인 개원의·중소 클리닉 및 대형 의료기관 소속 임상의 (누적 85,000명 이상 임상의 및 130개 이상 의료 조직) | 개인·소규모 구독형 SaaS (Pro 월 **$119**/인, 무료 체험 제공) + 엔터프라이즈 맞춤형 계약 (단가 미확인) | 크롬 브라우저 확장 프로그램(Chrome Extension), 웹 앱, 데스크톱·모바일 앱 + 주요 EMR(Epic, Cerner, athenahealth 등) 연동 | **미확인** (2025-06 시리즈 C 발표 시 기업 가치 비공개) | **$120M** (2025-06 시리즈 C 발표 기준) | 운영 중 | A / B |
| **Olive AI** (미국, 폐업) | 병원 행정·수익주기관리(RCM) 업무(사전 승인, 보험 자격 확인, 청구 클리어링하우스 등) RPA·AI 자동화 플랫폼 | 미국 병원·의료 시스템 행정 및 재무(RCM) 부서 (한때 미국 내 900개 이상 병원 고객 발표) | B2B 엔터프라이즈 계약 (구체 단가 미확인) | 병원 레거시 시스템·EMR 위 RPA(로보틱 처리 자동화) 봇 및 엔터프라이즈 통합 방식 | 최고 기업 가치 **$4.0B** (2021-07 투자 발표 기준) / **2023-10 폐업** | 약 **$852M~$902M** (2021-07 투자 라운드 후 보도 기준) | 폐업·핵심 사업 분할 매각 (2023-10) | A / B |

---

## 2. 기업별 상세 조사 (사실과 해석 분리)

### 2-1. Abridge (미국)

#### [사실 (출처 확인)]

| 항목 | 확인된 사실 요약 | 등급 | 출처 및 원문 링크 | 확인일 |
|---|---|---|---|---|
| **제품 형태** | 진료 중 의사와 환자의 대화를 인식해 구조화된 임상 기록(SOAP 노트 등) 초안을 생성하는 앰비언트(Ambient) AI 플랫폼이다. 생성된 요약 문장을 클릭하면 원본 대화 오디오·텍스트 구간을 즉시 확인하는 'Linked Evidence' 기능을 제공하며, 임상 기록 단계에서 청구 코드·사전 승인(Prior Authorization) 등 수익주기관리(RCM) 워크플로우를 연결하는 컨텍스트 추론 엔진(Contextual Reasoning Engine)을 탑재했다. | A | Abridge 공식 발표 ([Series D 발표](https://www.abridge.com/blog/abridge-announces-250m-series-d-investment-and-new-contextual-reasoning-engine), [Series E 발표](https://www.abridge.com/blog/abridge-secures-300m-series-e)) | 2026-11-18 |
| **고객** | 미국 대형 병원 네트워크(Health Systems)와 학술의료센터가 주 고객이다. Kaiser Permanente(산하 40개 병원·600개 이상 진료소 배포), Mayo Clinic, Johns Hopkins Medicine, UPMC, Emory Healthcare 등 150개 이상의 대형 의료 시스템에서 사용되며 연간 5,000만 건 이상의 환자 진료를 지원하는 것으로 발표되었다. | A | Kaiser Permanente 공식 보도자료 ([Kaiser Permanente News](https://about.kaiserpermanente.org/news/kaiser-permanente-improves-member-experience-with-ai-enabled-clinical-technology)), Abridge 공식 발표 ([Series E 발표](https://www.abridge.com/blog/abridge-secures-300m-series-e)) | 2026-11-18 |
| **수익 모델** | 개별 의사 대상 셀프서비스가 아닌 대형 의료기관 대상 B2B 엔터프라이즈 계약 모델을 운영한다. 병원별 구체적인 계약 금액 및 단가 산정 방식은 공개되지 않았다 (**세부 가격 미확인**). | B | Fierce Healthcare ([Series E 보도](https://www.fiercehealthcare.com/ai-and-machine-learning/generative-ai-company-abridge-scores-300m-series-e-backed-a16z-and-khosla)) | 2026-11-18 |
| **배포 방식** | 2023년 8월 미국 최대 EMR 기업 Epic의 'Partners and Pals' 프로그램 최초 파트너로 선정되어, 별도 외부 창 복사·붙여넣기 없이 Epic 모바일 앱(Haiku)과 데스크톱·웹(Hyperdrive) 워크플로우 내부에 네이티브로 내장 배포된다. | B | Fierce Healthcare ([Epic 파트너십 보도](https://www.fiercehealthcare.com/health-tech/abridge-inks-epic-partnership-emory-healthcare-tie-umbra-its-generative-ai-tech)) | 2026-11-18 |
| **기업 가치·누적 투자** | - **2025년 2월 (Series D)**: **$250M** 투자 유치 (Elad Gil, IVP 공동 리드). 보도된 기업 가치는 **$2.75B**.<br>- **2025년 6월 (Series E, 최근 공식 발표)**: **$300M** 투자 유치 (Andreessen Horowitz(a16z) 주도, Khosla Ventures 참여). 발표된 기업 가치는 **$5.3B** (53억 달러)이며, 누적 투자금은 약 **$750M 이상**으로 보도되었다. | A / B | Abridge 공식 발표 ([Series E 발표](https://www.abridge.com/blog/abridge-secures-300m-series-e), 등급 A), Fierce Healthcare ([Series E 및 $5.3B 기업가치 보도](https://www.fiercehealthcare.com/ai-and-machine-learning/generative-ai-company-abridge-scores-300m-series-e-backed-a16z-and-khosla), 등급 B) | 2026-11-18 |
| **성공·실패 관련 사실** | 100개 이상의 전문 진료과와 28개 이상 언어를 지원하며, Mayo Clinic·Epic과 함께 간호사 업무 워크플로우 공동 개발을 진행 중이다. 또한 의료 보험 청구·사전 승인 네트워크 기업인 Availity 등과 협력해 진료실 대화 시점에 보험 청구 및 사전 승인 근거를 자동 생성하는 영역으로 확장했다. | A / B | Abridge 공식 발표 ([Series E 발표](https://www.abridge.com/blog/abridge-secures-300m-series-e), 등급 A), Fierce Healthcare ([Series E 보도](https://www.fiercehealthcare.com/ai-and-machine-learning/generative-ai-company-abridge-scores-300m-series-e-backed-a16z-and-khosla), 등급 B) | 2026-11-18 |

#### [해석 (에이전트 분석)]
- **유통 해자(Distribution Moat) 선점**: 미국 병원 EMR 시장 점유율 1위인 Epic의 'Pal' 파트너십을 가장 먼저 확보해, 의사가 기존 EMR 화면을 벗어나지 않고 노트를 승인할 수 있게 만든 점이 대형 병원(Kaiser Permanente, Mayo Clinic 등) 엔터프라이즈 계약을 빠르게 석권한 결정적 요인으로 해석된다.
- **신뢰성 검증 UI와 수익주기(RCM) 결합**: 의료 AI 도입의 최대 걸림돌인 '환각(Hallucination)' 문제를 원문 오디오 매핑(Linked Evidence) 인터페이스로 해결해 임상의 신뢰를 얻었고, 단순 기록 시간 단축을 넘어 병원의 실질적 매출과 직결되는 청구 코딩·사전 승인 자동화로 확장해 병원 재무 의사결정권자(CFO)의 지불 의사를 끌어냈다.

---

### 2-2. Ambience Healthcare (미국)

#### [사실 (출처 확인)]

| 항목 | 확인된 사실 요약 | 등급 | 출처 및 원문 링크 | 확인일 |
|---|---|---|---|---|
| **제품 형태** | 의료기관용 통합 AI 운영체제를 표방하며, 실시간 임상 기록 자동화(**AutoScribe**), 실시간 ICD-10·CPT 청구 코딩 지원(**AutoCode**), 임상 문서 무결성·누락 검토(**AutoCDI**), 진료 의뢰서 작성(**AutoRefer**), 환자용 방문 요약(**AutoAVS**) 제품군을 제공한다. 외래뿐만 아니라 복잡한 응급실(ED)·입원 병동 및 100개 이상의 세부 전문과목에 맞춘 모델을 제공한다. | A | Ambience Healthcare 공식 발표 ([Series B 보도자료](https://www.prnewswire.com/news-releases/ambience-healthcare-raises-70m-to-scale-the-most-comprehensive-ai-operating-system-for-healthcare-organizations-302054170.html), [Series C 블로그 발표](https://www.ambiencehealthcare.com/blog/ambience-healthcare-announces-243-million-series-c-to-scale-its-ai-platform-for-health-systems)) | 2026-11-18 |
| **고객** | 미국 내 주요 학술의료센터 및 대형 의료 시스템인 UCSF Health, Cleveland Clinic, Houston Methodist, Memorial Hermann, John Muir Health 등을 고객으로 확보했다. | A / B | Ambience Healthcare 공식 발표 ([Series C 발표](https://www.ambiencehealthcare.com/blog/ambience-healthcare-announces-243-million-series-c-to-scale-its-ai-platform-for-health-systems), 등급 A), Fierce Healthcare ([Series C 보도](https://www.fiercehealthcare.com/ai-and-machine-learning/ambience-reels-in-243m-series-c-investors-continue-bet-big-ambient-ai), 등급 B) | 2026-11-18 |
| **수익 모델** | 대형 병원 및 의료 네트워크 대상 B2B 엔터프라이즈 계약 모델이다. 구체적인 기관별 계약 단가 및 과금 체계는 외부에 공개되지 않았다 (**세부 가격 미확인**). | B | Fierce Healthcare ([Series C 보도](https://www.fiercehealthcare.com/ai-and-machine-learning/ambience-reels-in-243m-series-c-investors-continue-bet-big-ambient-ai)) | 2026-11-18 |
| **배포 방식** | Epic, Oracle Cerner, athenahealth 등 대형 병원의 핵심 EMR 시스템 워크플로우 내부에 직접 통합(EHR-embedded)되어 작동한다. | A / B | Ambience Healthcare 공식 발표 ([Series B 보도자료](https://www.prnewswire.com/news-releases/ambience-healthcare-raises-70m-to-scale-the-most-comprehensive-ai-operating-system-for-healthcare-organizations-302054170.html), 등급 A), Fierce Healthcare ([Series C 보도](https://www.fiercehealthcare.com/ai-and-machine-learning/ambience-reels-in-243m-series-c-investors-continue-bet-big-ambient-ai), 등급 B) | 2026-11-18 |
| **기업 가치·누적 투자** | - **2024년 2월 (Series B)**: **$70M** 투자 유치 (Kleiner Perkins, OpenAI Startup Fund 공동 리드).<br>- **2025년 7월 (Series C, 최근 공식 발표)**: **$243M** 투자 유치 (Oak HC/FT, Andreessen Horowitz(a16z) 공동 리드). 보도된 최근 기업 가치는 **$1.25B** (12억 5,000만 달러)이며, 누적 투자금은 약 **$343M** 수준으로 보도되었다. | A / B | Ambience Healthcare 공식 발표 ([Series C 발표](https://www.ambiencehealthcare.com/blog/ambience-healthcare-announces-243-million-series-c-to-scale-its-ai-platform-for-health-systems), 등급 A), Fierce Healthcare ([Series C 및 $1.25B 기업가치 보도](https://www.fiercehealthcare.com/ai-and-machine-learning/ambience-reels-in-243m-series-c-investors-continue-bet-big-ambient-ai), 등급 B) | 2026-11-18 |
| **성공·실패 관련 사실** | 초기부터 단순 요약 노트가 아니라 청구 규정 준수(Coding compliance)와 CDI(임상 문서 무결성)를 진료 시점(Point of care)에 동시 처리하는 기능을 전면에 내세웠으며, 일반 외래 진료 외에 워크플로우가 까다로운 응급실(Cleveland Clinic, Houston Methodist 등)과 입원 환자 영역에서 도입 사례를 만들었다. | A / B | Ambience Healthcare 공식 발표 ([Series C 발표](https://www.ambiencehealthcare.com/blog/ambience-healthcare-announces-243-million-series-c-to-scale-its-ai-platform-for-health-systems), 등급 A), Fierce Healthcare ([Series C 보도](https://www.fiercehealthcare.com/ai-and-machine-learning/ambience-reels-in-243m-series-c-investors-continue-bet-big-ambient-ai), 등급 B) | 2026-11-18 |

#### [해석 (에이전트 분석)]
- **초기부터 코딩·청구 무결성(CDI)을 결합한 포지셔닝**: 다수의 AI 스크라이브가 '의사 번아웃 감소'라는 정성적 효과에 머물 때, Ambience는 진료 후 별도 청구 부서가 사후 검토하던 CDI·코딩 작업을 진료 시점으로 앞당겨 '청구 누락 방지 및 보험 삭감 감소'라는 직접적인 재무 ROI를 제시한 점이 차별화 요인으로 분석된다.
- **고난도 분과(응급실·입원·세부 전문과) 공략**: 비교적 정형화된 1차 외래 진료를 넘어 응급실(ED)과 분과별 특수 템플릿을 빠르게 지원함으로써 대형 상급종합병원 전체 계약으로 확장할 수 있는 기반을 마련했다.

---

### 2-3. Nabla (프랑스·미국)

#### [사실 (출처 확인)]

| 항목 | 확인된 사실 요약 | 등급 | 출처 및 원문 링크 | 확인일 |
|---|---|---|---|---|
| **제품 형태** | 프랑스 파리와 미국 뉴욕에 기반을 둔 임상 AI 기업으로, 다국어(영어·프랑스어·스페인어 등 35개 이상 언어) 진료를 실시간 전사·요약해 임상 노트를 만드는 'Nabla Copilot'에서 출발해, 최근 진료 코딩 지원·EHR 명령 실행·간호 워크플로우를 포괄하는 '적응형 에이전틱 플랫폼(Adaptive Agentic Platform)'으로 확장했다. | A | Nabla 공식 보도자료 ([Series C PR Newswire](https://www.prnewswire.com/news-releases/nabla-raises-70m-series-c-to-deliver-agentic-ai-to-the-heart-of-clinical-workflows-bringing-total-funding-to-120m-302483646.html), [Nabla 공식 블로그](https://www.nabla.com/blog/70m-series-c-just-getting-started)) | 2026-11-18 |
| **고객** | 개인 개원의·소규모 의원부터 미국 대형 의료 네트워크(University of Iowa Health Care, Children's Hospital Los Angeles, Carilion Clinic, Denver Health 등 130개 이상 의료 조직)까지 폭넓게 확보했다. 2025년 6월 발표 기준 85,000명 이상의 임상의가 현장에서 사용 중이다. | A | Nabla 공식 보도자료 ([Series C PR Newswire](https://www.prnewswire.com/news-releases/nabla-raises-70m-series-c-to-deliver-agentic-ai-to-the-heart-of-clinical-workflows-bringing-total-funding-to-120m-302483646.html)) | 2026-11-18 |
| **수익 모델** | 셀프서비스형 개인·클리닉 구독(PLG)과 B2B 엔터프라이즈 계약을 병행한다. 개인 임상의 대상 Pro 플랜은 무료 체험 후 **월 $119(USD)** 정액 구독 모델을 제공해 왔으며, 다수 의료진이 소속된 병원·그룹에는 별도 맞춤형 엔터프라이즈 가격(구체 단가 미확인)을 적용한다. | B | Fierce Healthcare ([Series C 보도](https://www.fiercehealthcare.com/ai-and-digital-health/nabla-banks-70m-series-c-to-build-out-agentic-ai-clinical-workflows)) | 2026-11-18 |
| **배포 방식** | **크롬 브라우저 확장 프로그램(Chrome Extension)**, 웹 앱, 데스크톱·모바일 앱 형태로 제공되어 별도 병원 IT 구축 없이도 웹 기반 EMR 화면 위에서 바로 쓸 수 있으며, 동시에 Epic, Oracle Cerner, athenahealth, NextGen 등 주요 EMR과의 직접 연동도 지원한다. | A / B | Nabla 공식 보도자료 ([Series B PR Newswire](https://www.prnewswire.com/news-releases/nabla-raises-24m-in-series-b-to-fuel-expansion-of-its-ambient-ai-assistant-to-transform-care-delivery-302027132.html), [Series C PR Newswire](https://www.prnewswire.com/news-releases/nabla-raises-70m-series-c-to-deliver-agentic-ai-to-the-heart-of-clinical-workflows-bringing-total-funding-to-120m-302483646.html), 등급 A) | 2026-11-18 |
| **기업 가치·누적 투자** | - **2024년 1월 (Series B)**: **$24M** 투자 유치 (Cathay Innovation 리드, ZEBOX Ventures 참여).<br>- **2025년 6월 (Series C, 최근 공식 발표)**: **$70M** 투자 유치 (HV Capital 리드, Highland Europe, DST Global 등 참여). 총 누적 투자금은 **$120M** (1억 2,000만 달러)이다.<br>- **최근 기업 가치**: **미확인** (2025년 6월 시리즈 C 공식 발표 및 주요 보도에서 기업 가치를 공개하지 않음). | A / B | Nabla 공식 보도자료 ([Series B 발표](https://www.prnewswire.com/news-releases/nabla-raises-24m-in-series-b-to-fuel-expansion-of-its-ambient-ai-assistant-to-transform-care-delivery-302027132.html), [Series C 발표](https://www.prnewswire.com/news-releases/nabla-raises-70m-series-c-to-deliver-agentic-ai-to-the-heart-of-clinical-workflows-bringing-total-funding-to-120m-302483646.html), 등급 A), Fierce Healthcare ([Series C 보도](https://www.fiercehealthcare.com/ai-and-digital-health/nabla-banks-70m-series-c-to-build-out-agentic-ai-clinical-workflows), 등급 B) | 2026-11-18 |
| **성공·실패 관련 사실** | 공동창업자 Alex Lebrun(전 Facebook AI Research 디렉터 출신) 등 유럽 AI 연구 인력을 바탕으로 자체 소형화·최적화 음성 및 임상 언어 모델을 구축했으며, 환자 음성 데이터를 서버에 저장하지 않는 프라이버시 설계와 가벼운 브라우저 확장 프로그램 배포를 통해 출시 후 단기간에 85,000명 이상의 임상의 사용자를 확보했다. | A / B | Nabla 공식 보도자료 ([Series C PR Newswire](https://www.prnewswire.com/news-releases/nabla-raises-70m-series-c-to-deliver-agentic-ai-to-the-heart-of-clinical-workflows-bringing-total-funding-to-120m-302483646.html), 등급 A), Fierce Healthcare ([Series C 보도](https://www.fiercehealthcare.com/ai-and-digital-health/nabla-banks-70m-series-c-to-build-out-agentic-ai-clinical-workflows), 등급 B) | 2026-11-18 |

#### [해석 (에이전트 분석)]
- **브라우저 확장 프로그램(Chrome Extension)을 통한 빠른 상향식(Bottom-up) 확산**: 대형 병원 IT 부서의 느린 EMR 통합 승인을 기다리지 않고, 개별 의사나 클리닉이 크롬 확장 프로그램과 웹 앱으로 즉시 써볼 수 있게 한 제품 주도 성장(PLG) 전략이 Abridge·Ambience 대비 적은 자본($120M)으로도 85,000명 이상의 사용자를 빠르게 모은 핵심 동력으로 풀이된다.
- **국내 및 비영어권·중소 의료기관 시사점**: 단일 대형 EMR 독점 구조가 아니거나 병원 IT 연동 비용이 높은 환경에서는, Nabla처럼 브라우저 확장 프로그램·가벼운 앱 형태로 진입 장벽을 낮춘 뒤 기관 계약으로 전환하는 배포 방식이 초기 검증에 유리함을 보여준다.

---

### 2-4. Olive AI (미국, 폐업)

#### [사실 (출처 확인)]

| 항목 | 확인된 사실 요약 | 등급 | 출처 및 원문 링크 | 확인일 |
|---|---|---|---|---|
| **제품 형태** | 병원 행정 업무와 수익주기관리(RCM)—보험 사전 승인(Prior Authorization), 환자 보험 자격 확인, 청구 클리어링하우스(Clearinghouse), 재고·구매 관리 등—를 로보틱 처리 자동화(RPA)와 AI로 자동화하는 엔터프라이즈 소프트웨어 플랫폼을 표방했다. | B | Fierce Healthcare ([2021년 $400M 투자 보도](https://www.fiercehealthcare.com/health-tech/olive-rakes-in-400m-to-turbocharge-growth-humanized-ai-for-healthcare), [2023년 폐업 보도](https://www.fiercehealthcare.com/health-tech/once-high-flying-unicorn-olive-ai-sells-two-key-businesses-winds-down-operations)) | 2026-11-18 |
| **고객** | 미국 내 병원 및 의료 시스템의 재무·행정·수익주기관리(RCM) 부서를 고객으로 삼았으며, 전성기 기준 미국 내 900개 이상의 병원에서 사용된다고 발표했다. | B | Fierce Healthcare ([2021년 $400M 투자 보도](https://www.fiercehealthcare.com/health-tech/olive-rakes-in-400m-to-turbocharge-growth-humanized-ai-for-healthcare)) | 2026-11-18 |
| **수익 모델** | 병원·의료 시스템 단위 B2B 엔터프라이즈 계약 모델로 운영되었다 (구체적 계약 단가 미확인). | B | Fierce Healthcare ([2023년 폐업 보도](https://www.fiercehealthcare.com/health-tech/once-high-flying-unicorn-olive-ai-sells-two-key-businesses-winds-down-operations)) | 2026-11-18 |
| **배포 방식** | 병원의 기존 EMR 및 행정·청구 소프트웨어 화면과 데이터베이스 위에서 사람 대신 클릭·입력을 수행하는 RPA(로보틱 처리 자동화) 봇 및 API·엔터프라이즈 통합 방식으로 배포되었다. | B | Fierce Healthcare ([2021년 $400M 투자 보도](https://www.fiercehealthcare.com/health-tech/olive-rakes-in-400m-to-turbocharge-growth-humanized-ai-for-healthcare), [2023년 폐업 보도](https://www.fiercehealthcare.com/health-tech/once-high-flying-unicorn-olive-ai-sells-two-key-businesses-winds-down-operations)) | 2026-11-18 |
| **최고 기업 가치·누적 투자** | - **최고 기업 가치 시점 (2021년 7월)**: Vista Equity Partners가 주도하고 Base10 Partners, General Catalyst, Tiger Global 등이 참여한 라운드에서 **$400M**을 조달하며 최고 기업 가치 **$4.0B** (40억 달러)를 기록했다.<br>- **누적 투자금**: 약 **$852M~$902M** (보도 매체별 약 $852M 또는 $900M 이상으로 집계). | B | Fierce Healthcare ([2021년 7월 $400M 투자 및 $4B 기업가치 보도](https://www.fiercehealthcare.com/health-tech/olive-rakes-in-400m-to-turbocharge-growth-humanized-ai-for-healthcare), [2023년 10월 폐업 보도](https://www.fiercehealthcare.com/health-tech/once-high-flying-unicorn-olive-ai-sells-two-key-businesses-winds-down-operations)) | 2026-11-18 |
| **폐업·사업 매각 시점과 경위** | - **2022년 7월~2023년 초 구조조정**: 2022년 7월 직원 450명 해고, 2023년 2월 추가 215명(당시 인력의 35%) 해고 및 핵심 영역(사전 승인·환자 접근·클리어링하우스) 외 사업 축소를 단행했다.<br>- **2023년 10월 31일 폐업 및 핵심 사업 매각 발표**: 유동성 위기와 채무 상환 압박 속에 완전 폐업(Wind down)을 발표했다. 폐업 과정에서 핵심 자산 중 **클리어링하우스(Clearinghouse) 및 환자 접근(Patient Access) 사업부는 의료 결제 기업 Waystar**에 매각했고, **사전 승인(Prior Authorization) 사업부는 Humata Health**에 매각한 뒤 잔여 법인 영업을 종료했다. | A / B | Fierce Healthcare ([2023-10-31 폐업 및 매각 보도](https://www.fiercehealthcare.com/health-tech/once-high-flying-unicorn-olive-ai-sells-two-key-businesses-winds-down-operations), 등급 B), Waystar 공식 보도자료 ([Olive AI 고객 인수 발표](https://www.waystar.com/press-release/waystars-immediate-focus-on-olive-ai-clients/), 등급 A) | 2026-11-18 |
| **실패 요인 관련 보도 사실** | 공격적인 기업 인수(Verata Health, Empiric Health 등)와 무리한 외형 확장으로 인한 현금 소진(Cash burn), 병원 고객사들의 계약 해지(Churn), 그리고 도입한 RPA 자동화 봇이 병원 시스템 변경 시 자주 오작동해 약속한 ROI를 달성하지 못했다는 고객 불만과 언론 지적이 이어졌다. | B | Fierce Healthcare ([2023-10-31 폐업 보도](https://www.fiercehealthcare.com/health-tech/once-high-flying-unicorn-olive-ai-sells-two-key-businesses-winds-down-operations)) | 2026-11-18 |

#### [해석 (에이전트 분석)]
- **깨지기 쉬운 RPA(화면 스크래핑) 기술의 한계와 과대 포장**: 생성형 AI 이전 세대인 Olive AI는 병원 EMR·청구 시스템의 UI가 조금만 바뀌어도 멈추는 RPA 스크립트를 '자율 AI'로 포장해 판매했으나, 유지보수에 막대한 인력이 투입되고 실제 병원 현장의 자동화 체감도가 낮아 재계약 실패로 이어졌다.
- **검증 전 무리한 다각화 vs 핵심 워크플로우 집중의 교훈**: 단일 워크플로우에서 확실한 제품-시장 적합성(PMF)과 재계약률을 증명하기 전에 대규모 투자금으로 여러 인접 사업과 플랫폼을 인수·확장한 것이 치명적 패인이었다. 반면 폐업 시에도 '사전 승인(Humata 인수)'과 '클리어링하우스(Waystar 인수)'처럼 명확한 청구 병목을 해결하던 개별 모듈만은 생존해 매각되었다는 점은, 초기에는 좁고 명확한 행정·기록 병목 하나를 깊이 해결해야 함을 시사한다.

---

## 3. 종합 시사점 (해석)

1. **기록 자동화에서 청구·수익주기(RCM)로의 필연적 결합**: Abridge와 Ambience 모두 진료실 음성 기록(Scribe)으로 시작했으나, 수십억 달러 기업 가치를 인정받은 핵심 동력은 진료 기록을 **청구 코드(ICD-10/CPT), 사전 승인, 임상 문서 무결성(CDI)**으로 직결해 병원의 재무적 수익 손실을 막아준 데 있다.
2. **배포 방식의 이원화 전략 (EMR 내장 vs 브라우저 확장)**: 대형 상급종합병원 시장에서는 Epic 등 주류 EMR 내부 내장(Abridge, Ambience)이 필수적이었으나, 개별 임상의·클리닉을 빠르게 침투할 때는 IT 통합 없이 즉시 작동하는 크롬 확장 프로그램·웹 앱(Nabla)이 유효한 진입 경로로 작동했다.
3. **Olive AI 폐업이 주는 반증 교훈**: 기술적 안정성과 실제 현장의 반복 사용률(Retention)이 검증되기 전에 '병원 전체 AI 운영체제'로 범위를 넓히면 유지보수 비용과 고객 이탈로 무너진다.

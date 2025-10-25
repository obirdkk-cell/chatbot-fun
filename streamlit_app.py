import time

def get_user_age():
    """사용자로부터 연령을 입력받는 함수"""
    while True:
        try:
            age_input = input("🙂 안녕하세요! 학습 도우미 챗봇입니다. 학습을 시작하기 전에, 사용자님의 연령을 숫자로 입력해주세요: ")
            age = int(age_input)
            if 5 <= age <= 100:  # 합리적인 연령 범위 설정
                return age
            else:
                print("🤔 연령을 올바르게 입력해주세요.")
        except ValueError:
            print("🚨 죄송하지만, 연령은 숫자로만 입력해주세요.")

# --- 연령별 응답 함수 (가상의 예시) ---

def get_learning_response_for_child(query):
    """어린이용 응답 로직: 쉬운 비유와 친근한 어투"""
    # 실제로는 간단한 규칙 기반 또는 소형 모델 사용
    if "태양계" in query:
        return "☀️ 태양계는 거대한 가족 같아요! 태양이 아빠고, 행성들은 태양 주변을 도는 아이들이죠. 알았지? 참 잘했어요!👍"
    return f"🌟 묻고 싶은 게 뭐야? {query}에 대해 더 쉽게 설명해 줄게!"

def get_learning_response_for_teen(query):
    """청소년용 응답 로직: 개념 설명과 심화 질문 유도"""
    # 실제로는 중형 모델 또는 학습 커리큘럼 기반 응답
    if "미분" in query:
        return "📈 미분은 변화율을 구하는 핵심 개념이야. 접선의 기울기를 찾는 거랑 같지. 어떤 부분이 헷갈려? 관련 예제를 풀어볼까?"
    return f"📚 네 질문인 '{query}'에 대해 깊이 있는 설명을 준비했어. 좀 더 구체적으로 물어봐 줄래?"

def get_learning_response_for_adult(query):
    """성인용 응답 로직: 실용적 적용과 요약 강조"""
    # 실제로는 대형 모델 또는 전문 지식 기반 응답
    if "머신러닝" in query:
        return "💻 머신러닝은 데이터를 통해 학습하는 AI의 핵심 분야입니다. 비즈니스 적용 사례(추천 시스템, 예측 모델)를 중심으로 요약해 드릴까요?"
    return f"✅ '{query}'에 대한 전문적인 답변입니다. 어떤 정보가 가장 필요하신가요?"

# --- 메인 챗봇 루프 ---

def run_learning_chatbot():
    """챗봇 실행 함수"""
    user_age = get_user_age()
    
    # 3. 연령에 따른 응답 로직 분기
    if user_age < 13:
        response_func = get_learning_response_for_child
        print("👶 자, 이제 챗봇 친구와 신나게 공부해 보자!")
    elif 13 <= user_age <= 18:
        response_func = get_learning_response_for_teen
        print("🧑‍🎓 반갑습니다! 학습 목표 달성을 도와드릴게요.")
    else: # 19세 이상
        response_func = get_learning_response_for_adult
        print("💼 안녕하세요. 효율적인 정보 습득을 지원합니다.")

    print("---")
    
    while True:
        user_input

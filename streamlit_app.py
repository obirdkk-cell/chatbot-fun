import os
from google import genai
from google.genai import types

# 1. API 키 설정 (보안을 위해 환경 변수 사용 권장)
# os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY_HERE"

# 클라이언트 초기화
try:
    client = genai.Client()
except Exception as e:
    print("🚨 API 클라이언트 초기화 실패: API 키가 올바르게 설정되었는지 확인하세요.")
    print(f"오류: {e}")
    exit()

# --- 2. 연령별 프롬프트 시스템 메시지 정의 ---

def get_system_prompt(age):
    """사용자 연령에 맞는 챗봇의 역할과 말투를 정의하는 시스템 프롬프트를 생성합니다."""
    
    if age < 13:
        # 어린이 (초등학생 이하)
        style = "매우 친절하고, 밝고, 재미있는 유치원 또는 초등학교 선생님입니다. 어려운 단어는 절대 쓰지 않고, 쉬운 비유와 칭찬(예: '참 잘했어요!')을 사용하며, 이모티콘(😊, 🌟)을 적절히 활용하세요. 답변은 항상 2~3문장 이내로 짧게 마무리하세요."
    elif 13 <= age <= 18:
        # 청소년 (중고등학생)
        style = "친근하지만 전문적인 지식을 갖춘 과외 선생님이자 멘토입니다. 학습 목표에 집중하며, 개념을 명확하게 설명하고, 심화 학습을 유도하는 질문을 던져주세요. 답변은 4~5문장 정도로 구성하며, 격려는 적당히 사용하세요."
    else:
        # 성인 (대학생 및 일반)
        style = "고급 지식을 제공하는 전문 컨설턴트 또는 대학 교수입니다. 공식적이고 전문적인 어투를 사용하며, 핵심 정보를 빠르게 요약하고, 실무적인 적용 사례나 심층적인 배경 지식을 제공하는 데 중점을 두세요."
        
    return (
        f"당신은 {age}세 사용자의 학습을 돕는 AI 도우미 챗봇입니다. 당신의 페르소나는 다음과 같습니다: {style} "
        "사용자가 묻는 학습 질문에 대해 당신의 페르소나와 스타일에 맞춰 답변하세요."
    )

# --- 3. 사용자 연령 입력 및 챗봇 실행 로직 ---

def get_user_age():
    """사용자로부터 연령을 입력받는 함수"""
    while True:
        try:
            age_input = input("🙂 안녕하세요! 학습 도우미 챗봇입니다. 학습을 시작하기 전에, 사용자님의 연령을 숫자로 입력해주세요 (5~100): ")
            age = int(age_input)
            if 5 <= age <= 100:
                return age
            else:
                print("🤔 연령을 5세에서 100세 사이의 숫자로 입력해주세요.")
        except ValueError:
            print("🚨 죄송하지만, 연령은 숫자로만 입력해주세요.")

def run_learning_chatbot():
    """챗봇 실행 함수"""
    user_age = get_user_age()
    
    # 3-1. 연령에 따른 시스템 프롬프트 설정
    system_prompt = get_system_prompt(user_age)
    
    print("-" * 30)
    print(f"🤖 챗봇이 {user_age}세 사용자님을 위한 맞춤형 학습 도우미로 설정되었습니다.")
    print("👉 이제 학습 질문을 입력해주세요. (종료하려면 '종료')")
    print("-" * 30)
    
    # 3-2. LLM 설정 및 대화 시작
    
    # 모델 설정: 시스템 프롬프트를 사용하여 챗봇의 역할 정의
    config = types.GenerateContentConfig(
        system_instruction=system_prompt
    )
    
    # 대화 세션 시작 (대화 기록 유지)
    chat = client.chats.create(
        model="gemini-2.5-flash", # 빠르고 효율적인 모델 선택
        config=config,
    )
    
    while True:
        user_input = input("🙋 사용자: ")
        
        if user_input.lower() == '종료':
            print("👋 학습을 종료합니다. 다음에 또 만나요!")
            break
        
        if not user_input.strip():
            continue
            
        try:
            # 3-3. LLM에 질문 전송 및 답변 받기
            print("🤖 챗봇: 생각 중...")
            response = chat.send_message(user_input)
            
            # 3-4. LLM 응답 출력
            print(f"🤖 챗봇: {response.text}\n")
            
        except Exception as e:
            print(f"🚨 LLM 응답 중 오류가 발생했습니다: {e}")
            break

if __name__ == "__main__":
    run_learning_chatbot()

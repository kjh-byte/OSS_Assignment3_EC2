import streamlit as st
import time

@st.cache_data
def load_quiz_database():
    time.sleep(2)
    return [
        {
            "id": 1, "type": "객관식",
            "question": "시험 끝! 종강 기념으로 해외여행 갈 때 내 우선순위는?",
            "options": ["📸 무조건 인생샷! 남는 건 사진뿐임", "🌲 사람 많은 거 질색.. 힐링이 필요해", "🏛️ 박물관, 유적지 뽕 뽑아야지", "🌃 화려한 도시 야경 보면서 칵테일 한 잔"],
            "points": [10, 20, 30, 40]
        },
        {
            "id": 2, "type": "OX",
            "question": "나는 여행 갈 때 구글 지도에 별표 50개쯤 찍어놓는 '파워 J'다. (O/X)",
            "options": ["O (계획 없으면 불안함)", "X (그냥 발길 닿는 대로 감)"],
            "points": [10, 5]
        },
        {
            "id": 3, "type": "다지선다",
            "question": "내 캐리어에 절대 빼놓을 수 없는 필수템 2개만 고르면? (다지선다)",
            "options": ["보조배터리랑 고프로", "편한 슬리퍼랑 트레이닝복", "종이 지도랑 필기도구", "선글라스랑 힙한 착장"],
            "points": [5, 5, 5, 5]
        },
        {
            "id": 4, "type": "유형판별",
            "question": "게스트하우스에서 외국인이 'Where are you from?' 하고 말을 건다면?",
            "options": ["'I'm from Korea!' 바로 인스타 맞팔 고고", "웃으면서 하이 하고 조용히 내 침대로 감", "파파고 켜서라도 근처 로컬 맛집 물어봄", "오늘 밤에 파티 하냐고 슬쩍 물어봄"],
            "points": [10, 20, 30, 40]
        },
        {
            "id": 5, "type": "점수합산",
            "question": "이번 여행을 위해 내가 모은 소중한 알바비 예산은?",
            "options": ["돈 아껴서 길게 가자! 가성비 모드 (10점)", "쓸 땐 쓰고 아낄 땐 아끼자 (20점)", "나를 위한 선물! 플렉스 하러 감 (30점)"],
            "points": [10, 20, 30]
        },
        {
            "id": 6, "type": "객관식",
            "question": "현지 음식이 입에 안 맞는다면 당신의 선택은?",
            "options": ["참고 먹는다, 이것도 경험이지!", "미리 챙겨온 비장의 고추장을 꺼낸다", "스타벅스나 맥도날드 같은 아는 맛을 찾는다", "구글 평점 4.5 이상인 다른 맛집을 턴다"],
            "points": [30, 10, 20, 40]
        },
        {
            "id": 7, "type": "객관식",
            "question": "여행 마지막 날, 지인들 기념품은 어떻게 챙기나요?",
            "options": ["드럭스토어에서 가장 핫한 템으로 싹쓸이", "현지 느낌 낭낭한 마그넷이나 엽서", "기념품 살 돈으로 내 선물을 하나 더 산다", "공항 면세점에서 남은 돈 탈탈 턴다"],
            "points": [10, 30, 20, 40]
        }
    ]

def main():
    st.set_page_config(page_title="재희의 여행 성향 분석", layout="centered", page_icon="✈️")

    st.sidebar.title("📁 과제 정보")
    st.sidebar.markdown(f"""
    - **과목명**: 오픈소스소프트웨어실습
    - **학기**: 2026년 1학기
    - **학번**: 2025404006
    - **이름**: 김재희
    """)
    st.sidebar.markdown("---")

    st.title("✈️ 나만의 맞춤 해외 여행지 추천 서비스")
    st.markdown("#### 🎓 오픈소스소프트웨어실습 중간고사 대체 과제")
    st.info("**제출자**: 김재희 (학번: 2025404006)")
    st.divider()

    if 'login_active' not in st.session_state:
        st.session_state.login_active = False

    if not st.session_state.login_active:
        st.subheader("🔐 시스템 보안 로그인")
        input_id = st.text_input("아이디 (학번)").strip()
        input_pw = st.text_input("비밀번호 (영문 성함)", type="password", help="영문으로 'kimjaehee'를 입력하세요.").strip()

        if st.button("로그인"):
            if input_id == "2025404006" and input_pw.lower() == "kimjaehee":
                st.session_state.login_active = True
                st.success("인증 성공! 김재희 님 환영합니다.")
                st.rerun()
            else:
                st.error("학번 또는 비밀번호가 틀렸습니다.")
    
    else:
        st.success("✅ 로그인 상태: 김재희 (2025404006)")
        quiz_data = load_quiz_database()
        
        with st.form("travel_quiz_form"):
            st.subheader("📝 7가지 유형별 정밀 분석 퀴즈")
            total_score = 0
            
            for item in quiz_data:
                st.write(f"**Q{item['id']}. {item['question']}**")
                
                if item['type'] == "다지선다":
                    selected = st.multiselect("최대 2개 선택 가능", item['options'], max_selections=2, key=f"q{item['id']}")
                    for s in selected:
                        idx = item['options'].index(s)
                        total_score += item['points'][idx]
                elif item['type'] == "OX":
                    choice = st.radio("선택", item['options'], horizontal=True, key=f"q{item['id']}")
                    idx = item['options'].index(choice)
                    total_score += item['points'][idx]
                elif item['type'] == "객관식":
                    choice = st.selectbox("답변 선택", item['options'], key=f"q{item['id']}")
                    idx = item['options'].index(choice)
                    total_score += item['points'][idx]
                else:
                    choice = st.radio("가장 가까운 답변", item['options'], key=f"q{item['id']}")
                    idx = item['options'].index(choice)
                    total_score += item['points'][idx]
                st.write("") 

            submitted = st.form_submit_button("종합 분석 결과 확인")
            
            if submitted:
                st.balloons() 
                st.divider()
                
                if total_score <= 80: result = "MZ핫플형 (일본 도쿄 추천)"
                elif total_score <= 130: result = "자연힐링형 (스위스 융프라우 추천)"
                elif total_score <= 170: result = "역사탐방형 (이집트 피라미드 추천)"
                else: result = "도심야경형 (홍콩 빅토리아 피크 추천)"
                
                st.header(f"🌟 분석 결과: {result}")
                st.info(f"당신의 총점은 {total_score}점입니다. 취향 저격 여행지로 떠나보세요!")

        if st.sidebar.button("로그아웃"):
            st.session_state.login_active = False
            st.rerun()

if __name__ == "__main__":
    main()
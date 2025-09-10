import streamlit as st
import random
import time

# ------------------------
# 랜덤 단어 100개 생성 (2~8글자, 한글 조합)
# ------------------------
def generate_word_list(num_words=100):
    chosung = list("가나다라마바사아자차카타파하")
    jungsung = list("ㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣ")
    word_list = []
    for _ in range(num_words):
        length = random.randint(2, 8)
        word = "".join(random.choice(chosung) + random.choice(jungsung) for _ in range(length))
        word_list.append(word)
    return word_list

# ------------------------
# 세션 상태 초기화
# ------------------------
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "word_list" not in st.session_state:
    st.session_state.word_list = generate_word_list()
if "current_word" not in st.session_state:
    st.session_state.current_word = random.choice(st.session_state.word_list)
if "word_count" not in st.session_state:
    st.session_state.word_count = 0
if "total_words" not in st.session_state:
    st.session_state.total_words = 10
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# ------------------------
# 단어 제출 함수
# ------------------------
def submit_word():
    elapsed_time = time.time() - st.session_state.start_time
    st.session_state.start_time = time.time()  # 다음 단어용 시간 초기화

    # 맞으면 시간 기반 점수, 틀리면 0점
    if st.session_state.input_text == st.session_state.current_word:
        base_score = len(st.session_state.current_word)
        speed_bonus = max(1, int((3 - elapsed_time) * 10))  # 3초 기준
        st.session_state.score += base_score * speed_bonus

    st.session_state.word_count += 1

    # 게임 종료 또는 다음 단어
    if st.session_state.word_count >= st.session_state.total_words:
        st.session_state.game_started = False  # 게임 종료 후 시작 화면으로
        st.success(f"게임 종료! 최종 점수: {st.session_state.score}")
    else:
        st.session_state.current_word = random.choice(st.session_state.word_list)
    
    st.session_state.input_text = ""  # 입력창 초기화

# ------------------------
# 게임 시작 화면
# ------------------------
if not st.session_state.game_started:
    st.title("타자 연습 고난도 버전")
    st.write("게임을 시작하려면 아래 버튼을 눌러주세요!")
    if st.button("게임 시작"):
        st.session_state.game_started = True
        st.session_state.start_time = time.time()
        st.session_state.word_count = 0
        st.session_state.score = 0
        st.session_state.current_word = random.choice(st.session_state.word_list)

# ------------------------
# 게임 화면
# ------------------------
if st.session_state.game_started:
    st.title("빠른 타자 게임 ⏱")
    st.write(f"점수: {st.session_state.score}")
    st.write(f"단어 {st.session_state.word_count+1}/{st.session_state.total_words}")
    st.subheader(st.session_state.current_word)

    # Enter만으로 제출
    st.text_input(
        "단어 입력 후 Enter",
        key="input_text",
        on_change=submit_word
    )

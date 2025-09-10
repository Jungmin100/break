import streamlit as st
import random
import time

# ------------------------
# 세션 상태 초기화
# ------------------------
if "score" not in st.session_state:
    st.session_state.score = 0
if "word_list" not in st.session_state:
    st.session_state.word_list = ["축제", "게임", "프로그래밍", "재미", "코딩", "참여", "도전", "점수"]
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
# 타이틀 및 상태 표시
# ------------------------
st.title("빠른 타자 게임 ⏱")
st.write(f"점수: {st.session_state.score}")
st.write(f"단어 {st.session_state.word_count+1}/{st.session_state.total_words}")
st.subheader(st.session_state.current_word)

# ------------------------
# 입력창
# ------------------------
st.session_state.input_text = st.text_input("단어 입력", value=st.session_state.input_text, key="input_box")

# ------------------------
# 단어 확인 및 점수 계산
# ------------------------
if st.session_state.input_text == st.session_state.current_word and st.session_state.input_text != "":
    elapsed_time = time.time() - st.session_state.start_time
    st.session_state.start_time = time.time()

    # 점수 계산: 빠를수록 높음 (0.1초 단위 보너스)
    base_score = len(st.session_state.current_word)
    speed_bonus = max(1, int((3 - elapsed_time) * 10))  # 3초 기준
    gained_score = base_score * speed_bonus
    st.session_state.score += gained_score

    st.session_state.word_count += 1
    st.session_state.input_text = ""  # 입력 초기화

    # 다음 단어 설정 또는 게임 종료
    if st.session_state.word_count >= st.session_state.total_words:
        st.success(f"게임 종료! 최종 점수: {st.session_state.score}")
    else:
        st.session_state.current_word = random.choice(st.session_state.word_list)

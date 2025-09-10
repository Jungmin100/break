import streamlit as st
import random
import time

# 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.word_list = ["축제", "게임", "프로그래밍", "재미", "코딩", "참여", "도전", "점수"]
    st.session_state.current_word = random.choice(st.session_state.word_list)
    st.session_state.word_count = 0
    st.session_state.total_words = 10
    st.session_state.start_time = time.time()

st.title("빠른 타자 게임 ⏱")
st.write(f"점수: {st.session_state.score}")
st.write(f"단어 {st.session_state.word_count+1}/{st.session_state.total_words}")

st.subheader(st.session_state.current_word)

# 입력
user_input = st.text_input("단어 입력", value="", key="input_box")

if user_input == st.session_state.current_word:
    # 시간 계산
    elapsed_time = time.time() - st.session_state.start_time  # 단어 입력에 걸린 시간
    st.session_state.start_time = time.time()  # 다음 단어 측정 시작

    # 점수 계산: 빠를수록 높음 (예: 0.1초 당 보너스)
    base_score = len(st.session_state.current_word)
    speed_bonus = max(1, int((3 - elapsed_time) * 10))  # 3초 기준, 빠를수록 보너스 높음
    gained_score = base_score * speed_bonus
    st.session_state.score += gained_score

    st.session_state.word_count += 1
    if st.session_state.word_count >= st.session_state.total_words:
        st.success(f"게임 종료! 최종 점수: {st.session_state.score}")
    else:
        st.session_state.current_word = random.choice(st.session_state.word_list)
    st.experimental_rerun()

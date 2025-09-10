import streamlit as st
import time

# 초기화
if "grid" not in st.session_state:
    st.session_state.grid = [[1 for _ in range(7)] for _ in range(3)]  # 벽돌
    st.session_state.ball_pos = [5, 3]  # y, x
    st.session_state.ball_dir = [-1, 1]  # dy, dx
    st.session_state.paddle_x = 3
    st.session_state.score = 0
    st.session_state.game_over = False

ROWS, COLS = 10, 7

# 화면 렌더링 함수
def render():
    grid_display = ""
    for y in range(ROWS):
        row = ""
        for x in range(COLS):
            if y < len(st.session_state.grid) and st.session_state.grid[y][x] == 1:
                row += "🟥"
            elif [y, x] == st.session_state.ball_pos:
                row += "⚪"
            elif y == ROWS-1 and st.session_state.paddle_x <= x < st.session_state.paddle_x+3:
                row += "🟦"
            else:
                row += "⬛"
        grid_display += row + "\n"
    st.text(grid_display)

# 공 이동
def move_ball():
    if st.session_state.game_over:
        return

    ball_y, ball_x = st.session_state.ball_pos
    dy, dx = st.session_state.ball_dir

    new_y, new_x = ball_y + dy, ball_x + dx

    # 벽 충돌
    if new_x < 0 or new_x >= COLS:
        dx *= -1
    if new_y < 0:
        dy *= -1

    # 패들 충돌
    if new_y == ROWS-1 and st.session_state.paddle_x <= new_x < st.session_state.paddle_x+3:
        dy *= -1

    # 벽돌 충돌
    if 0 <= new_y < len(st.session_state.grid) and st.session_state.grid[new_y][new_x] == 1:
        st.session_state.grid[new_y][new_x] = 0
        dy *= -1
        st.session_state.score += 10

    # 공 위치 갱신
    st.session_state.ball_pos = [ball_y + dy, ball_x + dx]
    st.session_state.ball_dir = [dy, dx]

    # 게임 오버 체크
    if st.session_state.ball_pos[0] >= ROWS:
        st.session_state.game_over = True

move_ball()

st.title("벽돌깨기 🎮")
render()
st.write(f"점수: {st.session_state.score}")

if st.session_state.game_over:
    st.error("게임 오버! 😢")

# 패들 좌우 버튼
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("◀"):
        st.session_state.paddle_x = max(0, st.session_state.paddle_x-1)
with col3:
    if st.button("▶"):
        st.session_state.paddle_x = min(COLS-3, st.session_state.paddle_x+1)

# 게임 리셋
if st.button("게임 리셋"):
    st.session_state.clear()
    st.experimental_rerun()

# 자동 새로고침
if not st.session_state.game_over:
    time.sleep(0.2)
    st.experimental_rerun()

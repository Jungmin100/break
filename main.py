import streamlit as st
import random
import time

# ------------------------
# 단어 리스트 -> 짧은 파이썬 코드 100개
# ------------------------
word_list = [
"print('Hello World!')","print(1 + 1)","print(10 - 3)","print(2 * 5)","print(10 / 2)",
"print(10 // 3)","print(10 % 3)","print(2 ** 3)","print('Python' + ' Rocks!')","print('A' * 5)",
"for i in range(5): print(i)","for i in range(1,6): print(i*i)","nums = [1,2,3]; print(nums)",
"nums = list(range(5)); print(nums)","print([x*2 for x in range(5)])","print([x**2 for x in range(6)])",
"x = 5; print(x)","x = 10; y = 20; print(x+y)","x = 'Hello'; y = 'World'; print(x+y)","x = 'Python'; print(x[0])",
"x = 'Python'; print(x[-1])","x = 'Python'; print(x[1:4])","mylist = [1,2,3]; print(mylist[1])",
"mylist = [0]*5; print(mylist)","mylist = [1,2,3,4,5]; print(mylist[:3])","print(list('Python'))",
"x = 10; print(x>5)","x = 3; print(x==3)","x = 5; print(x!=3)","x = 2; print(x<5 and x>0)","x = 4; print(x>0 or x<0)",
"x = 5 if 3>2 else 10; print(x)","def f(): return 10; print(f())","def add(a,b): return a+b; print(add(2,3))",
"x = [1,2,3]; x.append(4); print(x)","x = [1,2,3,4]; x.pop(); print(x)","x = [1,2,3,4]; x.remove(2); print(x)",
"x = [1,2,3]; print(len(x))","x = [5,3,1]; x.sort(); print(x)","x = [5,3,1]; x.reverse(); print(x)",
"x = ['a','b','c']; print(' '.join(x))","x = 'Hello World'; print(x.split())","print('Python'.upper())",
"print('Python'.lower())","print('  Hello  '.strip())","print('Python'.replace('Py','J'))","x = 10; x += 5; print(x)",
"x = 10; x -= 3; print(x)","x = 2; x *= 3; print(x)","x = 10; x /= 2; print(x)","x = [1,2,3]; print(sum(x))",
"x = [1,2,3]; print(max(x))","x = [1,2,3]; print(min(x))","x = [1,2,3]; print(sorted(x))","x = [1,2,3]; print(list(reversed(x)))",
"x = 0; print(bool(x))","x = 5; print(bool(x))","x = None; print(bool(x))","x = ['a','b','c']; print('b' in x)",
"x = ['a','b','c']; print('d' not in x)","x = range(5); print(list(x))","x = list(range(10)); print(x[::2])",
"x = list(range(10)); print(x[1::2])","x = [1,2,3]; y = [4,5,6]; print(x+y)","x = [1,2,3]; print(x*2)",
"x = {1,2,3}; print(2 in x)","x = {1,2,3}; print(len(x))","x = {'a':1,'b':2}; print(x['a'])","x = {'a':1,'b':2}; x['c']=3; print(x)",
"x = {'a':1,'b':2}; del x['b']; print(x)","x = {'a':1,'b':2}; print(list(x.keys()))","x = {'a':1,'b':2}; print(list(x.values()))",
"x = 10; print(bin(x))","x = 10; print(hex(x))","x = 10; print(oct(x))","x = 5; print(float(x))","x = 3.5; print(int(x))",
"x = '123'; print(int(x))","x = '3.14'; print(float(x))","x = 5; print(abs(x))","x = -5; print(abs(x))","x = 16; print(x**0.5)",
"round(3.14159,2); print(round(3.14159,2))","x = 'Python'; print(list(x))","x = 'Python'; print(x[::-1])",
"x = [1,2,3]; print([i*2 for i in x])","x = [1,2,3]; print([i**2 for i in x])","x = range(5); print([i*2 for i in x])",
"x = [1,2,3]; print([i+1 for i in x if i>1])","x = 'hello'; print(' '.join(x))","x = 'a,b,c'; print(x.split(','))",
"x = [1,2,3,4]; print(sum(x)/len(x))","x = list(range(5)); print([i%2==0 for i in x])","x = [1,2,3]; print(list(map(lambda x:x*2, x)))",
"x = [1,2,3]; print(list(filter(lambda x:x>1, x)))","x = [1,2,3,4]; print(any(i>3 for i in x))","x = [1,2,3,4]; print(all(i>0 for i in x))",
"x = 'Python'; print(any(c.isupper() for c in x))","x = 'Python'; print(all(c.isalpha() for c in x))","x = [1,2,3]; print(min(x)+max(x))",
"x = [1,2,3]; print(sum(x)**2)","x = 'abc'; print(''.join(reversed(x)))","x = [1,2,3]; y=[4,5,6]; print([a+b for a,b in zip(x,y)])",
"x = [1,2,3]; print(list(reversed(x)))","x = [1,2,3]; print(list(range(len(x))))","x = [1,2,3]; print(x.index(2))",
"x = [1,2,3]; x.insert(1,100); print(x)","x = [1,2,3,4,5]; print(x[::2])","x = [1,2,3,4,5]; print(x[1::2])",
"x = [1,2,3]; x.extend([4,5]); print(x)","x = ['a','b','c']; print([s.upper() for s in x])","x = [1,2,3]; print(list(map(lambda x:x+1,x)))",
"x = [1,2,3,4]; print([i*i for i in x if i%2==0])","x = 'hello'; print(x.capitalize())","x = 'hello world'; print(x.title())",
"x = 'hello world'; print(x.replace('world','Python'))","x = 10; print(str(x))","x = 5; print(bool(x==5))",
"x = [1,2,3]; print(sum([i for i in x if i>1]))"
]

# ------------------------
# 세션 상태 초기화
# ------------------------
if "game_started" not in st.session_state:
    st.session_state.game_started = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_word" not in st.session_state:
    st.session_state.current_word = random.choice(word_list)
if "word_count" not in st.session_state:
    st.session_state.word_count = 0
if "total_words" not in st.session_state:
    st.session_state.total_words = 10
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# ------------------------
# 컨테이너 생성
# ------------------------
container = st.empty()

# ------------------------
# 단어 제출 함수
# ------------------------
def submit_word():
    elapsed_time = time.time() - st.session_state.start_time
    st.session_state.start_time = time.time()  # 다음 단어용 시간 초기화

    # 맞으면 시간 기반 점수, 틀리면 0점
    if st.session_state.input_text == st.session_state.current_word:
        base_score = len(st.session_state.current_word)
        speed_bonus = max(1, int((3 - elapsed_time) * 10))
        st.session_state.score += base_score * speed_bonus

    st.session_state.word_count += 1

    if st.session_state.word_count >= st.session_state.total_words:
        st.session_state.game_started = False
        container.empty()  # 게임 화면 제거
        st.success(f"게임 종료! 최종 점수: {st.session_state.score}")
    else:
        st.session_state.current_word = random.choice(word_list)
    
    st.session_state.input_text = ""  # 입력창 초기화

# ------------------------
# 게임 시작 화면
# ------------------------
if not st.session_state.game_started:
    with container.container():
        st.title("타자 연습 고난도 버전")
        st.write("게임을 시작하려면 아래 버튼을 눌러주세요!")
        if st.button("게임 시작"):
            st.session_state.game_started = True
            st.session_state.start_time = time.time()
            st.session_state.word_count = 0
            st.session_state.score = 0
            st.session_state.current_word = random.choice(word_list)
            container.empty()  # 시작 화면 제거

# ------------------------
# 게임 화면
# ------------------------
if st.session_state.game_started:
    with container.container():
        st.title("빠른 타자 게임 ⏱")
        st.write(f"점수: {st.session_state.score}")
        st.write(f"단어 {st.session_state.word_count+1}/{st.session_state.total_words}")
        st.subheader(st.session_state.current_word)

        st.text_input(
            "단어 입력 후 Enter",
            key="input_text",
            on_change=submit_word
        )

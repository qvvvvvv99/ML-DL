# 모듈 로딩 ------------------------------------------------------------------
import cgi, os.path
from pydoc import html
import joblib, sys, codecs
import cgitb

# cgi 기능 활성화 설정 --------------------------------------------------------
cgitb.enable()

# --------------------------------------------------------------------------
# 함수 선언
# --------------------------------------------------------------------------
# 텍스트 입력 양식 출력 함수 ---------------------------------------------------
def show_form(text, msg=""):
    print("Content-Type : text/html; charset=utf-8")
    print("")
    print("""
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>언어판별</title>
        </head>
        <body>
        <form>
            <textarea name="text" rows="8" cols="40">{0}</textarea>
            <p><input type="submit" value="판정"></p>
            <p>{1}</p>
        </form>
        </body>
        </html>
    """.format(text, msg))

def detect_lang(text):
    text=text.lower()
    code_a, code_z=(ord("a"), ord("z"))
    cnt=[0 for i in range(26)]
    for ch in text:
        n=ord(ch) - code_a
        if 0 <= n < 26: cnt[n] += 1
    total=sum(cnt)
    if total == 0: return "입력이 없습니다"
    freq=list(map(lambda n: n/total, cnt))
    # 언어 예측하기
    res=clf.predict([freq])
    lang_dic={"en":"영어", "fr":"프랑스어","id":"인도네시아어", "tl":"타갈로그어"}
    return lang_dic[res[0]]

# 기능 구현
# (1) WEB 인코딩 설정
sys.stdout=codecs.getwriter('utf-8')(sys.stdout.detach())

# (2) 학습 데이터 읽기
pklfile=os.path.dirname(__file__) + "/lang.pkl"
clf=joblib.load(pklfile)

# (3) 입력 양식의 값 읽어 들이기
form=cgi.FieldStorage()
text=form.getvalue("text", default="")
msg=""
if text != "":
    lang=detect_lang(text)
    msg="판정 결과 : "+ lang
show_form(text, msg)
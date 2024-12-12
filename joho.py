import streamlit as st
import time

# カスタムCSSの追加
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f8ff;
    }
    .title {
        font-size: 2.5em;
        color: #2e8b57;
        text-align: center;
        margin-bottom: 20px;
    }
    .question {
        font-size: 1.2em;
        margin-top: 10px;
        color: #4169e1;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# タイトル
st.markdown('<div class="title">🎢 どのテーマパークに行く？ 🎠</div>', unsafe_allow_html=True)

st.write("テーマパークに行きたいけど、どこに行こうか迷っているそこのあなた🌟")
st.write("診断を通して、あなたにピッタリのテーマパークを見つけましょう！")

# 質問セクション
st.markdown("### 📝 以下の質問に答えてください")
q1 = st.radio("👫 一緒に行く人を教えてください", ("友達", "恋人", "家族", "1人で"))
q2 = st.radio("📍 どこから行くか教えてください", ("関東", "関西"))
q3 = st.radio("🌈 世界観に浸って素敵な時間を過ごしたい？", ("はい", "いいえ"))
q4 = st.radio("🎢 スリルを味わいたい気分？", ("はい", "いいえ"))
q5 = st.radio("📸 写真をたくさん撮りたい？", ("はい", "いいえ"))
q6 = st.radio("🗣️ 方言が好き？", ("はい", "いいえ"))
q7 = st.radio("☀️ 暑いより寒いほうが好き？", ("はい", "いいえ"))
q8 = st.radio("🏯 東京の都市より奈良京都で時代を感じるほうが好き？", ("はい", "いいえ"))

# 結果を見るボタン
if st.button("🎉 結果を見る！"):
    st.write("診断結果を計算中...🌟")
    
    # アニメーション付きの診断中表示
    with st.spinner("少々お待ちください...🌟"):
        time.sleep(3)

    # 回答を数値に変換 (x軸, y軸)
    x = 0
    y = 0
    if q1 in ["恋人", "家族"]:
        x += 1.1
    else:
        x -= 1.1
    if q2 == "関東":
        y += 3
    else:
        y -= 3
    if q3 == "はい":
        x += 1.2
    else:
        x -= 1.2
    if q4 == "はい":
        x -= 1.3
    else:
        x += 1.3
    if q5 == "はい":
        x += 1.4
    else:
        x -= 1.4
    if q6 == "はい":
        y -= 1.2
    else:
        y += 1.2
    if q7 == "はい":
        y += 1.3
    else:
        y -= 1.3
    if q8 == "はい":
        y -= 1.4
    else:
        y += 1.4

    # 判定ロジック
    if x > 0 and y > 0:
        result = "Disney"
        image_path = "disney.jpg"
        caption = "夢の国ディズニーへようこそ！ 🏰✨"
        video_link = "https://youtu.be/AvEehDyyUt8?feature=shared"
        homepage_link = "https://www.tokyodisneyresort.jp/"
    elif x > 0 and y < 0:
        result = "USJ"
        image_path = "usj.jpg"
        caption = "映画の世界が広がるUSJへ！ 🎥🎢"
        video_link = "https://youtu.be/xkwcnffhTLY?feature=shared"
        homepage_link = "https://www.usj.co.jp/"
    elif x < 0 and y > 0:
        result = "富士急ハイランド"
        image_path = "fujiq.jpg"
        caption = "絶叫マシンの聖地、富士急！ 🎡🗻"
        video_link = "https://youtu.be/SWSk_lUCBJ8?feature=shared"
        homepage_link = "https://www.fujiq.jp/"
    else:
        result = "ナガシマスパーランド"
        image_path = "nagashima.jpg"
        caption = "温泉も楽しめるナガシマスパーランド！ 🛁🎠"
        video_link = "https://youtu.be/Kki1V9L9PUk?feature=shared"
        homepage_link = "https://www.nagashima-onsen.co.jp/spaland/"

    # 結果の表示
    st.write(f"あなたは **{result}** へ行くべきです！")
    st.image(image_path, caption=caption)
    st.write(f"🎥 [公式プロモーション動画を観る]({video_link})")
    st.write(f"🌐 [公式ホームページはこちら]({homepage_link})")


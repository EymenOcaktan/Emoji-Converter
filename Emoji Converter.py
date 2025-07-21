emoji_map = {
    "love": "❤️",
    "heart": "❤️",
    "happy": "😊",
    "smile": "😄",
    "sad": "😢",
    "cry": "😭",
    "angry": "😠",
    "laugh": "😂",
    "cool": "😎",
    "kiss": "😘",
    "sleep": "😴",
    "ok": "👌",
    "yes": "✅",
    "no": "❌",
    "star": "⭐",
    "fire": "🔥",
    "sun": "☀️",
    "moon": "🌙",
    "cloud": "☁️",
    "rain": "🌧️",
    "snow": "❄️",
    "pizza": "🍕",
    "burger": "🍔",
    "fries": "🍟",
    "coffee": "☕",
    "tea": "🫖",
    "water": "💧",
    "cat": "🐱",
    "dog": "🐶",
    "rabbit": "🐰",
    "panda": "🐼",
    "lion": "🦁",
    "tiger": "🐯",
    "car": "🚗",
    "bus": "🚌",
    "bike": "🚲",
    "train": "🚆",
    "rocket": "🚀",
    "book": "📚",
    "pen": "🖊️",
    "phone": "📱",
    "computer": "💻",
    "tv": "📺",
    "money": "💰",
    "gift": "🎁",
    "music": "🎵",
    "party": "🥳",
    "clap": "👏",
    "thumbs": "👍",
    "100": "💯",
    "check": "✔️",
    "cross": "❌",
    "danger": "⚠️",
    "time": "⏰",
    "clock": "🕒",
    "game": "🎮",
    "soccer": "⚽",
    "basketball": "🏀",
    "tennis": "🎾",
    "school": "🏫",
    "home": "🏠",
    "work": "💼"
}

sentence = input("Please enter your sentence: ")
sentence = sentence.lower()
words = sentence.split()
converted = []
for x in words:
    if x in emoji_map:
        converted.append(emoji_map[x])
    else:
        converted.append(x)
new_sentence = " ".join(converted)
print(new_sentence)
def detect_language(text):
    for char in text:
        if '\u3040' <= char <= '\u30ff' or '\u4e00' <= char <= '\u9faf':
            return "ja"
    return "en"

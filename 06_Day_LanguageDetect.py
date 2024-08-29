from langdetect import detect

def detect_language(text):
    try:
        language = detect(text)
        return language
    except:
        return "Unable to detect language"

# Example usage
sample_text = "Hello, how are you?"


detected_lang = detect_language(sample_text)
print(f"Detected language: {detected_lang}")

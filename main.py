from morse_code_translator import MorseCodeTranslator

morse_translator = MorseCodeTranslator()

def translate_text():
    original_text = input("Enter text: ").lower()
    result = morse_translator.translate_text(original_text)
    print(result)


if __name__ == "__main__":
	translate_text()
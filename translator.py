import re
import time
from deep_translator import GoogleTranslator


def translate_line(line):
    match = re.match(r"^(.*)=(.*)$", line)
    if match:
        prefix = match.group(1).strip() 
        text = match.group(2).strip()
        if text:
            try:
                translated = GoogleTranslator(source='en', target='ru').translate(text)
                print(f"Перевод: '{text}' -> '{translated}'")
                return f"{prefix}={translated}"
            except Exception as e:
                print(f"Ошибка перевода строки: {line}. Причина: {e}")
                return line
    return line.strip()


input_file = "original version/en_us.lang"
output_file = "russian version/en_us.lang"

start_time = time.time()

with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        if line.strip().startswith("#") or line.strip() == "":
            outfile.write(line)
        else:
            translated_line = translate_line(line)
            outfile.write(translated_line + "\n")

end_time = time.time()


elapsed_time = end_time - start_time
print(f"Перевод завершен. Время выполнения: {elapsed_time:.2f} секунд.")
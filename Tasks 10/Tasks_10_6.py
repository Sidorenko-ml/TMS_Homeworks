#В конец существующего текстового файла записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры

with open(r'C:\Users\sidor\TMS\Tasks 10\Tasks10_5.txt','a') as file:
    file.writelines(['Дописываю первую строку\n','Дописал вторую\n','А теперь и третью заканчиваю\n'])
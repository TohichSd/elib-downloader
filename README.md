### Программа позволяет скачивать книги из электронной библиотеки МЭИ в формате pdf

## Инструкция

При первом запуске программа попросит логин и пароль - это ваш логин и пароль от электронной библиотеки.
Программа сохранит их в файл _config.json_ и использует при последующих запусках.

Далее программа попросит ID книги. Его можно найти взглянув на ссылку на книгу - она должна выглядеть примерно так:  
http://elib.mpei.ru/action.php?kt_path_info=ktcore.SecViewPlugin.actions.document&fDocumentId=1234  
ID книги указан в поле **_DocumentId_** - в данном случае ID равен **_1234_**.

После ввода ID, программа постепенно скачает все страницы книги (они временно хранятся в папке tmp и будут удалены по завершении работы программы) и склеит их в файл **result.pdf**, который будет сохранён в той же папке, где и сама программа.
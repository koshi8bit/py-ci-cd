# py-ci-cd
[![Tests and deploy](https://github.com/koshi8bit/py-ci-cd/actions/workflows/deploy.yml/badge.svg)](https://github.com/koshi8bit/py-ci-cd/actions/workflows/deploy.yml)

Настройка CI CD для проекта на python в github

Пуш в мастер запрещен. В мастер можно фигачить только через *pull request*. Настройка этой опции
[тут](https://github.com/koshi8bit/py-ci-cd/settings/branches). Подставьте свой аккаунт и название репы в ссылке.

Перед pull реквестом в *master* происходит прогон пайплайна, описанного [тут](.github/workflows/deploy.yml).
В него входит:
- Инициализация нужной версии python.
- Установка всех зависимостей из requirements.txt.
- Проверка синтаксиса кода по PEP8 при помощи flake8.
- Запуск всех [юнит тестов](tests/) из папки.
 
Перед пушем в мастер происходит все, что описано выше, но добавляется процесс деплоя на хостинг:
- Запаковка кода в docker контейнер.
- Пуш в dockerhub. При этом образ имеет вид `username/github-repo-name_branch-name:commit_hash`. 
  Такой подход позволит легко вернуться в рабочую версию в случае горения жёп.
- Создание контейнера в виде файла и сжатие его перед отправкой на хостинг (устарело, загрузка в dockerhub лучше, т.к.
  тогда заливается только diff. Но если интересно - можно посмотреть шаги в файле _.github\workflows\deploy.yml.7z_ на этапе _Create locally_).
- Отправка архива контейнера на хостинг через csp (устарело, см выше).
- Подготовка приватного SSH ключа для хостинга из "секретов" гитхаба.
- В этом пайпе представлены примеры удалённого запуска кода на хостинге и пример передачи файла
- Запуск docker контейнера на хостинге при помощи `docker-compose` через SSH. Рабочий развернутый проект [на хостинге amazon](http://ec2-18-220-152-128.us-east-2.compute.amazonaws.com:5000/api/v2/foo). Исходный код [тут](src/main.py) **В МОЕМ ПРИМЕРЕ ОТКЛЮЧЁН HTTPS!** 
- PROFIT!!

Проект и документацию сделал **Лёха К** aka **koshi8bit** 

## Секреты
Пока не нашел, как в давать доступ к секретам разным разрабам. Наткнулся на такую "фишку".

Допустим есть репа, в которой работают два разраба: джун и сеньёр. Допустим сеньёр настроил CI-CD и прописал в секретах IP сервака и приватный ключ и настроил деплой. Допустим сеньёр не хочет, чтобы джун лазил в тачку, на которую производится деплой.

Теперь кейс: джун создал ветку с новой фичей, реализовал ее и решил добавить эксплойт, который тырит приватный ключ SSH. 

Как оказалось, в гитхабе при пулл реквесте запуск CI производится из yml файла ветки, в только что работали. 
Соответственно пайп пожно изменить и запустить свой в любой момент и никто его не запретит запускать. И в своем 
ужа красть секреты. 

Вывести в консоль секреты не получится, в гитхабе это дело закрашивается звездочками. 
Через bace64 тоже. Тогда я написал скрипт, который сохраняет переменную в файл и передает ее на удаленный сервак.

```bash
DEBUG="$SERVER_ADDRES $(git log -1 --pretty=format:%h)"
ssh $SERVER_SSH_USER@$SERVER_ADDRES "echo '$DEBUG' > ~/debug.txt"
```

И получается можно в любой момент украсть всю мякотку, которая лежит в секретах гитхаба, если ты делаешь обычный пулл реквест.

Надеюсь я упустил какую-то деталь. Иначе любой автоматический деплой выглядит как дырявое Г.

В гитхабе есть настройка окружений, в целом это позволяет настроить уровни доступа к секретам при помощи 
_Branch protection rule_, но из-за того, что доступ к этим секретам можно получить в пайпе очень криво - нужно
делать много CTRL+C CTRL+V, а это выглядит не очень хорошо.

Тогда можно сделать "сборщик" yaml файла, который будет из темлейта подставлять в разные job'ы одинаковый код, 
но это уже какой-то костыль.. 

## Branch protection rule
Branch protection rule для веток ниже будет таким: `[dps][ert][voa]*`:
- dev
- prod
- stage

Абсолютно отвратительный паттерн, который берет 3 раза по каждой букве из каждого перечисления букв в [скобках]. Паттерн передается в _fnmatch_, 
который не умеет в _логическое или_. По сути - урезанная регулярка.

## Источники
- [Actions](https://youtu.be/WTofttoD2xg?t=82)
- [Docker + Actions](https://youtu.be/09lZdSpeHAk?t=80)
- [Actions на русском](https://youtu.be/hevU4NdIsoU)
- [Gitlab docker](https://youtu.be/RV0845KmsNI)
- [Моя таблица с командами для Docker](https://docs.google.com/spreadsheets/d/1XWuif-QDWUb66IGFz_dPtnHq3K8sGVm4_GctkrrSni4/edit#gid=882078486)
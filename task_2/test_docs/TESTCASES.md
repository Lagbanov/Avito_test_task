
### Проверка верстки счетчиков со значением "0"
### id: ТК-1
- шаги: 
- - открыть сайт `https://www.avito.ru/avito-care/eco-impact`
- - замокать json по запросу `web/1/charity/ecoImpact/init`:
```
{
  "result": {
    "blocks": {
      "personalImpact": {
        "data": {
          "co2": 0,
          "energy": 0,
          "materials": 0,
          "pineYears": 0,
          "water": 0
        }
      }
    },
    "isAuthorized": false
  },
  "status": "ok"
}
```
- ожидаемый результат:
- - 0 л воды
- - 0 кг СО2
- - 0 кВт.ч энергии
- - текст внутри счетчика с небольшой прозрачностью

### Проверка на вход граничного значения 
### id: ТК-2
- шаги: 
- - открыть сайт `https://www.avito.ru/avito-care/eco-impact`
- - замокать json по запросу `web/1/charity/ecoImpact/init`:
```
{
  "result": {
    "blocks": {
      "personalImpact": {
        "data": {
          "co2": 999,
          "energy": 999,
          "materials": 999,
          "pineYears": 999,
          "water": 999
        }
      }
    },
    "isAuthorized": false
  },
  "status": "ok"
}
```
- ожидаемый результат:
- - 999 л воды
- - 999 кг СО2
- - 999 кВт.ч энергии

### Проверка проверка на конвертацию при входе значения "1000" 
### id: ТК-3
- шаги: 
- - открыть сайт `https://www.avito.ru/avito-care/eco-impact`
- - замокать json по запросу `web/1/charity/ecoImpact/init`:
```
{
  "result": {
    "blocks": {
      "personalImpact": {
        "data": {
          "co2": 1000,
          "energy": 1000,
          "materials": 1000,
          "pineYears": 1000,
          "water": 1000
        }
      }
    },
    "isAuthorized": false
  },
  "status": "ok"
}
```
- ожидаемый результат:
- - 1000 л воды
- - 1000 кг СО2
- - 1000 кВт.ч энергии




### Проверка на округление при вход значения "1500" 
### id: ТК-4
- шаги: 
- - открыть сайт `https://www.avito.ru/avito-care/eco-impact`
- - замокать json по запросу `web/1/charity/ecoImpact/init`:
```
{
  "result": {
    "blocks": {
      "personalImpact": {
        "data": {
          "co2": 1500,
          "energy": 1500,
          "materials": 1500,
          "pineYears": 1500,
          "water": 1500
        }
      }
    },
    "isAuthorized": false
  },
  "status": "ok"
}
```
- ожидаемый результат:
- - 1500 л воды
- - 1500 кг СО2
- - 1500 кВт.ч энергии

### Проверка на конвертацию при входе значения 1.000.000
### id: ТК-5
- шаги: 
- - открыть сайт `https://www.avito.ru/avito-care/eco-impact`
- - замокать json по запросу `web/1/charity/ecoImpact/init`:
```
{
  "result": {
    "blocks": {
      "personalImpact": {
        "data": {
          "co2": 1000000,
          "energy": 1000000,
          "materials": 1000000,
          "pineYears": 1000000,
          "water": 1000000
        }
      }
    },
    "isAuthorized": false
  },
  "status": "ok"
}
```
- ожидаемый результат:
- - 1000000 л воды
- - 1000000 кг СО2
- - 1000000 кВт.ч энергии

### Проверка на обработку больших чисел
### id: ТК-6
- шаги: 
- - открыть сайт `https://www.avito.ru/avito-care/eco-impact`
- - замокать json по запросу `web/1/charity/ecoImpact/init`:
```
{
  "result": {
    "blocks": {
      "personalImpact": {
        "data": {
          "co2": 1000000000000,
          "energy": 1000000000000,
          "materials": 1000000000000,
          "pineYears": 1000000000000,
          "water": 1000000000000
        }
      }
    },
    "isAuthorized": false
  },
  "status": "ok"
}
```
- ожидаемый результат:
- - 1000000000000 л воды
- - 1000000000000 кг СО2
- - 1000000000000 кВт.ч энергии

### Проверка на обработку предельно больших чисел
### id: ТК-7
- шаги: 
- - открыть сайт `https://www.avito.ru/avito-care/eco-impact`
- - замокать json по запросу `web/1/charity/ecoImpact/init`:
```
{
  "result": {
    "blocks": {
      "personalImpact": {
        "data": {
          "co2": 1000000000000000,
          "energy": 1000000000000000,
          "materials": 1000000000000000,
          "pineYears": 1000000000000000,
          "water": 1000000000000000
        }
      }
    },
    "isAuthorized": false
  },
  "status": "ok"
}
```
- ожидаемый результат:
- - 1000000000000000 л воды
- - 1000000000000000 кг СО2
- - 1000000000000000 кВт.ч энергии


###`Проверка на вход отрицательного числа 
### id: ТК-8
- шаги: 
- - открыть сайт `https://www.avito.ru/avito-care/eco-impact`
- - замокать json по запросу `web/1/charity/ecoImpact/init`:
```
{
  "result": {
    "blocks": {
      "personalImpact": {
        "data": {
          "co2": -1,
          "energy": -1,
          "materials": -1,
          "pineYears": -1,
          "water": -1
        }
      }
    },
    "isAuthorized": false
  },
  "status": "ok"
}
```
- ожидаемый результат:
- -1 л воды
- -1 кг СО2
- -1 кВт.ч энергии




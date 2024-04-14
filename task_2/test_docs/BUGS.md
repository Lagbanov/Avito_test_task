### id: 1
### Не отображается единица измерения в счетчике при числе 1.000.000.000.000 и более

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
- - 1 триллион м3 воды
- - 1 триллион тонн СО2
- - 1 триллон мВт.ч энергии

- фактический результат:
- - 1 воды
- - 1 СО2
- - 1 мВт.ч энергии

severity: minor
priority: low
attachment: screenshot output/TK-7-full_counter.png

### id: 2
### Накладываение текста в счетчике "Энергия" при числе 1.000.000 и более

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
- - в счетчике "энергия" текст: "1 млн мВт.ч энергии было сэкономлено"

- фактический результат:
- - в счетчике "энергия" текст: "1 млн мВт.ч" накладывается на текст: "энергии было сэкономлено"

severity: minor
priority: low
attachment: screenshot output/TK-5-energy.png
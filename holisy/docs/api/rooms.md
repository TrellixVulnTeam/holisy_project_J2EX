**URL** : `/rooms/`

**Method** : `GET`

**Auth required** : No

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
   "Rooms": [
    {
        "room_number": 1,
        "name": "Economy room",
        "beds_number": 2,
        "day_cost": 10,
        "room_class": "эконом",
        "photo": "http://127.0.0.1:8000/media/room1.jpg",
        "description": "Отель удобно расположен в Василеостровском районе Санкт-Петербурга, менее чем в 1 км от стадиона «Петровский» и в 1,4 км от Зимнего дворца и Государственного Эрмитажа. Расстояние до Исаакиевского собора и Дворцовой площади составляет около 1,5 км, а до храма Спаса на Крови — 2,2 км. Стойка регистрации отеля работает круглосуточно. Гостям предоставляется бесплатный Wi-Fi и услуга доставки еды и напитков в номер. По запросу организуется трансфер.\r\nНомера оснащены кондиционером и телевизором с плоским экраном и кабельными каналами. В числе удобств шкаф для одежды, чайник, душ и фен."
    },
    {
        "room_number": 2,
        "name": "Luxury room",
        "beds_number": 4,
        "day_cost": 20,
        "room_class": "luxury",
        "photo": "http://127.0.0.1:8000/media/room2.jpg",
        "description": "Отель удобно расположен в Василеостровском районе Санкт-Петербурга, менее чем в 1 км от стадиона «Петровский» и в 1,4 км от Зимнего дворца и Государственного Эрмитажа. Расстояние до Исаакиевского собора и Дворцовой площади составляет около 1,5 км, а до храма Спаса на Крови — 2,2 км. Стойка регистрации отеля работает круглосуточно. Гостям предоставляется бесплатный Wi-Fi и услуга доставки еды и напитков в номер. По запросу организуется трансфер.\r\nНомера оснащены кондиционером и телевизором с плоским экраном и кабельными каналами. В числе удобств шкаф для одежды, чайник, душ и фен."
    },
    {
        "room_number": 3,
        "name": "President room",
        "beds_number": 2,
        "day_cost": 100,
        "room_class": "president",
        "photo": "http://127.0.0.1:8000/media/room3.jpg",
        "description": "Отель удобно расположен в Василеостровском районе Санкт-Петербурга, менее чем в 1 км от стадиона «Петровский» и в 1,4 км от Зимнего дворца и Государственного Эрмитажа. Расстояние до Исаакиевского собора и Дворцовой площади составляет около 1,5 км, а до храма Спаса на Крови — 2,2 км. Стойка регистрации отеля работает круглосуточно. Гостям предоставляется бесплатный Wi-Fi и услуга доставки еды и напитков в номер. По запросу организуется трансфер.\r\nНомера оснащены кондиционером и телевизором с плоским экраном и кабельными каналами. В числе удобств шкаф для одежды, чайник, душ и фен."
    }
]
}
```
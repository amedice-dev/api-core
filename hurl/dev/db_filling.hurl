#######################################
# New Organisation`s Owner
#######################################

GET http://web:8000/users/
HTTP 200
[Captures]
user_count: jsonpath "$" count


POST http://web:8000/auth/register/
{
    "email": "owner_boss_{{user_count}}@test.com",
    "password": "TheBigFatBoss",
    "first_name": "John",
    "last_name": "Doe",
    "user_phone": "+7 666 666 66 66",
    "user_role": "Owners"
}
HTTP 201
[Captures]
owner_id: jsonpath "$.id"
owner_email: jsonpath "$.email"


POST http://web:8000/auth/login/
{
    "email": "owner_boss_{{user_count}}@test.com",
    "password": "TheBigFatBoss"
}
HTTP 200
[Captures]
owner_access_token: jsonpath "$.access"
owner_refresh_token: jsonpath "$.refresh"

#######################################
# 20 New Organisations
#######################################

POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Dark Side Medical",
    "org_category": "Медицинский центр",
    "org_local_phone": "+7 778 778 7788",
    "org_main_phone": "+7 333 333 3333",
    "org_directions": [
        "Терапия",
        "Хирургия"
    ]
}
HTTP 201
[Captures]
org_id_1: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Sunrise Dental Clinic",
    "org_category": "Стоматология",
    "org_local_phone": "+7 777 888 9999",
    "org_main_phone": "+7 444 555 6666",
    "org_directions": [
        "Стоматология",
        "Ортопедия"
    ]
}
HTTP 201
[Captures]
org_id_2: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Tech Diagnostics",
    "org_category": "Диагностический центр",
    "org_local_phone": "+7 555 666 7777",
    "org_main_phone": "+7 222 333 4444",
    "org_directions": [
        "Дерматология",
        "Физиотерапия"
    ]
}
HTTP 201
[Captures]
org_id_3: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Happy Kids Clinic",
    "org_category": "Детская клиника",
    "org_local_phone": "+7 999 888 7777",
    "org_main_phone": "+7 111 222 3333",
    "org_directions": [
        "Педиатрия",
        "Отоларингология"
    ]
}
HTTP 201
[Captures]
org_id_4: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Cosmetic Wellness Center",
    "org_category": "Косметологический центр",
    "org_local_phone": "+7 666 555 4444",
    "org_main_phone": "+7 999 888 7777",
    "org_directions": [
        "Косметология",
        "Гинекология"
    ]
}
HTTP 201
[Captures]
org_id_5: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "City Hospital",
    "org_category": "Больница",
    "org_local_phone": "+7 777 111 2222",
    "org_main_phone": "+7 333 555 7777",
    "org_directions": [
        "Терапия",
        "Хирургия"
    ]
}
HTTP 201
[Captures]
org_id_6: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Healthy Life Clinic",
    "org_category": "Медицинский центр",
    "org_local_phone": "+7 888 999 1111",
    "org_main_phone": "+7 111 222 3333",
    "org_directions": [
        "Неврология",
        "Эндокринология"
    ]
}
HTTP 201
[Captures]
org_id_7: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Bright Eyes Clinic",
    "org_category": "Офтальмологическая клиника",
    "org_local_phone": "+7 333 444 5555",
    "org_main_phone": "+7 666 777 8888",
    "org_directions": [
        "Офтальмология",
        "Кардиология"
    ]
}
HTTP 201
[Captures]
org_id_8: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Dental Polyclinic",
    "org_category": "Стоматологическая поликлиника",
    "org_local_phone": "+7 555 666 7777",
    "org_main_phone": "+7 888 999 1111",
    "org_directions": [
        "Стоматология",
        "Ортопедия"
    ]
}
HTTP 201
[Captures]
org_id_9: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Tech Dispensary",
    "org_category": "Диспансер",
    "org_local_phone": "+7 444 555 6666",
    "org_main_phone": "+7 111 222 3333",
    "org_directions": [
        "Неврология",
        "Эндокринология"
    ]
}
HTTP 201
[Captures]
org_id_10: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Healthy Kids Hospital",
    "org_category": "Детская больница",
    "org_local_phone": "+7 777 888 9999",
    "org_main_phone": "+7 333 444 5555",
    "org_directions": [
        "Педиатрия",
        "Отоларингология"
    ]
}
HTTP 201
[Captures]
org_id_11: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Cosmetic Bliss Center",
    "org_category": "Косметологический центр",
    "org_local_phone": "+7 666 555 4444",
    "org_main_phone": "+7 999 888 7777",
    "org_directions": [
        "Косметология",
        "Гинекология"
    ]
}
HTTP 201
[Captures]
org_id_12: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "City Maternity Hospital",
    "org_category": "Роддом",
    "org_local_phone": "+7 777 111 2222",
    "org_main_phone": "+7 333 555 7777",
    "org_directions": [
        "Педиатрия"
    ]
}
HTTP 201
[Captures]
org_id_13: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Urban Cosmetology Center",
    "org_category": "Косметологический центр",
    "org_local_phone": "+7 888 999 1111",
    "org_main_phone": "+7 111 222 3333",
    "org_directions": [
        "Косметология",
        "Дерматология"
    ]
}
HTTP 201
[Captures]
org_id_14: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Bright Eyes Clinic",
    "org_category": "Офтальмологическая клиника",
    "org_local_phone": "+7 333 444 5555",
    "org_main_phone": "+7 666 777 8888",
    "org_directions": [
        "Офтальмология",
        "Кардиология"
    ]
}
HTTP 201
[Captures]
org_id_15: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Dental Wellness Clinic",
    "org_category": "Стоматология",
    "org_local_phone": "+7 555 666 7777",
    "org_main_phone": "+7 888 999 1111",
    "org_directions": [
        "Стоматология",
        "Ортопедия"
    ]
}
HTTP 201
[Captures]
org_id_16: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Tech Diagnostics",
    "org_category": "Диагностический центр",
    "org_local_phone": "+7 444 555 6666",
    "org_main_phone": "+7 111 222 3333",
    "org_directions": [
        "Дерматология",
        "Физиотерапия"
    ]
}
HTTP 201
[Captures]
org_id_17: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Happy Kids Clinic",
    "org_category": "Детская клиника",
    "org_local_phone": "+7 999 888 7777",
    "org_main_phone": "+7 111 222 3333",
    "org_directions": [
        "Педиатрия",
        "Отоларингология"
    ]
}
HTTP 201
[Captures]
org_id_18: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Cosmetic Wellness Center",
    "org_category": "Косметологический центр",
    "org_local_phone": "+7 666 555 4444",
    "org_main_phone": "+7 999 888 7777",
    "org_directions": [
        "Косметология",
        "Гинекология"
    ]
}
HTTP 201
[Captures]
org_id_19: jsonpath "$.org_id"


POST http://web:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "City Hospital",
    "org_category": "Больница",
    "org_local_phone": "+7 777 111 2222",
    "org_main_phone": "+7 333 555 7777",
    "org_directions": [
        "Терапия",
        "Хирургия"
    ]
}
HTTP 201
[Captures]
org_id_20: jsonpath "$.org_id"

#######################################
# Superuser Auth
#######################################

POST http://web:8000/auth/login
{
    "email": "admin@test.com",
    "password": "admin_Root"
}
HTTP 200
[Captures]
admin_access_token: jsonpath "$.access"
admin_refresh_token: jsonpath "$.refresh"

#######################################
# Create Categories
#######################################

POST http://web:8000/catalog/categories
Authorization: Bearer {{admin_access_token}}
{
    "name": "Медицинские центры",
    "slug": "med_centers",
    "type": "private",
    "page_content": {
        "seo_title": "Медицинские центры",
        "seo_description": "Центры, в которых есть медицина",
        "seo_content": "HTML тыры-пыры"
    }
}
HTTP 201
[Captures]
med_centers_id: jsonpath "$.category_id"

POST http://web:8000/catalog/categories
Authorization: Bearer {{admin_access_token}}
{
    "name": "Лаборатории",
    "slug": "laboratories",
    "type": "private"
}
HTTP 201
[Captures]
laboratories_id: jsonpath "$.category_id"

POST http://web:8000/catalog/categories
Authorization: Bearer {{admin_access_token}}
{
    "name": "Стоматологические клиники",
    "slug": "dental_clinics",
    "type": "private"
}
HTTP 201
[Captures]
dental_clinics_id: jsonpath "$.category_id"

POST http://web:8000/catalog/categories
Authorization: Bearer {{admin_access_token}}
{
    "name": "Диагностические центры",
    "slug": "diagnostic_centers",
    "type": "private"
}
HTTP 201
[Captures]
diagnostic_centers_id: jsonpath "$.category_id"

POST http://web:8000/catalog/categories
Authorization: Bearer {{admin_access_token}}
{
    "name": "Офтальмологические клиники",
    "slug": "eye_clinics",
    "type": "private"
}
HTTP 201
[Captures]
eye_clinics_id: jsonpath "$.category_id"

POST http://web:8000/catalog/categories
Authorization: Bearer {{admin_access_token}}
{
    "name": "Детские клиники",
    "slug": "kids_clinics",
    "type": "private"
}
HTTP 201
[Captures]
kids_clinics_id: jsonpath "$.category_id"

POST http://web:8000/catalog/categories
Authorization: Bearer {{admin_access_token}}
{
    "name": "Косметологические центры",
    "slug": "cosmetology_centers",
    "type": "private"
}
HTTP 201
[Captures]
cosmetology_centers_id: jsonpath "$.category_id"

POST http://web:8000/catalog/categories
Authorization: Bearer {{admin_access_token}}
{
    "name": "Госпитали",
    "slug": "gos_hospitals",
    "type": "public"
}
HTTP 201
[Captures]
gos_hospitals_id: jsonpath "$.category_id"

POST http://web:8000/catalog/categories
Authorization: Bearer {{admin_access_token}}
{
    "name": "Амбулатории",
    "slug": "gos_ambulatories",
    "type": "public"
}
HTTP 201
[Captures]
gos_ambulatories_id: jsonpath "$.category_id"

POST http://web:8000/catalog/categories
Authorization: Bearer {{admin_access_token}}
{
    "name": "Детские госпитали",
    "slug": "gos_kids_hospitals",
    "type": "public"
}
HTTP 201
[Captures]
gos_kids_hospitals_id: jsonpath "$.category_id"

POST http://web:8000/catalog/categories
Authorization: Bearer {{admin_access_token}}
{
    "name": "Госполиклиники",
    "slug": "gos_polyclinics",
    "type": "public"
}
HTTP 201
[Captures]
gos_polyclinics_id: jsonpath "$.category_id"

POST http://web:8000/catalog/categories
Authorization: Bearer {{admin_access_token}}
{
    "name": "Государственные стоматологические поликлиники",
    "slug": "gos_dental_polyclinics",
    "type": "public"
}
HTTP 201
[Captures]
gos_dental_polyclinics_id: jsonpath "$.category_id"

POST http://web:8000/catalog/categories
Authorization: Bearer {{admin_access_token}}
{
    "name": "Государственные роддомы",
    "slug": "gos_maternity_hospitals",
    "type": "public"
}
HTTP 201
[Captures]
gos_maternity_hospitals_id: jsonpath "$.category_id"

POST http://web:8000/catalog/categories
Authorization: Bearer {{admin_access_token}}
{
    "name": "Диспансеры",
    "slug": "gos_dispensaries",
    "type": "public"
}
HTTP 201
[Captures]
gos_dispensaries_id: jsonpath "$.category_id"

#######################################
# Create Directions
#######################################

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Урология",
    "slug": "urology"
}
HTTP 201
[Captures]
urology_id: jsonpath "$.direction_id"

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Терапия",
    "slug": "therapy"
}
HTTP 201
[Captures]
therapy_id: jsonpath "$.direction_id"

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Стоматология",
    "slug": "dentistry"
}
HTTP 201
[Captures]
dentistry_id: jsonpath "$.direction_id"

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Дерматология",
    "slug": "dermatology"
}
HTTP 201
[Captures]
dermatology_id: jsonpath "$.direction_id"

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Неврология",
    "slug": "neurology"
}
HTTP 201
[Captures]
neurology_id: jsonpath "$.direction_id"

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Косметология",
    "slug": "cosmetology"
}
HTTP 201
[Captures]
cosmetology_id: jsonpath "$.direction_id"

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Венерология",
    "slug": "venereology"
}
HTTP 201
[Captures]
venereology_id: jsonpath "$.direction_id"

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Ортопедия",
    "slug": "orthopedics"
}
HTTP 201
[Captures]
orthopedics_id: jsonpath "$.direction_id"

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Физиотерапия",
    "slug": "physiotherapy"
}
HTTP 201
[Captures]
physiotherapy_id: jsonpath "$.direction_id"

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Хирургия",
    "slug": "surgery"
}
HTTP 201
[Captures]
surgery_id: jsonpath "$.direction_id"

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Эндокринология",
    "slug": "endocrinology"
}
HTTP 201
[Captures]
endocrinology_id: jsonpath "$.direction_id"

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Онкология",
    "slug": "oncology"
}
HTTP 201
[Captures]
oncology_id: jsonpath "$.direction_id"

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Педиатрия",
    "slug": "pediatrics"
}
HTTP 201
[Captures]
pediatrics_id: jsonpath "$.direction_id"

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Кардиология",
    "slug": "cardiology"
}
HTTP 201
[Captures]
cardiology_id: jsonpath "$.direction_id"

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Отоларингология",
    "slug": "oto_rhino_laryngology"
}
HTTP 201
[Captures]
oto_rhino_laryngology_id: jsonpath "$.direction_id"

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Психиатрия",
    "slug": "psychiatry"
}
HTTP 201
[Captures]
psychiatry_id: jsonpath "$.direction_id"

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Офтальмология",
    "slug": "ophthalmology"
}
HTTP 201
[Captures]
ophthalmology_id: jsonpath "$.direction_id"

POST http://web:8000/catalog/directions
Authorization: Bearer {{admin_access_token}}
{
    "name": "Гинекология",
    "slug": "gynecology"
}
HTTP 201
[Captures]
gynecology_id: jsonpath "$.direction_id"

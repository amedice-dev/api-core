#######################################
# First User Registration
#######################################

GET http://localhost:8000/auth/users/
HTTP 200
[Captures]
user_count: jsonpath "$" count



POST http://localhost:8000/auth/user/register/
{
    "user": {
        "email": "user{{user_count}}@metacortex.com",
        "first_name": "Thomas",
        "last_name": "Anderson",
        "password": "WhatistheMatrix?"
    }
}
HTTP 201
[Captures]
first_user_id: jsonpath "$.user.id"
first_user_email: jsonpath "$.user.email"
first_user_name: jsonpath "$.user.first_name"



GET http://localhost:8000/auth/users/
HTTP 200
[Asserts]
#jsonpath "$" count == {{user_count}}
jsonpath "$[0].id" == {{first_user_id}}


#######################################
# First User Login
#######################################

POST http://localhost:8000/auth/user/login/
{
    "user": {
        "email": "{{first_user_email}}",
        "password": "WhatistheMatrix?"
    }
}
HTTP 200
[Captures]
first_user_token: jsonpath "$.user.token"


#######################################
# First User Get and Update profile
#######################################

GET http://localhost:8000/auth/user/
Authorization: Bearer {{first_user_token}}
HTTP 200
[Asserts]
jsonpath "$.user.email" == {{first_user_email}}
jsonpath "$.user.id" == {{first_user_id}}



PUT http://localhost:8000/auth/user/
Authorization: Bearer {{first_user_token}}
{
    "user": {
        "email": "the_one{{user_count}}@zion.com",
        "first_name": "Neo",
        "last_name": "The One",
        "password": "Thereisnospoon!"
    }
}
HTTP 200
[Asserts]
jsonpath "$.user.email" == "the_one{{user_count}}@zion.com"
jsonpath "$.user.first_name" == "Neo"


#######################################
# Create New Medical Center
#######################################

GET http://localhost:8000/core_api/med_centers/
Authorization: Bearer {{first_user_token}}
HTTP 200
[Captures]
med_centers_count: jsonpath "$" count



POST http://localhost:8000/core_api/med_centers/
Authorization: Bearer {{first_user_token}}
{
    "title": "Medical Center {{med_centers_count}}",
    "type": "Клиника",
    "description": "Описание медицинского центра {{med_centers_count}}",
    "services": ["Хирургия", "Неврология", "УЗИ"],
    "doctors_speciality": ["Хирург", "Невролог"],
    "address": "ул. Ленина, 1a",
    "email": "med_center_{{med_centers_count}}@test.com",
    "phone_number": "+7 (999) 999-99-99"
}
HTTP 201
[Captures]
med_center_1_id: jsonpath "$.id"



GET http://localhost:8000/core_api/med_centers/{{med_center_1_id}}/
Authorization: Bearer {{first_user_token}}
HTTP 200
[Asserts]
jsonpath "$.title" == "Medical Center {{med_centers_count}}"
jsonpath "$.type" == "Клиника"
jsonpath "$.description" == "Описание медицинского центра {{med_centers_count}}"
jsonpath "$.services[0]" == "Хирургия"
jsonpath "$.services[1]" == "Неврология"
jsonpath "$.services[2]" == "УЗИ"
jsonpath "$.doctors_speciality[0]" == "Хирург"
jsonpath "$.doctors_speciality[1]" == "Невролог"
jsonpath "$.address" == "ул. Ленина, 1a"
jsonpath "$.email" == "med_center_{{med_centers_count}}@test.com"
jsonpath "$.phone_number" == "+7 (999) 999-99-99"
jsonpath "$.doctors" count == 0


#######################################
# Create New Doctor
#######################################

GET http://localhost:8000/core_api/doctors/
Authorization: Bearer {{first_user_token}}
HTTP 200
[Captures]
doctors_count: jsonpath "$" count



POST http://localhost:8000/core_api/doctors/
Authorization: Bearer {{first_user_token}}
{
    "first_name": "Doctor-{{doctors_count}}",
    "last_name": "Иванов",
    "speciality": ["Хирург"],
    "email": "surgery_top@example.com",
    "phone_number": "+7 (999) 777-77-77"
}
HTTP 201
[Captures]
surgery_id: jsonpath "$.id"



GET http://localhost:8000/core_api/doctors/{{surgery_id}}/
Authorization: Bearer {{first_user_token}}
HTTP 200
[Asserts]
jsonpath "$.first_name" == "Doctor-{{doctors_count}}"
jsonpath "$.last_name" == "Иванов"
jsonpath "$.speciality[0]" == "Хирург"
jsonpath "$.email" == "surgery_top@example.com"
jsonpath "$.phone_number" == "+7 (999) 777-77-77"


#######################################
# Add Doctor to Medical Center
#######################################

PATCH http://localhost:8000/core_api/med_centers/{{med_center_1_id}}/
Authorization: Bearer {{first_user_token}}
{
    "doctors": ["{{surgery_id}}"]
}
HTTP 200



GET http://localhost:8000/core_api/med_centers/{{med_center_1_id}}/
Authorization: Bearer {{first_user_token}}
HTTP 200
[Asserts]
jsonpath "$.doctors" count == 1
jsonpath "$.doctors[0]" == {{surgery_id}}

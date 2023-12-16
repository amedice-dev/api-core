#######################################
# New Organisation`s Owner
#######################################

GET http://web:8000/users
HTTP 200
[Captures]
user_count: jsonpath "$" count


POST http://web:8000/auth/register
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


POST http://web:8000/auth/login
{
    "email": "owner_boss_{{user_count}}@test.com",
    "password": "TheBigFatBoss"
}
HTTP 200
[Captures]
owner_access_token: jsonpath "$.access"
owner_refresh_token: jsonpath "$.refresh"

#######################################
# Get Categories
#######################################

GET http://web:8000/categories_tree
HTTP 200
[Captures]
med_center_id: jsonpath "$[0].category_id"
laboratory_id: jsonpath "$[1].category_id"
dental_clinic_id: jsonpath "$[2].category_id"
diagnostic_center_id: jsonpath "$[3].category_id"
eye_clinic_id: jsonpath "$[4].category_id"
kids_clinic_id: jsonpath "$[5].category_id"
cosmetology_center_id: jsonpath "$[6].category_id"
gos_hospital_id: jsonpath "$[7].category_id"
gos_ambulatory_id: jsonpath "$[8].category_id"
gos_kids_hospital_id: jsonpath "$[9].category_id"
gos_polyclinic_id: jsonpath "$[10].category_id"
gos_dental_clinic_id: jsonpath "$[11].category_id"
gos_maternity_hospital_id: jsonpath "$[12].category_id"
gos_dispensary_id: jsonpath "$[13].category_id"
[Asserts]
jsonpath "$" count == 14
jsonpath "$[0].slug" == "med_center"
jsonpath "$[1].slug" == "laboratory"
jsonpath "$[2].slug" == "dental_clinic"
jsonpath "$[3].slug" == "diagnostic_center"
jsonpath "$[4].slug" == "eye_clinic"
jsonpath "$[5].slug" == "kids_clinic"
jsonpath "$[6].slug" == "cosmetology_center"
jsonpath "$[7].slug" == "gos_hospital"
jsonpath "$[8].slug" == "gos_ambulatory"
jsonpath "$[9].slug" == "gos_kids_hospital"
jsonpath "$[10].slug" == "gos_polyclinic"
jsonpath "$[11].slug" == "gos_dental_polyclinic"
jsonpath "$[12].slug" == "gos_maternity_hospital"
jsonpath "$[13].slug" == "gos_dispensary"

#######################################
# Get Directions
#######################################

GET http://web:8000/directions
HTTP 200
[Captures]
urology_id: jsonpath "$[0].direction_id"
therapy_id: jsonpath "$[1].direction_id"
dentistry_id: jsonpath "$[2].direction_id"
dermatology_id: jsonpath "$[3].direction_id"
neurology_id: jsonpath "$[4].direction_id"
cosmetology_id: jsonpath "$[5].direction_id"
venereology_id: jsonpath "$[6].direction_id"
orthopedics_id: jsonpath "$[7].direction_id"
physiotherapy_id: jsonpath "$[8].direction_id"
surgery_id: jsonpath "$[9].direction_id"
endocrinology_id: jsonpath "$[10].direction_id"
oncology_id: jsonpath "$[11].direction_id"
pediatrics_id: jsonpath "$[12].direction_id"
cardiology_id: jsonpath "$[13].direction_id"
oto_rhino_laryngology_id: jsonpath "$[14].direction_id"
psychiatry_id: jsonpath "$[15].direction_id"
ophthalmology_id: jsonpath "$[16].direction_id"
gynecology_id: jsonpath "$[17].direction_id"
[Asserts]
jsonpath "$" count == 18
jsonpath "$[0].slug" == "urology"
jsonpath "$[1].slug" == "therapy"
jsonpath "$[2].slug" == "dentistry"
jsonpath "$[3].slug" == "dermatology"
jsonpath "$[4].slug" == "neurology"
jsonpath "$[5].slug" == "cosmetology"
jsonpath "$[6].slug" == "venereology"
jsonpath "$[7].slug" == "orthopedics"
jsonpath "$[8].slug" == "physiotherapy"
jsonpath "$[9].slug" == "surgery"
jsonpath "$[10].slug" == "endocrinology"
jsonpath "$[11].slug" == "oncology"
jsonpath "$[12].slug" == "pediatrics"
jsonpath "$[13].slug" == "cardiology"
jsonpath "$[14].slug" == "oto_rhino_laryngology"
jsonpath "$[15].slug" == "psychiatry"
jsonpath "$[16].slug" == "ophthalmology"
jsonpath "$[17].slug" == "gynecology"

#######################################
# 20 New Organisations
#######################################

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Dark Side Medical",
    "org_category": {{med_center_id}},
    "org_local_phone": "+7 778 778 7788",
    "org_directions": [
        {{therapy_id}},
        {{surgery_id}}
    ]
}
HTTP 201
[Captures]
org_id_1: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Sunrise Dental Clinic",
    "org_category": {{dental_clinic_id}},
    "org_local_phone": "+7 777 888 9999",
    "org_directions": [
        {{dentistry_id}},
        {{orthopedics_id}}
    ]
}
HTTP 201
[Captures]
org_id_2: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Tech Diagnostics",
    "org_category": {{diagnostic_center_id}},
    "org_local_phone": "+7 555 666 7777",
    "org_directions": [
        {{dermatology_id}},
        {{physiotherapy_id}}
    ]
}
HTTP 201
[Captures]
org_id_3: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Happy Kids Clinic",
    "org_category": {{kids_clinic_id}},
    "org_local_phone": "+7 999 888 7777",
    "org_directions": [
        {{pediatrics_id}},
        {{oto_rhino_laryngology_id}}
    ]
}
HTTP 201
[Captures]
org_id_4: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Cosmetic Wellness Center",
    "org_category": {{cosmetology_center_id}},
    "org_local_phone": "+7 666 555 4444",
    "org_directions": [
        {{cosmetology_id}},
        {{gynecology_id}}
    ]
}
HTTP 201
[Captures]
org_id_5: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "City Hospital",
    "org_category": {{gos_hospital_id}},
    "org_local_phone": "+7 777 111 2222",
    "org_directions": [
        {{therapy_id}},
        {{surgery_id}}
    ]
}
HTTP 201
[Captures]
org_id_6: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Healthy Life Clinic",
    "org_category": {{med_center_id}},
    "org_local_phone": "+7 888 999 1111",
    "org_directions": [
        {{neurology_id}},
        {{endocrinology_id}}
    ]
}
HTTP 201
[Captures]
org_id_7: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Bright Eyes Clinic",
    "org_category": {{eye_clinic_id}},
    "org_local_phone": "+7 333 444 5555",
    "org_directions": [
        {{ophthalmology_id}},
        {{cardiology_id}}
    ]
}
HTTP 201
[Captures]
org_id_8: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Dental Polyclinic",
    "org_category": {{dental_clinic_id}},
    "org_local_phone": "+7 555 666 7777",
    "org_directions": [
        {{dentistry_id}},
        {{orthopedics_id}}
    ]
}
HTTP 201
[Captures]
org_id_9: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Tech Dispensary",
    "org_category": {{gos_dispensary_id}},
    "org_local_phone": "+7 444 555 6666",
    "org_directions": [
        {{neurology_id}},
        {{endocrinology_id}}
    ]
}
HTTP 201
[Captures]
org_id_10: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Healthy Kids Hospital",
    "org_category": {{gos_kids_hospital_id}},
    "org_local_phone": "+7 777 888 9999",
    "org_directions": [
        {{pediatrics_id}},
        {{oto_rhino_laryngology_id}}
    ]
}
HTTP 201
[Captures]
org_id_11: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Cosmetic Bliss Center",
    "org_category": {{cosmetology_center_id}},
    "org_local_phone": "+7 666 555 4444",
    "org_directions": [
        {{cosmetology_id}},
        {{gynecology_id}}
    ]
}
HTTP 201
[Captures]
org_id_12: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "City Maternity Hospital",
    "org_category": {{gos_maternity_hospital_id}},
    "org_local_phone": "+7 777 111 2222",
    "org_directions": [
        {{pediatrics_id}}
    ]
}
HTTP 201
[Captures]
org_id_13: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Urban Cosmetology Center",
    "org_category": {{cosmetology_center_id}},
    "org_local_phone": "+7 888 999 1111",
    "org_directions": [
        {{cosmetology_id}},
        {{dermatology_id}}
    ]
}
HTTP 201
[Captures]
org_id_14: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Bright Eyes Clinic",
    "org_category": {{eye_clinic_id}},
    "org_local_phone": "+7 333 444 5555",
    "org_directions": [
        {{ophthalmology_id}},
        {{cardiology_id}}
    ]
}
HTTP 201
[Captures]
org_id_15: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Dental Wellness Clinic",
    "org_category": {{dental_clinic_id}},
    "org_local_phone": "+7 555 666 7777",
    "org_directions": [
        {{dentistry_id}},
        {{orthopedics_id}}
    ]
}
HTTP 201
[Captures]
org_id_16: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Tech Diagnostics",
    "org_category": {{diagnostic_center_id}},
    "org_local_phone": "+7 444 555 6666",
    "org_directions": [
        {{dermatology_id}},
        {{physiotherapy_id}}
    ]
}
HTTP 201
[Captures]
org_id_17: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Happy Kids Clinic",
    "org_category": {{kids_clinic_id}},
    "org_local_phone": "+7 999 888 7777",
    "org_directions": [
        {{pediatrics_id}},
        {{oto_rhino_laryngology_id}}
    ]
}
HTTP 201
[Captures]
org_id_18: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Cosmetic Wellness Center",
    "org_category": {{cosmetology_center_id}},
    "org_local_phone": "+7 666 555 4444",
    "org_directions": [
        {{cosmetology_id}},
        {{gynecology_id}}
    ]
}
HTTP 201
[Captures]
org_id_19: jsonpath "$.org_id"

POST http://web:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "City Hospital",
    "org_category": {{gos_hospital_id}},
    "org_local_phone": "+7 777 111 2222",
    "org_directions": [
        {{therapy_id}},
        {{surgery_id}}
    ]
}
HTTP 201
[Captures]
org_id_20: jsonpath "$.org_id"


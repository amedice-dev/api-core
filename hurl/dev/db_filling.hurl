#######################################
# New Organisation`s Owner
#######################################

POST http://web:8000/api/auth/register
{
    "email": "owner@test.com",
    "password": "big_boss",
    "first_name": "John",
    "last_name": "Doe",
    "user_phone": "+7 666 666 66 66",
    "user_role": "Owners"
}
HTTP 201
[Captures]
owner_id: jsonpath "$.id"
owner_email: jsonpath "$.email"


POST http://web:8000/api/auth/login
{
    "email": "owner@test.com",
    "password": "big_boss"
}
HTTP 200
[Captures]
owner_access_token: jsonpath "$.access"
owner_refresh_token: jsonpath "$.refresh"

#######################################
# Get Categories
#######################################

GET http://web:8000/api/catalog/categories_tree
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
jsonpath "$[0].slug" == "med_centers"
jsonpath "$[1].slug" == "laboratories"
jsonpath "$[2].slug" == "dental_clinics"
jsonpath "$[3].slug" == "diagnostic_centers"
jsonpath "$[4].slug" == "eye_clinics"
jsonpath "$[5].slug" == "kids_clinics"
jsonpath "$[6].slug" == "cosmetology_centers"
jsonpath "$[7].slug" == "gos_hospitals"
jsonpath "$[8].slug" == "gos_ambulatories"
jsonpath "$[9].slug" == "gos_kids_hospitals"
jsonpath "$[10].slug" == "gos_polyclinics"
jsonpath "$[11].slug" == "gos_dental_polyclinics"
jsonpath "$[12].slug" == "gos_maternity_hospitals"
jsonpath "$[13].slug" == "gos_dispensaries"

#######################################
# Get Directions
#######################################

GET http://web:8000/api/catalog/directions
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
# 40 New Organisations
#######################################

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
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

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Healing Hands Medical Center",
    "org_category": {{med_center_id}},
    "org_local_phone": "+7 111 222 4444",
    "org_directions": [
        {{cosmetology_id}},
        {{gynecology_id}}
    ]
}
HTTP 201
[Captures]
org_id_21: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Tech Care Laboratory",
    "org_category": {{laboratory_id}},
    "org_local_phone": "+7 555 666 8888",
    "org_directions": [
        {{orthopedics_id}},
        {{physiotherapy_id}}
    ]
}
HTTP 201
[Captures]
org_id_22: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Sunset Diagnostic Center",
    "org_category": {{diagnostic_center_id}},
    "org_local_phone": "+7 777 888 1111",
    "org_directions": [
        {{dermatology_id}},
        {{surgery_id}}
    ]
}
HTTP 201
[Captures]
org_id_23: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Happy Kids Pediatrics",
    "org_category": {{kids_clinic_id}},
    "org_local_phone": "+7 999 888 2222",
    "org_directions": [
        {{pediatrics_id}},
        {{oto_rhino_laryngology_id}}
    ]
}
HTTP 201
[Captures]
org_id_24: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Tech Wellness Center",
    "org_category": {{gos_hospital_id}},
    "org_local_phone": "+7 123 456 7890",
    "org_directions": [
        {{neurology_id}},
        {{psychiatry_id}}
    ]
}
HTTP 201
[Captures]
org_id_25: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Eternal Beauty Cosmetology",
    "org_category": {{cosmetology_center_id}},
    "org_local_phone": "+7 111 222 3333",
    "org_directions": [
        {{dermatology_id}},
        {{cosmetology_id}}
    ]
}
HTTP 201
[Captures]
org_id_26: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "City General Hospital",
    "org_category": {{gos_ambulatory_id}},
    "org_local_phone": "+7 333 444 5555",
    "org_directions": [
        {{surgery_id}},
        {{orthopedics_id}}
    ]
}
HTTP 201
[Captures]
org_id_27: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Little Stars Kids Hospital",
    "org_category": {{gos_kids_hospital_id}},
    "org_local_phone": "+7 666 777 8888",
    "org_directions": [
        {{pediatrics_id}},
        {{cardiology_id}}
    ]
}
HTTP 201
[Captures]
org_id_28: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Green Meadows Polyclinic",
    "org_category": {{gos_polyclinic_id}},
    "org_local_phone": "+7 999 888 7777",
    "org_directions": [
        {{therapy_id}},
        {{oto_rhino_laryngology_id}}
    ]
}
HTTP 201
[Captures]
org_id_29: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Smile Dental Polyclinic",
    "org_category": {{gos_dental_clinic_id}},
    "org_local_phone": "+7 111 222 3333",
    "org_directions": [
        {{dentistry_id}},
        {{orthopedics_id}}
    ]
}
HTTP 201
[Captures]
org_id_30: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Joyful Maternity Hospital",
    "org_category": {{gos_maternity_hospital_id}},
    "org_local_phone": "+7 555 666 7777",
    "org_directions": [
        {{gynecology_id}}
    ]
}
HTTP 201
[Captures]
org_id_31: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Sunrise Dispensary",
    "org_category": {{gos_dispensary_id}},
    "org_local_phone": "+7 777 888 9999",
    "org_directions": [
        {{therapy_id}},
        {{psychiatry_id}}
    ]
}
HTTP 201
[Captures]
org_id_32: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Healthy Life Wellness",
    "org_category": {{med_center_id}},
    "org_local_phone": "+7 333 444 5555",
    "org_directions": [
        {{cardiology_id}},
        {{physiotherapy_id}}
    ]
}
HTTP 201
[Captures]
org_id_33: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Tech Lab Innovations",
    "org_category": {{laboratory_id}},
    "org_local_phone": "+7 888 999 0000",
    "org_directions": [
        {{dermatology_id}},
        {{oncology_id}}
    ]
}
HTTP 201
[Captures]
org_id_34: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Sunset Kids Clinic",
    "org_category": {{kids_clinic_id}},
    "org_local_phone": "+7 111 222 3333",
    "org_directions": [
        {{pediatrics_id}},
        {{oto_rhino_laryngology_id}}
    ]
}
HTTP 201
[Captures]
org_id_35: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Eternal Youth Cosmetology",
    "org_category": {{cosmetology_center_id}},
    "org_local_phone": "+7 555 666 7777",
    "org_directions": [
        {{dermatology_id}},
        {{cosmetology_id}}
    ]
}
HTTP 201
[Captures]
org_id_36: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "City Hospital",
    "org_category": {{gos_hospital_id}},
    "org_local_phone": "+7 999 888 9999",
    "org_directions": [
        {{surgery_id}},
        {{orthopedics_id}}
    ]
}
HTTP 201
[Captures]
org_id_37: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Little Angels Kids Hospital",
    "org_category": {{gos_kids_hospital_id}},
    "org_local_phone": "+7 111 222 4444",
    "org_directions": [
        {{pediatrics_id}},
        {{cardiology_id}}
    ]
}
HTTP 201
[Captures]
org_id_38: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Green Valley Polyclinic",
    "org_category": {{gos_polyclinic_id}},
    "org_local_phone": "+7 333 444 5555",
    "org_directions": [
        {{therapy_id}},
        {{oto_rhino_laryngology_id}}
    ]
}
HTTP 201
[Captures]
org_id_39: jsonpath "$.org_id"

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Dental Bliss Polyclinic",
    "org_category": {{gos_dental_clinic_id}},
    "org_local_phone": "+7 777 888 0000",
    "org_directions": [
        {{dentistry_id}},
        {{orthopedics_id}}
    ]
}
HTTP 201
[Captures]
org_id_40: jsonpath "$.org_id"


#######################################
# Make Organisations "is_active"
#######################################

PATCH http://web:8000/api/organisations/1
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/2
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/3
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/4
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/5
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/6
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/7
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/8
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/9
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/10
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/11
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/12
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/13
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/14
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/15
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/16
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/17
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/18
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/19
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/20
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/21
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/22
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/23
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/24
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/25
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/26
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/27
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/28
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/29
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/30
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/31
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/32
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/33
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/34
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/35
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/36
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/37
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/38
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/39
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

PATCH http://web:8000/api/organisations/40
Authorization: Bearer {{owner_access_token}}
{
    "is_active": true
}
HTTP 200
[Asserts]
jsonpath "$.is_active" == true

#######################################
# Request Organisations with filters
#######################################

GET http://web:8000/api/organisations?page=1&page_size=1&org_category=med_centers
HTTP 200
[Asserts]
jsonpath "$.count" == 4
jsonpath "$.next" != null
jsonpath "$.previous" == null
jsonpath "$.results" count == 1

GET http://web:8000/api/organisations?page=2&page_size=1&org_category=med_centers
HTTP 200
[Asserts]
jsonpath "$.count" == 4
jsonpath "$.next" == "http://web:8000/api/organisations?org_category=med_centers&page=3&page_size=1"
jsonpath "$.previous" != null
jsonpath "$.results" count == 1

GET http://web:8000/api/organisations?page=1&page_size=10
HTTP 200
[Asserts]
jsonpath "$.count" == 40
jsonpath "$.next" != null
jsonpath "$.previous" == null
jsonpath "$.results" count == 10

GET http://web:8000/api/organisations?page=1&page_size=10&org_category=cosmetology_centers
HTTP 200
[Asserts]
jsonpath "$.count" == 6
jsonpath "$.next" == null
jsonpath "$.previous" == null
jsonpath "$.results" count == 6

GET http://web:8000/api/organisations?page=1&page_size=10&org_direction=gynecology&org_category=cosmetology_centers
HTTP 200
[Asserts]
jsonpath "$.count" == 3
jsonpath "$.next" == null
jsonpath "$.previous" == null
jsonpath "$.results" count == 3

#######################################
# Description len test
#######################################

PATCH http://web:8000/api/organisations/1
Authorization: Bearer {{owner_access_token}}
{
    "org_text_info": "Медицинский центр 'Dark Side Medical' предоставляет высококачественные медицинские услуги, объединяя опыт врачей с современными технологиями. Наша миссия - забота о вашем здоровье. Врачи с различными специализациями обеспечивают комплексное лечение, а дружелюбная атмосфера создает комфортное окружение для пациентов."
}
HTTP 200

#######################################
# New Full Organisation
#######################################

POST http://web:8000/api/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Медицинский центр МедТести XXI",
    "org_local_phone": "+998781482288",
    "org_category": 1,
    "org_directions": [1, 2, 10, 14, 18]
}
HTTP 201

POST http://web:8000/api/socials
Authorization: Bearer {{owner_access_token}}
{
    "whatsapp": "+998781482288",
    "viber": null,
    "telegram": "@telegram",
    "instagram": null,
    "facebook": null,
    "vkontakte": "moonservice_spb",
    "odnoklassniki": null,
    "imo": null,
    "youtube": null
}
HTTP 201
[Captures]
org_socials_id: jsonpath "$.id"

PATCH http://web:8000/api/organisations/41
Authorization: Bearer {{owner_access_token}}
{
    "org_main_phone": null,
    "org_url": null,
    "org_local_address": "ул. Рашидова , 94д",
    "org_local_landmark": "Юнусабадский р-н, напротив Шавермы",
    "org_location": null,
    "org_legal_name": "ООО 'МедТести XXI'",
    "org_site_link": "http://www.test-med-xxi.com",
    "org_photos": null,
    "org_text_info": "Медицинский центр 'МедТести XXI' - это современное заведение, где опытные врачи и передовые технологии объединяются для предоставления высококачественных медицинских услуг. Наша миссия заключается в обеспечении комплексного подхода к здоровью каждого пациента. У нас работают специалисты различных областей медицины, готовые предложить индивидуальное лечение, а дружелюбная атмосфера центра создает комфортное окружение для всех посетителей.",
    "is_active": true,
    "doctors_list": null,
    "org_socials": {{org_socials_id}},
    "org_working_hours": {
        "monday": {
            "open": "09:00",
            "close": "18:00"
        },
        "tuesday": {
            "open": "09:00",
            "close": "18:00"
        },
        "wednesday": {
            "open": "09:00",
            "close": "18:00"
        },
        "thursday": {
            "open": "09:00",
            "close": "18:00"
        },
        "friday": {
            "open": "09:00",
            "close": "18:00"
        },
        "saturday": {
            "open": "10:00",
            "close": "16:00"
        },
        "sunday": {
            "open": "10:00",
            "close": "16:00"
        }
    }
}
HTTP 200
#######################################
# Owner Login
#######################################

GET http://localhost:8000/users
HTTP 200
[Captures]
owner_id: jsonpath "$.[0].id"
admin_id: jsonpath "$.[1].id"
visitor_id: jsonpath "$.[2].id"


POST http://localhost:8000/auth/login
{
    "email": "owner0@test.com",
    "password": "FooFooFoo123"
}
HTTP 200
[Captures]
owner_access_token: jsonpath "$.access"
owner_refresh_token: jsonpath "$.refresh"

#######################################
# Get Categories
#######################################

GET http://localhost:8000/categories_tree
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

GET http://localhost:8000/directions
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
# Create an Organisation
#######################################

POST http://localhost:8000/organisations
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Gold Med",
    "org_category": {{med_center_id}},
    "org_local_phone": "+7 123 123 1212",
    "org_directions": [
        {{urology_id}}
    ]
}
HTTP 201
[Captures]
org_id: jsonpath "$.org_id"
org_name: jsonpath "$.org_name"
org_local_phone: jsonpath "$.org_local_phone"


GET http://localhost:8000/organisations
HTTP 200
[Asserts]
jsonpath "$" count == 1
jsonpath "$[0].org_id" == {{org_id}}


GET http://localhost:8000/organisations/{{org_id}}
HTTP 200
[Asserts]
jsonpath "$.org_id" == {{org_id}}
jsonpath "$.org_name" == {{org_name}}
jsonpath "$.org_category" == {{med_center_id}}
jsonpath "$.org_local_phone" == {{org_local_phone}}
jsonpath "$.org_directions[0]" == {{urology_id}}
jsonpath "$.org_owner" == {{owner_id}}

#######################################
# Update an Organisation and add an Admin
#######################################

PATCH http://localhost:8000/organisations/{{org_id}}
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Silver Med",
    "org_directions": [
        {{urology_id}},
        {{therapy_id}}
    ],
    "org_admins": [
        {{admin_id}}
    ]
}
HTTP 200
[Captures]
new_org_name: jsonpath "$.org_name"
new_org_directions: jsonpath "$.org_directions"


PATCH http://localhost:8000/users/{{admin_id}}
{
    "organisations_list": [
       {{org_id}}
    ]
}
HTTP 200


GET http://localhost:8000/organisations/{{org_id}}
HTTP 200
[Asserts]
jsonpath "$.org_id" == {{org_id}}
jsonpath "$.org_name" == {{new_org_name}}
jsonpath "$.org_directions" == {{new_org_directions}}
jsonpath "$.org_admins[0]" == {{admin_id}}


GET http://localhost:8000/users/{{owner_id}}
HTTP 200
[Asserts]
jsonpath "$.organisations_list[0]" == {{org_id}}


GET http://localhost:8000/users/{{admin_id}}
HTTP 200
[Asserts]
jsonpath "$.organisations_list[0]" == {{org_id}}


#######################################
# Delete an Organisation
#######################################

DELETE http://localhost:8000/organisations/{{org_id}}
Authorization: Bearer {{owner_access_token}}
HTTP 204

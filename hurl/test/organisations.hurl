#######################################
# Owner Login
#######################################

GET http://localhost:8000/users/
HTTP 200
[Captures]
owner_id: jsonpath "$.[0].id"
admin_id: jsonpath "$.[1].id"
visitor_id: jsonpath "$.[2].id"


POST http://localhost:8000/auth/login/
{
    "email": "owner0@test.com",
    "password": "FooFooFoo123"
}
HTTP 200
[Captures]
owner_access_token: jsonpath "$.access"
owner_refresh_token: jsonpath "$.refresh"

#######################################
# Create an Organisation
#######################################

POST http://localhost:8000/organisations/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Gold Med",
    "org_category": "Медицинский центр",
    "org_local_phone": "+7 123 123 1212",
    "org_main_phone": "+7 123 123 4040",
    "org_directions": [
        "Урология"
    ]
}
HTTP 201
[Captures]
org_id: jsonpath "$.org_id"
org_name: jsonpath "$.org_name"
org_category: jsonpath "$.org_category"
org_local_phone: jsonpath "$.org_local_phone"
org_main_phone: jsonpath "$.org_main_phone"
org_directions: jsonpath "$.org_directions"


GET http://localhost:8000/organisations/
HTTP 200
[Asserts]
jsonpath "$" count == 1
jsonpath "$[0].org_id" == {{org_id}}


GET http://localhost:8000/organisations/{{org_id}}/
HTTP 200
[Asserts]
jsonpath "$.org_id" == {{org_id}}
jsonpath "$.org_name" == {{org_name}}
jsonpath "$.org_category" == {{org_category}}
jsonpath "$.org_local_phone" == {{org_local_phone}}
jsonpath "$.org_main_phone" == {{org_main_phone}}
jsonpath "$.org_directions" == {{org_directions}}
jsonpath "$.org_owner" == {{owner_id}}

#######################################
# Update an Organisation and add an Admin
#######################################

PATCH http://localhost:8000/organisations/{{org_id}}/
Authorization: Bearer {{owner_access_token}}
{
    "org_name": "Silver Med",
    "org_directions": [
        "Урология",
        "Терапия"
    ],
    "org_admins": [
        {{admin_id}}
    ]
}
HTTP 200
[Captures]
new_org_name: jsonpath "$.org_name"
new_org_directions: jsonpath "$.org_directions"


PATCH http://localhost:8000/users/{{admin_id}}/
{
    "organisations_list": [
       {{org_id}}
    ]
}
HTTP 200


GET http://localhost:8000/organisations/{{org_id}}/
HTTP 200
[Asserts]
jsonpath "$.org_id" == {{org_id}}
jsonpath "$.org_name" == {{new_org_name}}
jsonpath "$.org_directions" == {{new_org_directions}}
jsonpath "$.org_admins[0]" == {{admin_id}}


GET http://localhost:8000/users/{{owner_id}}/
HTTP 200
[Asserts]
jsonpath "$.organisations_list[0]" == {{org_id}}


GET http://localhost:8000/users/{{admin_id}}/
HTTP 200
[Asserts]
jsonpath "$.organisations_list[0]" == {{org_id}}


#######################################
# Delete an Organisation
#######################################

DELETE http://localhost:8000/organisations/{{org_id}}/
Authorization: Bearer {{owner_access_token}}
HTTP 204

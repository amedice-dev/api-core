#######################################
# Owner Registration
#######################################

GET http://localhost:8000/users/
HTTP 200
[Captures]
user_count: jsonpath "$" count


POST http://localhost:8000/auth/register/
{
    "email": "owner{{user_count}}@test.com",
    "password": "FooFooFoo123",
    "first_name": "Thomas",
    "last_name": "Anderson",
    "user_phone": "+7 777 777 7777",
    "user_role": "Owners"
}
HTTP 201
[Captures]
owner_id: jsonpath "$.id"
owner_email: jsonpath "$.email"
owner_name: jsonpath "$.first_name"


GET http://localhost:8000/users/
HTTP 200
[Asserts]
jsonpath "$[{{user_count}}].id" == {{owner_id}}

#######################################
# Owner Login
#######################################

POST http://localhost:8000/auth/login/
{
    "email": "{{owner_email}}",
    "password": "FooFooFoo123"
}
HTTP 200
[Captures]
owner_access_token: jsonpath "$.access"
owner_refresh_token: jsonpath "$.refresh"

#######################################
# Owner Refresh Token
#######################################

POST http://localhost:8000/auth/refresh/
{
    "refresh": "{{owner_refresh_token}}"
}
HTTP 200
[Captures]
owner_access_token: jsonpath "$.access"

#######################################
# Administrator Registration
#######################################

POST http://localhost:8000/auth/register/
{
    "email": "admin{{user_count}}@test.com",
    "password": "LalaLala123",
    "first_name": "Allison",
    "last_name": "Top",
    "user_phone": "+7 888 888 8888",
    "user_role": "Administrators"
}
HTTP 201
[Captures]
admin_id: jsonpath "$.id"
admin_email: jsonpath "$.email"
admin_name: jsonpath "$.first_name"

#######################################
# Administrator Login
#######################################

POST http://localhost:8000/auth/login/
{
    "email": "{{admin_email}}",
    "password": "LalaLala123"
}
HTTP 200
[Captures]
admin_access_token: jsonpath "$.access"
admin_refresh_token: jsonpath "$.refresh"

#######################################
# Administrator Refresh Token
#######################################

POST http://localhost:8000/auth/refresh/
{
    "refresh": "{{admin_refresh_token}}"
}
HTTP 200
[Captures]
admin_access_token: jsonpath "$.access"

#######################################
# Visitor Registration
#######################################

POST http://localhost:8000/auth/register/
{
    "email": "visitor{{user_count}}@test.com",
    "password": "BooBooBoo123",
    "first_name": "Victor",
    "last_name": "Bottom",
    "user_phone": "+7 999 999 9999",
    "user_role": "Visitors"
}
HTTP 201
[Captures]
visitor_id: jsonpath "$.id"
visitor_email: jsonpath "$.email"
visitor_name: jsonpath "$.first_name"

#######################################
# Visitor Login
#######################################

POST http://localhost:8000/auth/login/
{
    "email": "{{visitor_email}}",
    "password": "BooBooBoo123"
}
HTTP 200
[Captures]
visitor_access_token: jsonpath "$.access"
visitor_refresh_token: jsonpath "$.refresh"

#######################################
# Visitor Refresh Token
#######################################

POST http://localhost:8000/auth/refresh/
{
    "refresh": "{{visitor_refresh_token}}"
}
HTTP 200
[Captures]
visitor_access_token: jsonpath "$.access"

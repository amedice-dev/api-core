from drf_spectacular.utils import OpenApiParameter

ORG_ID_PARAMETER = OpenApiParameter(
    name="org_id",
    description="Уникальное целочисленное значение, идентифицирующее данную организацию.",
    type=int,
    location="path",
    required=True,
)

DOCTOR_ID_PARAMETER = OpenApiParameter(
    name="doc_id",
    description="Уникальное целочисленное значение, идентифицирующее доктора.",
    type=int,
    location="path",
    required=True,
)

USER_ID_PARAMETER = OpenApiParameter(
    name="user_id",
    description="Уникальное целочисленное значение, идентифицирующее пользователя",
    type=int,
    location="path",
    required=True,
)

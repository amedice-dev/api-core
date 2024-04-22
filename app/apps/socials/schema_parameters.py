from drf_spectacular.utils import OpenApiParameter

ORG_ID_PARAMETER = OpenApiParameter(
    name="org_id",
    description="Уникальное целочисленное значение, идентифицирующее данную организацию.",
    type=int,
    location="path",
    required=True,
)

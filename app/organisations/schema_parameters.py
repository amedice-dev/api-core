from drf_spectacular.utils import OpenApiParameter

ID_PARAMETER = OpenApiParameter(
    name="org_id",
    description="Уникальное целочисленное значение, идентифицирующее данную организацию.",
    type=int,
    location="path",
    required=True,
)

CATEGORY_SLUG_PARAMETER = OpenApiParameter(
    name="category_slug",
    description="Уникальное slug значение, идентифицирующее категорию организаций.",
    type=str,
    location="query",
    required=True,
)

ORG_CATEGORY_PARAMETER = OpenApiParameter(
    name="org_category",
    description="Отфильтровать организации по slug категории.",
    type=str,
    location="query",
    required=False,
)

ORG_DIRECTION_PARAMETER = OpenApiParameter(
    name="org_direction",
    description="Отфильтровать организации по slug направления.",
    type=str,
    location="query",
    required=False,
)

PAGE_PARAMETER = OpenApiParameter(
    name="page",
    description="Номер страницы в разбитом на страницы результирующем наборе.",
    type=int,
    location="query",
    required=False,
)

PAGE_SIZE_PARAMETER = OpenApiParameter(
    name="page_size",
    description="Количество возвращаемых результатов на страницу.",
    type=int,
    location="query",
    required=False,
)

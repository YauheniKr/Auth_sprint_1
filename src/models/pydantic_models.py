import orjson
from pydantic import BaseModel as PydanticBaseModel, UUID4


def orjson_dumps(v, *, default):
    return orjson.dumps(v, default=default).decode()


class BaseModel(PydanticBaseModel):
    class Config:
        json_loads = orjson.loads
        json_dumps = orjson_dumps
        allow_population_by_field_name = True


class RoleModel(BaseModel):
    id: UUID4
    role_weight: int
    role_name: str


class RoleUserModel(BaseModel):
    role_weight: int
    role_name: str
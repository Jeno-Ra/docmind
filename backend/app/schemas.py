from pydantic import  BaseModel,Field

class WorkCreate(BaseModel):
    """新增作品时，客户端要提交的数据"""
    title: str = Field(...,min_length=1,max_length=120,description="作品标题")
    type: str = Field(default="text",description="video /image /text /code /project")
    content: str = Field(default="",description="正文或描述")
    tags: list[str] = Field(default_factory=list,description="标签")

class WorkResponse(WorkCreate):
    """返回给客户端的作品：多一个服务端生成的id"""
    id: int
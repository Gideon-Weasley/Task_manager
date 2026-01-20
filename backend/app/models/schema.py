from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class task_detail(BaseModel):
    title:str
    priority:int
    reminder_at:Optional[datetime]=None
    task_date:Optional[date]=None
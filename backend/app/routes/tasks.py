from fastapi import APIRouter

router=APIRouter(prefix="/tasks",tags=["Task Manager"])

@router.get("/gettasks")
def get_tasks(user_id:int):
    return{"user id":user_id,
           "message":"loaded tasks"}
from fastapi import APIRouter
from app.db.db import get_db
from datetime import date
router=APIRouter(prefix="/updates",tags=["Task Updates"])

@router.post("/update_status")
def update_task_status(task_id:int):
    conn=get_db()
    cur=conn.cursor()
    cur.execute("SELECT status,task_date FROM task_manager WHERE task_id=?", (task_id,))
    res=cur.fetchone()
    task_date = date.fromisoformat(res["task_date"])
    if task_date<date.today():
        return{"message":"Cannot update status of past tasks"}
    try:
        if res["status"] ==1:
            cur.execute("UPDATE task_manager SET status=0, completed_at=NULL WHERE task_id=?", (task_id,))
            return{"message":"Task marked as pending"}
        else:
            cur.execute("UPDATE task_manager SET status=1, completed_at=datetime('now') WHERE task_id=?", (task_id,))
            return{"message":"Task marked as completed"}
    finally:
        conn.commit()
        cur.close()
        conn.close()

"endpoint to move the task to another future date"

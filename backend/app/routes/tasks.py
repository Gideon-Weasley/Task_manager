from fastapi import APIRouter
from app.db.db import get_db
from typing import Optional
from datetime import date
from app.models.schema import task_detail
router=APIRouter(prefix="/tasks",tags=["Task Manager"])

@router.get("/getTodaysTasks")
def get_tasks_today():
    conn=get_db()
    cur=conn.cursor()
    cur.execute("SELECT task_id,title,status,task_date FROM task_manager WHERE task_date>=datetime('now','-1 day','+1 second') AND archived=0")
    res=cur.fetchall()
    tasks=[]
    for row in res:
        tasks.append({
            "id":row[0],
            "title":row[1],
            "status":"completed" if row[2]==1 else "pending",
            "created_at":row[3]
        })
    cur.close()
    conn.close()
    return {"tasks":tasks}

@router.get("/getWeeklyTasks")
def get_tasks_week():
    conn=get_db()
    cur=conn.cursor()
    cur.execute("SELECT task_id,title,task_date,status FROM task_manager WHERE task_date>=date('now','-7 day') AND archived=0")
    res=cur.fetchall()
    cur.close()
    conn.close()
    return {"tasks":res}


@router.post("/addtask")
def add_task(task:task_detail):
    conn=get_db()
    cur=conn.cursor()
    cur.execute("INSERT INTO task_manager (title,priority,reminder_at,task_date) VALUES (?,?,COALESCE(?, datetime(COALESCE(?, CURRENT_DATE), '+1 day', '-1 second')),COALESCE(?,CURRENT_DATE))",(task.title,task.priority,task.reminder_at,task.task_date,task.task_date))
    conn.commit()
    task_id=cur.lastrowid
    cur.close()
    conn.close()
    return {"task_id":task_id,
        "message":"Task added successfully"}

@router.get("/search")
def search_task(task_date:Optional[date]=None):
    if task_date is None:
        task_date=date.today()
    conn=get_db()
    cur=conn.cursor()
    cur.execute("SELECT task_id,title,reminder_at,status,created_at FROM task_manager WHERE task_date=? AND archived=0",(task_date,))
    res=cur.fetchall()
    tasks=[]
    for row in res:
        tasks.append({
            "id":row["task_id"],
            "title":row["title"],
            "reminder_at":row["reminder_at"],
            "status": "completed" if row["status"]==1 else "pending",
            "created_at":row["created_at"]
        })
    cur.close()
    conn.close()
    return {"tasks":tasks}
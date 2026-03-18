from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas, database

Base.metadata.create_all(bind=database.engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#CREATE: Add a new task
@app.post("/tasks/", response_model= schemas.TaskResponse)
def create_task(title:str, db: Session = Depends(get_db)):
    new_task = models.Task(title=title)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

#READ: Get all tasks 
@app.get("/tasks/", response_model =  list[schemas.TaskResponse])
def get_tasks(db : Session = Depends(get_db)):
    return db.query(models.Task).all()

#UPDATE: Update a task as done
@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id:int, updated_task: schemas.TaskCreate, db:Session = Depends(get_db)):
    db_task=db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    for key, value in updated_task.dict().items():
        setattr(db_task, key, value)    

    db.commit()
    return db_task  

#DELETE: Delete a task
@app.delete("/tasks/{task_id}")
def delete_task(task_id : int, db:Session = Depends(get_db)):
    db_task=db.query(models.Task).filter(models.Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(db_task)
    db.commit()
    return {"detail": "Task deleted successfully"}


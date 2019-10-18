from ..models import Task

def list():
    return Task.objects.all()

def create(task):
    Task.objects.create(
        title = task.title,
        description = task.description,
        date_expiration = task.date_expiration,
        priority = task.priority
    )

def find_by_id(id):
    return Task.objects.get(id=id)

def edit(old, new):
    old.title = new.title
    old.description = new.description
    old.date_expiration = new.date_expiration
    old.priority = new.priority

    old.save(force_update=True)

def delete(task):
    task.delete()
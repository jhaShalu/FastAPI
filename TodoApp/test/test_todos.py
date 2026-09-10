from ..routers.todos import get_db, get_current_user
from .utils import *
from fastapi import status
from ..models import Todos


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_read_all_authenticated(test_todo):
    response = client.get("/todos/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{'title': 'Learn Python!','description':'Need to learn everyday!', 'priority':5, 'complete':False, 'owner_id': 1, 'id':1}]

def test_read_one_authenticated(test_todo):
    response = client.get("/todos/todo/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'title': 'Learn Python!','description':'Need to learn everyday!', 'priority':5, 'complete':False, 'owner_id': 1, 'id':1}

def test_read_one_authenticated_not_found():
    response = client.get("/todos/todo/3")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Todo not found.'}


def test_create_todo(test_todo):
    request_data = {
        'title': 'Do journaling daily',
        'description': 'It improves thinking and build good habit.',
        'complete': False,
        'priority': 5,
        'owner_id': 1
    }

    response = client.post("/todos/todo/", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED

    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 2).first()
    assert model.title == request_data.get('title')
    assert model.complete == request_data.get('complete')
    assert model.description == request_data.get('description')
    assert model.owner_id == request_data.get('owner_id')
    assert model.priority == request_data.get('priority')


def test_update_todo(test_todo):
    updated_request_data = {
        'title': 'Do journaling daily',
        'description': 'It improves thinking and build good habit.',
        'complete': True,
        'priority': 5,
        'owner_id': 1
    }

    response = client.put("/todos/todo/1", json=updated_request_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT

    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model.title == updated_request_data.get('title')
    assert model.complete == updated_request_data.get('complete')
    assert model.description == updated_request_data.get('description')
    assert model.owner_id == updated_request_data.get('owner_id')
    assert model.priority == updated_request_data.get('priority')


def test_update_todo_not_found(test_todo):
    updated_request_data = {
        'title': 'Do journaling daily',
        'description': 'It improves thinking and build good habit.',
        'complete': True,
        'priority': 5,
        'owner_id': 1
    }

    response = client.put("/todos/todo/5", json=updated_request_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Todo not found.'}


def test_delete_todo(test_todo):
    response = client.delete("/todos/todo/1")

    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id == 1).first()
    assert model is None



def test_delete_todo_not_found(test_todo):
    response = client.delete("/todos/todo/11")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {'detail': 'Todo not found.'}
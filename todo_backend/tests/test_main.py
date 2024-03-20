from fastapi.testclient import TestClient
from sqlmodel import Session
from fastapi_with_neon.route import app
from fastapi_with_neon.db_connector import (testdb_connector, testdb_engine, get_session)
import pytest

# ===============================================================================================================================

#It's a way for us to declare some code that should be run before each test and provide a value for the test function (that's pretty much the same as FastAPI dependencies).In fact, it also has the same trick of allowing to use yield instead of return to provide the value, and then pytest makes sure that the code after yield is executed after the function with the test is done.In pytest, these things are called fixtures instead of dependencies.

@pytest.fixture(name="session")
def session_fixture():
    testdb_connector()
    with Session(testdb_engine) as session:
        yield session

@pytest.fixture(name="client")
def client_fixture(session: Session):   
    def get_session_override():
        return session  
    app.dependency_overrides[get_session] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()
# ===============================================================================================================================


# =========================== here all our test functions which we have created for testing purposes ============================
def test_read_main(client: TestClient):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Home": "Welcome to the FasApi Project!"}

def test_read_todos(client: TestClient):
    response = client.get("/gettodos")
    assert response.status_code == 200
    
def test_create_todo(client: TestClient):
    response = client.post("/createTodo", json="BreakFast")
    assert response.status_code == 200
    assert type(response.json()) == list


def test_update_todo(client: TestClient):
    todo_id = 18
    response = client.put(f"/completeTodo/{todo_id}", json=True)
    assert response.status_code == 200


def test_delete_todo(client: TestClient):
    todo_id = 21
    response = client.delete(f"/deleteTodo?todo_id={todo_id}")
    assert response.status_code == 200
    for item in response.json():
        assert type(item["todo_name"]) is str

# ===============================================================================================================================
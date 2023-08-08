import dataclasses
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi_login import LoginManager
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from dataclasses import dataclass

from fastapi_login.exceptions import InvalidCredentialsException






import os

SECRET = os.environ.get("SECRET_KEY") or os.urandom(24)

app = FastAPI()

templates = Jinja2Templates(directory="templates")

manager = LoginManager(SECRET, '/login')

app.mount("/static", StaticFiles(directory="static"), name="static")


DB = {
    'users': {
        'johndoe@mail.com': {
            'name': 'John Doe',
            'password': 'hunter2'
        }
    }
}

@manager.user_loader()
def query_user(user_id: str):
    """
    Get a user from the db
    :param user_id: E-Mail of the user
    :return: None or the user object
    """
    return DB['users'].get(user_id)



@dataclass
class login:
    email: str
    password: str


@app.post('/login')
def login(data: login):
    email = data.email
    password = data.password

    user = query_user(email)
    if not user:
        # you can return any response or error of your choice
        raise InvalidCredentialsException
    elif password != user['password']:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
    data={'sub': email}
    )
    return {'access_token': access_token}


@app.get('/protected')
def protected_route(user=Depends(manager)):
    return {'user': user}


@app.get("/", response_class=HTMLResponse)
async def render_home_page(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})

@app.post("/messages", response_class=HTMLResponse)
async def render_home_page(request: Request):
    return templates.TemplateResponse("./messages/message.html", context={"request": request})
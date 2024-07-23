import re
from enum import Enum

from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates

from fastapi.staticfiles import StaticFiles
from fastapi_users import fastapi_users, FastAPIUsers
from pydantic import field_validator
from starlette.responses import FileResponse

from auth.auth import auth_backend
from auth.database import Base as User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate


class ModelName(str, Enum):  #перечень страниц
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI(
    title='Green company'
)

templates = Jinja2Templates(
    directory="templates/html")  #есть подозрения что не работает расширение и наследования шаблонизатора,тк он не понимает где файлы хранятся!!!
app.mount("/templates", StaticFiles(directory="templates"),
          name="static")  #подключение директории для статических шаблонов
app.mount("/images", StaticFiles(directory="templates/images"), name="images")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

# роутер регистрации
app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)
# роутер автооризации из документации /auth/register
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

dogs = [{'static': '1', 'templates': '2'}]


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get('/')
async def first_page(request: Request):
    return templates.TemplateResponse("come_in.html", {'request': request})


@app.get('/base')
async def first_page():
    return FileResponse("templates/html/base.html")


#----------------------Registration------------------------------------------
@app.get('/registration')
async def first_page(request: Request):
    return templates.TemplateResponse("registration.html", {'request': request})


@app.get('/registration_organization')
async def first_page(request: Request):
    return templates.TemplateResponse("registration_organization.html", {'request': request})


@app.get('/registration_employee')
async def first_page(request: Request):
    return templates.TemplateResponse("registration_employee.html", {'request': request})


#----------------------stop Registration------------------------------------------
@app.get('/lost_password')
async def first_page(request: Request):
    return templates.TemplateResponse("lost_password.html", {'request': request})



#----------------------organization cabinet------------------------------------------

@app.get('/org_cabinet_users')
async def first_page(request: Request):
    return templates.TemplateResponse("org_cabinet_users.html", {'request': request})


@app.get('/org_cabinet')
async def first_page(request: Request):
    return templates.TemplateResponse("org_cabinet.html", {'request': request})



#----------------------organization cabinet stop------------------------------------------




@app.get('/contact')  #подключили джинжу для данных
async def contact_page(request: Request):
    return templates.TemplateResponse('contact.html', {"request": request, "name": "contact", 'dogs': dogs})




#хорошие практики

@field_validator("phone_number")    #валидация номера телефона
@classmethod
def validate_phone_number(cls, values: str) -> str:
    if not re.match(r'^\+\d{10,15}$', values):
        raise ValueError('Номер телефона должен начинаться с "+" и содержать от 1 до 15 цифр')
    return values
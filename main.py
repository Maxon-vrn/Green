from enum import Enum

from fastapi import FastAPI,Request,Response
from fastapi.templating import Jinja2Templates

from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse


class ModelName(str, Enum): #перечень страниц
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()

templates = Jinja2Templates(directory="templates/html")   #есть подозрения что не работает расширение и наследования шаблонизатора,тк он не понимает где файлы хранятся!!!
app.mount("/templates", StaticFiles(directory="templates"), name="static")    #подключение директории для статических шаблонов
app.mount("/images", StaticFiles(directory="templates/images"), name="images")


dogs= [{'static': '1', 'templates': '2'}]

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}




@app.get('/')
async def first_page(request: Request):
    return templates.TemplateResponse("come_in.html",{'request':request})

@app.get('/base')
async def first_page():
    return FileResponse("templates/html/base.html")

#----------------------Registration------------------------------------------
@app.get('/registration')
async def first_page(request: Request):
    return templates.TemplateResponse("registration.html",{'request':request})
@app.get('/registration_organization')
async def first_page(request: Request):
    return templates.TemplateResponse("registration_organization.html",{'request':request})

@app.get('/registration_employee')
async def first_page(request: Request):
    return templates.TemplateResponse("registration_employee.html",{'request':request})

#----------------------stop Registration------------------------------------------
@app.get('/lost_password')
async def first_page(request: Request):
    return templates.TemplateResponse("lost_password.html",{'request':request})

@app.get('/contact')    #подключили джинжу для данных
async def contact_page(request: Request):
    return templates.TemplateResponse('contact.html', {"request": request,"name":"contact",'dogs': dogs})
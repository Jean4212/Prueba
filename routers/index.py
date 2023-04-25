from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from config.token import decode_token

templates = Jinja2Templates(directory="templates")
index = APIRouter()

@index.route("/", methods=["GET", "POST"])
async def Index(request: Request): 
    access_token = request.cookies.get('access_token')   

    if access_token is None:
        return RedirectResponse(url="/login") 
        
    user = await decode_token(access_token)

    if user:        
        return templates.TemplateResponse("index.html", {"request": request, "user": user})


#@route_index.get("/asistencia", response_class=HTMLResponse)
#def asistencia(request: Request):
#    data = []
#    for num in range(100):
#        line = {"paterno": "Oropeza", "materno": "Inca", "nombre": "Jeancarlos Alberto",
#            "dni": num, "cargo": "Asistente", "distrito": "Chorrillos",
#            "licencia": "A48555618", "categoria": "AIIIC", "revalidacion":"01/01/2022",
#            "nacimiento": "01/01/2000", "ingreso": "01/01/2022"}
#        data.append(line)
#    return templates.TemplateResponse("asistencia.html", {"request": request, "data": data})

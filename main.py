from typing import Optional
from fastapi.responses import HTMLResponse 
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def show_message(name: str = "World", message: str = "I want to be friend"):
    html_content = """
        <html>
            <head><title>Web service </title></head>
            <body>
                <p>Hello """ + name + """! """ + message + """!
            </body>
        </html>
    """
    return HTMLResponse(content = html_content, status_code = 200) 

from typing import Optional
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from frontend.jinja_templates import templates

class ItemBrowserObjectButton:
    def __init__(self,
                 on_click_url: str,
                 name: str = "Unnamed item browser button",
                 hx_target: str = "this",
                 hx_swap: str = "innerHTML",
                 ):
        self.name: str = name
        self.on_click_url: str = on_click_url
        self.hx_target: str = hx_target
        self.hx_swap: str = hx_swap

    def render(self, request: Request) -> HTMLResponse:
        return templates.TemplateResponse("apps/elements/object_browser_button.j2", {"request" : request, "button" : self})

class ItemBrowserObject:
    def __init__(self,
                 title: str = "No title provided",
                 on_click_url: Optional[str] = None,
                 template_path: Optional[str] = None,
                 hx_target: str = None,
                 buttons: list[ItemBrowserObjectButton] = [],
                 ):
        self.title: str = title
        self.on_click_url: Optional[str] = on_click_url
        self.template_path: Optional[str] = template_path
        self.hx_target: str = hx_target
        self.buttons: list[ItemBrowserObjectButton] = buttons

class ItemBrowser:
    def __init__(self,
                 name: str = "Unnamed item browser",
                 refresh_url: Optional[str] = None,
                 toolbar_buttons: Optional[list[ItemBrowserObjectButton]] = [],
                 objects: Optional[list[ItemBrowserObject]] = [],
                 ):
        self.name: str = name

        self.refresh_url: str = refresh_url
        self.toolbar_buttons: list[ItemBrowserObjectButton] = toolbar_buttons

        self.objects: list[ItemBrowserObject] = objects

    def render(self, request: Request) -> HTMLResponse:
        return templates.TemplateResponse("apps/elements/object_browser.j2", {"request" : request, "browser" : self})

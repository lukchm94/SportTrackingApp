from app.__app_configs import ValidationEnum


class Templates(str, ValidationEnum):
    add_player = "tennis/add_player.html"
    success = "tennis/success.html"
    error = "tennis/error.html"


class Urls(str, ValidationEnum):
    root = "/"
    none = ""
    success = "success"
    success_path = f"{success}{root}"
    add_player = "add_player"

from app.__app_configs import ValidationEnum


class Templates(str, ValidationEnum):
    add_player = "tennis/add_player.html"
    success = "tennis/success.html"
    error = "tennis/error.html"


class Urls(str, ValidationEnum):
    root = "/"
    none = ""
    add_player = "add_player"
    success = "success"
    success_path = f"{success}{root}"
    find_player = "find_player"
    find_player_path = f"{find_player}{root}"
    all = "all"
    all_path = f"{all}{root}"

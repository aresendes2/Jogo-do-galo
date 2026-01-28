# main
import tkinter as tk
from pathlib import Path

from game2 import open_game


ASSETS_DIR = Path(__file__).resolve().parent / "assets"


def asset_path(filename: str) -> str:
    return str(ASSETS_DIR / filename)


# Janela
index = tk.Tk()
index.title("Jogo Do Galo")
index.geometry("600x450")
index.resizable(False, False)

# manter referência para não ser garbage-collected
index.img_background = tk.PhotoImage(file=asset_path("2.png"))
lbl_background = tk.Label(index, image=index.img_background)
lbl_background.place(x=0, y=0, relwidth=1, relheight=1)


def start_game(mode: str) -> None:
    open_game(index, mode=mode)
    index.withdraw()


# bt1 - singleplayer
index.btn_single = tk.PhotoImage(file=asset_path("single.png"))
btn_option1 = tk.Button(
    index,
    command=lambda: start_game("single"),
    image=index.btn_single,
    borderwidth=0,
    bg="#f0f0f4",
    highlightthickness=0,
    relief="flat",
    activebackground="#f0f0f4",
)
btn_option1.place(x=0, y=340)

# bt2 - 2 jogadores
index.btn_two = tk.PhotoImage(file=asset_path("two.png"))
btn_option2 = tk.Button(
    index,
    command=lambda: start_game("two"),
    image=index.btn_two,
    borderwidth=0,
    bg="#f0f0f4",
    highlightthickness=0,
    relief="flat",
    activebackground="#f0f0f4",
)
btn_option2.place(x=200, y=350)


index.mainloop()
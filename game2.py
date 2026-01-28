import random
import tkinter as tk
from pathlib import Path
from typing import Optional
from PIL import Image, ImageTk


ASSETS_DIR = Path(__file__).resolve().parent / "assets"


def asset_path(filename: str) -> str:
    return str(ASSETS_DIR / filename)


WIN_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def _winner(board: list[str]) -> Optional[str]:
    for a, b, c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None


def _best_ai_move(board: list[str], ai: str, human: str) -> Optional[int]:
    """IA forte usando minimax (joga sempre o melhor possível)."""

    def minimax(state: list[str], player: str) -> int:
        winner = _winner(state)
        if winner == ai:
            return 1
        if winner == human:
            return -1
        if all(v != "" for v in state):
            return 0

        moves = []
        for i, v in enumerate(state):
            if v != "":
                continue
            new_state = state[:]
            new_state[i] = player
            score = minimax(new_state, ai if player == human else human)
            moves.append((score, i))

        if player == ai:
            # maximizar
            best_score = max(moves, key=lambda x: x[0])[0]
        else:
            # minimizar
            best_score = min(moves, key=lambda x: x[0])[0]

        # devolver um dos melhores movimentos (se vários, escolher aleatoriamente)
        best_indices = [i for s, i in moves if s == best_score]
        return best_indices[0] if player == ai else best_indices[0]

    empty = [i for i, v in enumerate(board) if v == ""]
    if not empty:
        return None

    # IA é sempre 'ai' a jogar agora
    return minimax(board[:], ai)


def open_game(main_window: tk.Tk, mode: str = "single") -> None:
    game = tk.Toplevel(main_window)
    game.title("Jogo Do Galo")
    game.geometry("600x450")
    game.resizable(False, False)

    # background tabuleiro
    game.img_background = tk.PhotoImage(file=asset_path("3.png"))
    lbl_background = tk.Label(game, image=game.img_background)
    lbl_background.place(x=0, y=0, relwidth=1, relheight=1)

    # carregar imagens dos botões (ovo e galinha) e redimensionar para 50x50
    # Guardar no objeto game para não serem apagadas pelo garbage collector
    img_ovo_raw = Image.open(asset_path("jogo (1).png"))
    img_ovo_resized = img_ovo_raw.resize((50, 50), Image.Resampling.LANCZOS)
    game.img_ovo = ImageTk.PhotoImage(img_ovo_resized)  # X = ovo
    
    img_galinha_raw = Image.open(asset_path("jogo.png"))
    img_galinha_resized = img_galinha_raw.resize((50, 50), Image.Resampling.LANCZOS)
    game.img_galinha = ImageTk.PhotoImage(img_galinha_resized)  # O = galinha
    
    # carregar imagens de vitória e derrota e redimensionar para 600x450 (tamanho da janela)
    img_vitoria_raw = Image.open(asset_path("5.png"))
    img_vitoria_resized = img_vitoria_raw.resize((600, 450), Image.Resampling.LANCZOS)
    game.img_vitoria = ImageTk.PhotoImage(img_vitoria_resized)  # Mission Passed!
    
    img_derrota_raw = Image.open(asset_path("4.png"))
    img_derrota_resized = img_derrota_raw.resize((600, 450), Image.Resampling.LANCZOS)
    game.img_derrota = ImageTk.PhotoImage(img_derrota_resized)  # WASTED

    # estado do jogo
    board: list[str] = [""] * 9
    current = "X"  # X começa
    finished = False

    # UI
    status_var = tk.StringVar(value="Vez do Ovo")
    # Fundo preto no multiplayer para destacar
    status_bg = "black" if mode == "two" else "#f0f0f4"
    status_fg = "white" if mode == "two" else "black"
    status_lbl = tk.Label(
        game,
        textvariable=status_var,
        font=("Arial", 16, "bold"),
        bg=status_bg,
        fg=status_fg,
    )
    status_lbl.place(x=210, y=20)

    btns: list[tk.Label] = []

    # coordenadas alinhadas com o teu background
    positions = [
        (170, 90),  (280, 90),  (390, 90),
        (170, 200), (280, 200), (390, 200),
        (170, 310), (280, 310), (390, 310),
    ]

    def update_button(i: int) -> None:
        v = board[i]
        if v == "X":
            # X = ovo
            btns[i].config(
                image=game.img_ovo,
                text="",
                compound="center",
                bg="black",
                activebackground="black",
            )
        elif v == "O":
            # O = galinha
            btns[i].config(
                image=game.img_galinha,
                text="",
                compound="center",
                bg="black",
                activebackground="black",
            )
        else:
            # vazio - sem imagem
            btns[i].config(
                image="",
                text="",
                bg="black",
                activebackground="black",
            )

    # Label para mostrar imagem de vitória/derrota (inicialmente oculta)
    result_label = tk.Label(game, image="", bg="black")
    result_label.place(x=0, y=0, relwidth=1, relheight=1)
    result_label.lower()  # colocar atrás de tudo inicialmente
    
    # Criar botão RESTART antes das funções que o usam
    btn_restart = tk.Button(
        game,
        text="RESTART",
        command=lambda: None,  # será definido depois
        font=("Arial", 12, "bold"),
        bg="#000000",
        activebackground="#e0e0e4",
        borderwidth=2,
        relief="raised",
        cursor="hand2",
    )
    btn_restart.place(x=480, y=400, width=110, height=35)
    btn_restart.lift()  # garantir que está sempre visível
    
    # Criar botão Menu Principal
    btn_menu = tk.Button(
        game,
        text="Menu Principal",
        command=lambda: None,  # será definido depois
        font=("Arial", 12, "bold"),
        bg="#000000",
        activebackground="#e0e0e4",
        borderwidth=2,
        relief="raised",
        cursor="hand2",
    )
    btn_menu.place(x=10, y=400, width=130, height=35)
    btn_menu.lift()  # garantir que está sempre visível
    
    def show_result_image(won: bool) -> None:
        """Mostra a imagem de vitória ou derrota após 3 segundos"""
        if mode == "single":
            if won:
                # Vitória - mostrar Mission Passed!
                result_label.config(image=game.img_vitoria, bg="black")
            else:
                # Derrota - mostrar WASTED
                result_label.config(image=game.img_derrota, bg="black")
            result_label.lift()  # trazer para frente (sobrepor tudo)
            # Garantir que os botões RESTART e Menu Principal ficam visíveis por cima da imagem
            btn_restart.lift()
            btn_menu.lift()
            result_label.update()  # forçar atualização
    
    def set_finished(message: str, won: bool = False, is_tie: bool = False) -> None:
        nonlocal finished
        finished = True
        status_var.set(message)
        # Manter cor do status conforme o modo
        if mode == "two":
            status_lbl.config(bg="black", fg="white")
        else:
            status_lbl.config(bg="#f0f0f4", fg="black")
        
        # Esperar 3 segundos antes de mostrar imagem de vitória/derrota
        # NÃO mostrar imagem se for empate
        if mode == "single" and not is_tie:
            game.after(3000, lambda: show_result_image(won))
        # No modo multiplayer ou empate, não mostrar imagem (só mensagem)

    def check_end() -> bool:
        w = _winner(board)
        if w:
            if mode == "single":
                won = (w == "X")  # X (ovo) ganhou = vitória
                set_finished("Mission Passed!" if won else "WASTED", won=won)
            else:
                # Modo multiplayer - mostrar quem ganhou
                winner_name = "Ovo" if w == "X" else "Galinha"
                set_finished(f"Venceu: {winner_name}")
            return True
        if all(v != "" for v in board):
            set_finished("EMPATE!", is_tie=True)
            return True
        return False

    def ai_play() -> None:
        nonlocal current
        if finished or mode != "single" or current != "O":
            return
        move = _best_ai_move(board, ai="O", human="X")
        if move is None:
            return
        board[move] = "O"
        update_button(move)
        if not check_end():
            current = "X"
            status_var.set("Vez do Ovo")
            # Atualizar cor do status no singleplayer
            status_lbl.config(bg="#f0f0f4", fg="black")

    def on_click(i: int) -> None:
        nonlocal current
        if finished or board[i] != "":
            return
        if mode == "single" and current != "X":
            return

        board[i] = current
        update_button(i)

        if check_end():
            return

        current = "O" if current == "X" else "X"
        # Trocar X por "Ovo" e O por "Galinha"
        if current == "X":
            status_var.set("Vez do Ovo")
        else:
            status_var.set("Vez da Galinha")
        # Atualizar cor do status no multiplayer
        if mode == "two":
            status_lbl.config(bg="black", fg="white")

        if mode == "single":
            # pequeno delay para parecer “humano”
            game.after(250, ai_play)

    # criar 9 \"blocos\" com fundo preto (usamos Label para evitar o estilo branco dos botões no macOS)
    for i, (x, y) in enumerate(positions):
        cell = tk.Label(
            game,
            text="",
            image="",  # começa sem imagem
            bg="black",
            borderwidth=0,
            highlightthickness=1,
            highlightbackground="black",
            relief="flat",
        )
        cell.place(x=x, y=y, width=50, height=50)
        cell.bind("<Button-1>", lambda e, idx=i: on_click(idx))
        btns.append(cell)

    def restart() -> None:
        nonlocal board, current, finished
        board = [""] * 9
        current = "X"
        finished = False
        status_var.set("Vez do Ovo")
        # Esconder imagem de vitória/derrota
        result_label.lower()  # colocar atrás novamente
        result_label.config(image="")
        # Atualizar cor do status se necessário
        if mode == "two":
            status_lbl.config(bg="black", fg="white")
        else:
            status_lbl.config(bg="#f0f0f4", fg="black")
        for i in range(9):
            update_button(i)

    def back_to_menu() -> None:
        game.destroy()
        main_window.deiconify()
    
    # Atualizar os comandos dos botões agora que as funções estão definidas
    btn_restart.config(command=restart)
    btn_menu.config(command=back_to_menu)

    # fechar janela também volta ao menu
    game.protocol("WM_DELETE_WINDOW", back_to_menu)


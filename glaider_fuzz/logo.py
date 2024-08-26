import colorama

RESET = colorama.Style.RESET_ALL
DIM_WHITE = colorama.Style.DIM + colorama.Fore.WHITE
LIGHT_MAGENTA = colorama.Fore.LIGHTMAGENTA_EX
BRIGHT_CYAN = colorama.Fore.LIGHTCYAN_EX  # Changed to LIGHTCYAN_EX for a brighter cyan


def print_logo():
    logo = """

      ██████╗ ██╗      █████╗ ██╗██████╗ ███████╗██████╗ 
     ██╔════╝ ██║     ██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
     ██║  ███╗██║     ███████║██║██║  ██║█████╗  ██████╔╝
     ██║   ██║██║     ██╔══██║██║██║  ██║██╔══╝  ██╔══██╗
     ╚██████╔╝███████╗██║  ██║██║██████╔╝███████╗██║  ██║
      ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝


""".replace('█', f"{DIM_WHITE}█{RESET}").replace(' ', f"{LIGHT_MAGENTA} {RESET}").replace('█',
                                                                                          f"{BRIGHT_CYAN}▓{RESET}").replace(
        '▒', f"{BRIGHT_CYAN}▒{RESET}").replace('Z', f"{BRIGHT_CYAN}▒▒▒▒▒▒{RESET}")
    print(logo)

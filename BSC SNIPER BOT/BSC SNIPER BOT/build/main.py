from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Checkbutton, INSERT
#from tokenSniper import initBot, startStop

def logToLogBox(msg):
    logBox.insert(INSERT, msg + '\n')


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1108x874")
window.configure(bg = "#30363D")
window.title("pjrocks12345 Trading Bot")


canvas = Canvas(
    window,
    bg = "#30363D",
    height = 874,
    width = 1108,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    35.0,
    147.0,
    anchor="nw",
    text="BSC WALLET ADDRESS",
    fill="#CBCFD4",
    font=("Montserrat Regular", 10 * -1)
)

canvas.create_text(
    35.0,
    212.0,
    anchor="nw",
    text="Enter your Binance Smart Chain Address",
    fill="#CBCFD4",
    font=("Montserrat Regular", 10 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    637.5,
    185.0,
    image=entry_image_1
)
bnbAmt = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
bnbAmt.place(
    x=503.0,
    y=165.0,
    width=269.0,
    height=38.0
)
bnbAmt.insert(0, "0.05")

canvas.create_text(
    500.0,
    147.0,
    anchor="nw",
    text="BNB AMOUNT",
    fill="#CBCFD4",
    font=("Montserrat Regular", 10 * -1)
)

canvas.create_text(
    500.0,
    212.0,
    anchor="nw",
    text="BNB Amount to spend on each snipe",
    fill="#CBCFD4",
    font=("Montserrat Regular", 10 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    637.5,
    292.0,
    image=entry_image_2
)
takeProfit = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
takeProfit.place(
    x=503.0,
    y=272.0,
    width=269.0,
    height=38.0
)

takeProfit.insert(0,"1.5")

canvas.create_text(
    500.0,
    254.0,
    anchor="nw",
    text="TAKE PROFIT",
    fill="#CBCFD4",
    font=("Montserrat Regular", 10 * -1)
)

canvas.create_text(
    500.0,
    319.0,
    anchor="nw",
    text="Take Profit amount (Multiple), eg. “3” = 3x BNB Amount",
    fill="#CBCFD4",
    font=("Montserrat Regular", 10 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    637.5,
    399.0,
    image=entry_image_3
)
gasAmt = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
gasAmt.place(
    x=503.0,
    y=379.0,
    width=269.0,
    height=38.0
)

gasAmt.insert(0,"300000")

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    223.0,
    291.0,
    image=entry_image_4
)
privateKey = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
privateKey.place(
    x=38.0,
    y=271.0,
    width=370.0,
    height=38.0
)

privateKey.insert(0,"BSC Wallet Private Key")

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    223.0,
    185.0,
    image=entry_image_5
)
bscAddress = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
bscAddress.place(
    x=38.0,
    y=165.0,
    width=370.0,
    height=38.0
)

bscAddress.insert(0,"BSC Address")

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    223.0,
    503.0,
    image=entry_image_6
)
pancakeSwapRouterAddress = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
pancakeSwapRouterAddress.place(
    x=38.0,
    y=483.0,
    width=370.0,
    height=38.0
)

pancakeSwapRouterAddress.insert(0,"0x10ED43C718714eb63d5aA57B78B54704E256024E")

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    223.0,
    397.0,
    image=entry_image_7
)
bscNode = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
bscNode.place(
    x=38.0,
    y=377.0,
    width=370.0,
    height=38.0
)

bscNode.insert(0,"https://bsc-dataseed.binance.org/")


canvas.create_text(
    500.0,
    361.0,
    anchor="nw",
    text="GAS AMOUNT",
    fill="#CBCFD4",
    font=("Montserrat Regular", 10 * -1)
)

canvas.create_text(
    500.0,
    426.0,
    anchor="nw",
    text="Take Profit amount (Multiple), eg. “3” = 3x BNB Amount",
    fill="#CBCFD4",
    font=("Montserrat Regular", 10 * -1)
)

canvas.create_text(
    35.0,
    253.0,
    anchor="nw",
    text="BSC WALLET PRIVATE KEY",
    fill="#CBCFD4",
    font=("Montserrat Regular", 10 * -1)
)

canvas.create_text(
    35.0,
    318.0,
    anchor="nw",
    text="Enter your Private Key",
    fill="#CBCFD4",
    font=("Montserrat Regular", 10 * -1)
)

canvas.create_text(
    35.0,
    359.0,
    anchor="nw",
    text="BSC NODE",
    fill="#CBCFD4",
    font=("Montserrat Regular", 10 * -1)
)

canvas.create_text(
    35.0,
    424.0,
    anchor="nw",
    text="Leave default or enter your own BSC Node URL",
    fill="#CBCFD4",
    font=("Montserrat Regular", 10 * -1)
)

canvas.create_text(
    35.0,
    465.0,
    anchor="nw",
    text="PANCAKESWAP ROUTER ADDRESS",
    fill="#CBCFD4",
    font=("Montserrat Regular", 10 * -1)
)

canvas.create_text(
    35.0,
    530.0,
    anchor="nw",
    text="Leave default or update if PancakeSwap Router Address has changed",
    fill="#CBCFD4",
    font=("Montserrat Regular", 10 * -1)
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    558.5,
    712.5403747558594,
    image=entry_image_8
)
logBox = Text(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
logBox.place(
    x=35.0,
    y=589.0807495117188,
    width=1047.0,
    height=244.91925048828125
)

canvas.create_text(
    51.867919921875,
    606.3478393554688,
    anchor="nw",
    text="Type here...",
    fill="#CBCFD4",
    font=("Montserrat Regular", 14 * -1)
)

canvas.create_text(
    32.0,
    566.0,
    anchor="nw",
    text="LOGS",
    fill="#CBCFD4",
    font=("Montserrat Regular", 10 * -1)
)

canvas.create_text(
    864.0,
    156.0,
    anchor="nw",
    text="SMART CONTRACT AUDIT CHECKS",
    fill="#CBCFD4",
    font=("Montserrat Regular", 10 * -1)
)



canvas.create_rectangle(
    457.0,
    141.0,
    457.0,
    589.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    809.0,
    141.0,
    810.003173828125,
    454.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    457.0,
    453.98870849609375,
    1085.0,
    455.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    32.0,
    141.0,
    1085.0,
    141.01129150390625,
    fill="#FFFFFF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    554.0,
    71.0,
    image=image_image_1
)

canvas.create_text(
    894.0,
    213.0,
    anchor="nw",
    text="Source Code",
    fill="#CBCFD4",
    font=("Montserrat Regular", 14 * -1)
)

sourceCodeCheck = Checkbutton(
    bd=0,
    highlightthickness=0
)
sourceCodeCheck.place(
    x=864.0,
    y=213.0,
)

canvas.create_text(
    894.0,
    255.0,
    anchor="nw",
    text="Validate Pancake V2",
    fill="#CBCFD4",
    font=("Montserrat Regular", 14 * -1)
)

validatePancake2Check = Checkbutton(
    bd=0,
    highlightthickness=0
)
validatePancake2Check.place(
    x=864.0,
    y=255.0,
)

canvas.create_text(
    894.0,
    298.0,
    anchor="nw",
    text="Mint Function",
    fill="#CBCFD4",
    font=("Montserrat Regular", 14 * -1)
)

mintFunctionCheck = Checkbutton(
    bd=0,
    highlightthickness=0
)
mintFunctionCheck.place(
    x=864.0,
    y=298.0,
)

canvas.create_text(
    894.0,
    340.0,
    anchor="nw",
    text="Honeypot",
    fill="#CBCFD4",
    font=("Montserrat Regular", 14 * -1)
)

honeypotCheck = Checkbutton(
    bd=0,
    highlightthickness=0
)
honeypotCheck.place(
    x=864.0,
    y=340.0,
)

canvas.create_text(
    894.0,
    383.0,
    anchor="nw",
    text="Pancake V1 Router",
    fill="#CBCFD4",
    font=("Montserrat Regular", 14 * -1)
)

pancakeV1RouterCheck = Checkbutton(
    bd=0,
    highlightthickness=0
)
pancakeV1RouterCheck.place(
    x=864.0,
    y=383.0,
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
stopButton = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: logToLogBox("stop"),
    relief="flat"
)
stopButton.place(
    x=782.0,
    y=476.0,
    width=294.0,
    height=90.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
startButton = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: logToLogBox("start"),
    relief="flat"
)
startButton.place(
    x=477.0,
    y=470.0,
    width=294.0,
    height=90.0
)

window.resizable(False, False)
window.mainloop()

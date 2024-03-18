from pysamp.playertextdraw import PlayerTextDraw
from pysamp.textdraw import TextDraw

logo: dict[int, "TextDraw"] = {}
capture_td: dict[int, "TextDraw"]  = {}
squad_capture_td: dict[int, "TextDraw"] = {}
class_selection_td: dict[int, "TextDraw"]  = {}
commands_bottom: dict[int, "TextDraw"]  = {}
commands_bottom_gw: dict[int, "TextDraw"]  = {}
fps_and_ping: dict[int, "TextDraw"]  = {}


def create_textdraws() -> None:
    logo[0] = TextDraw.create(556.000000, 8.088897, "S")
    logo[0].letter_size(0.449999, 1.600000)
    logo[0].alignment(1)
    logo[0].color(-16776961)
    logo[0].set_shadow(0)
    logo[0].set_outline(1)
    logo[0].background_color(51)
    logo[0].font(1)
    logo[0].set_proportional(True)

    logo[1] = TextDraw.create(565.000000, 8.088858, "AGW")
    logo[1].letter_size(0.449999, 1.600000)
    logo[1].alignment(1)
    logo[1].color(-16776961)
    logo[1].set_shadow(0)
    logo[1].set_outline(1)
    logo[1].background_color(51)
    logo[1].font(1)
    logo[1].set_proportional(True)

    logo[2] = TextDraw.create(603.000000, 3.111082, "ld_chat:badchat")
    logo[2].letter_size(0.000000, 0.000000)
    logo[2].text_size(12.000000, 11.200004)
    logo[2].alignment(1)
    logo[2].color(-1)
    logo[2].set_shadow(0)
    logo[2].set_outline(0)
    logo[2].font(4)

    capture_td[0] = TextDraw.create(5.000000, 275.000000, "Time: ")
    capture_td[0].letter_size(0.323332, 1.346961)
    capture_td[0].alignment(1)
    capture_td[0].color(-1)
    capture_td[0].set_shadow(0)
    capture_td[0].set_outline(1)
    capture_td[0].background_color(128)
    capture_td[0].font(1)
    capture_td[0].set_proportional(True)

    capture_td[1] = TextDraw.create(5.000000, 290.000000, "Varios Los Aztecas  ~r~0")
    capture_td[1].letter_size(0.315997, 1.226662)
    capture_td[1].alignment(1)
    capture_td[1].color(-1)
    capture_td[1].set_shadow(0)
    capture_td[1].set_outline(1)
    capture_td[1].background_color(255)
    capture_td[1].font(1)
    capture_td[1].set_proportional(True)

    capture_td[2] = TextDraw.create(5.000000, 300.000000, "Los Santos Vagos  ~r~1")
    capture_td[2].letter_size(0.315997, 1.226662)
    capture_td[2].alignment(1)
    capture_td[2].color(-1)
    capture_td[2].set_shadow(0)
    capture_td[2].set_outline(1)
    capture_td[2].background_color(255)
    capture_td[2].font(1)
    capture_td[2].set_proportional(True)
    capture_td[2].set_outline(1)
    capture_td[2].background_color(255)
    capture_td[2].font(1)
    capture_td[2].set_proportional(True)

    squad_capture_td[0] = TextDraw.create(5.000000, 275.000000, "Time: ")
    squad_capture_td[0].letter_size(0.323332, 1.346961)
    squad_capture_td[0].alignment(1)
    squad_capture_td[0].color(-1)
    squad_capture_td[0].set_shadow(0)
    squad_capture_td[0].set_outline(1)
    squad_capture_td[0].background_color(128)
    squad_capture_td[0].font(1)
    squad_capture_td[0].set_proportional(True)

    squad_capture_td[1] = TextDraw.create(5.000000, 290.000000, "Varios Los Aztecas  ~r~0")
    squad_capture_td[1].letter_size(0.315997, 1.226662)
    squad_capture_td[1].alignment(1)
    squad_capture_td[1].color(-1)
    squad_capture_td[1].set_shadow(0)
    squad_capture_td[1].set_outline(1)
    squad_capture_td[1].background_color(255)
    squad_capture_td[1].font(1)
    squad_capture_td[1].set_proportional(True)

    squad_capture_td[2] = TextDraw.create(5.000000, 300.000000, "Los Santos Vagos  ~r~1")
    squad_capture_td[2].letter_size(0.315997, 1.226662)
    squad_capture_td[2].alignment(1)
    squad_capture_td[2].color(-1)
    squad_capture_td[2].set_shadow(0)
    squad_capture_td[2].set_outline(1)
    squad_capture_td[2].background_color(255)
    squad_capture_td[2].font(1)
    squad_capture_td[2].set_proportional(True)
    squad_capture_td[2].set_outline(1)
    squad_capture_td[2].background_color(255)
    squad_capture_td[2].font(1)
    squad_capture_td[2].set_proportional(True)

    commands_bottom[0] = TextDraw.create(10.000000, 435.000000, "/m - Menu")
    commands_bottom[1] = TextDraw.create(70.000000, 435.000000, "/w - Weapons")
    commands_bottom[2] = TextDraw.create(150.000000, 435.000000, "/v - Vehicles")
    commands_bottom[3] = TextDraw.create(230.000000, 435.000000, "/sm - Set mode")
    commands_bottom[4] = TextDraw.create(150.000000, 425.000000, "/t - Teleport")
    commands_bottom[5] = TextDraw.create(230.000000, 425.000000, "/vt - Tuning")
    for td in commands_bottom.values():
        td.font(2)
        td.letter_size(0.250000, 1.000000)
        td.text_size(400.000000, 17.000000)
        td.set_outline(1)
        td.set_shadow(0)
        td.alignment(1)
        td.color(-1)
        td.background_color(255)
        td.box_color(50)
        td.use_box(False)
        td.set_proportional(True)
        td.set_selectable(False)

    commands_bottom_gw[0] = TextDraw.create(10.000000, 435.000000, "/m - Menu")
    commands_bottom_gw[1] = TextDraw.create(70.000000, 435.000000, "/c - Capture")
    commands_bottom_gw[2] = TextDraw.create(150.000000, 435.000000, "/g - New gang")
    commands_bottom_gw[3] = TextDraw.create(230.000000, 435.000000, "/sm - Set mode")
    for td in commands_bottom_gw.values():
        td.font(2)
        td.letter_size(0.250000, 1.000000)
        td.text_size(400.000000, 17.000000)
        td.set_outline(1)
        td.set_shadow(0)
        td.alignment(1)
        td.color(-1)
        td.background_color(255)
        td.box_color(50)
        td.use_box(False)
        td.set_proportional(True)
        td.set_selectable(False)

    fps_and_ping[0] = TextDraw.create(610.000000, 100.000000, " ")
    fps_and_ping[0].font(2)
    fps_and_ping[0].letter_size(0.250000, 1.500000)
    fps_and_ping[0].text_size(400.000000, 17.000000)
    fps_and_ping[0].set_outline(1)
    fps_and_ping[0].set_shadow(0)
    fps_and_ping[0].alignment(3)
    fps_and_ping[0].color(-1)
    fps_and_ping[0].background_color(255)
    fps_and_ping[0].box_color(50)
    fps_and_ping[0].use_box(False)
    fps_and_ping[0].set_proportional(True)
    fps_and_ping[0].set_selectable(False)
    return print(f"Created: TextDraws (server)")

from pysamp.player import Player
from pysamp.timer import set_timer, kill_timer
from pysamp import (
    gang_zone_flash_for_player,
    gang_zone_hide_for_player,
    gang_zone_stop_flash_for_player,
    gang_zone_show_for_player
)
from pystreamer import (
    create_dynamic_map_icon,
    destroy_dynamic_map_icon
)
from ..database.database import DataBase
from ..gang.gang import GangZoneData, gangs, gangzone_pool
from ..static.textdraws import capture_td
from dataclasses import dataclass
from ..utils.data import ServerMode, Colors, convert_seconds, get_center
from ..utils.consts import TIMER_ID_NONE
from ..static import gangzones
from ..house.house import interiors
import random
from random import randint


@dataclass(frozen=True)
class RandomSpawns:
    spawns = [
        [1751.1097,-2106.4529,13.5469,183.1979], # El-Corona - Outside random house
        [2652.6418,-1989.9175,13.9988,182.7107], # Random house in willowfield - near playa de seville and stadium
        [2489.5225,-1957.9258,13.5881,2.3440], # Hotel in willowfield - near cluckin bell
        [2689.5203,-1695.9354,10.0517,39.5312], # Outside stadium - lots of cars
        [2770.5393,-1628.3069,12.1775,4.9637], # South in east beach - north of stadium - carparks nearby
        [2807.9282,-1176.8883,25.3805,173.6018], # North in east beach - near apartments
        [2552.5417,-958.0850,82.6345,280.2542], # Random house north of Las Colinas
        [2232.1309,-1159.5679,25.8906,103.2939], # Jefferson motel
        [2388.1003,-1279.8933,25.1291,94.3321], # House south of pig pen
        [2481.1885,-1536.7186,24.1467,273.4944], # East LS - near clucking bell and car wash
        [2495.0720,-1687.5278,13.5150,359.6696], # Outside CJ's house - lots of cars nearby
        [2306.8252,-1675.4340,13.9221,2.6271], # House in ganton - lots of cars nearby
        [2191.8403,-1455.8251,25.5391,267.9925], # House in south jefferson - lots of cars nearby
        [1830.1359,-1092.1849,23.8656,94.0113], # Mulholland intersection carpark
        [2015.3630,-1717.2535,13.5547,93.3655], # Idlewood house
        [1654.7091,-1656.8516,22.5156,177.9729], # Right next to PD
        [1219.0851,-1812.8058,16.5938,190.0045], # Conference Center
        [1508.6849,-1059.0846,25.0625,1.8058], # Across the street of BANK - lots of cars in intersection carpark
        [1421.0819,-885.3383,50.6531,3.6516], # Outside house in viod
        [1133.8237,-1272.1558,13.5469,192.4113], # Near hospital
        [1235.2196,-1608.6111,13.5469,181.2655], # Backalley west of mainstreet
        [590.4648,-1252.2269,18.2116,25.0473], # Outside "BAnk of San Andreas"
        [842.5260,-1007.7679,28.4185,213.9953], # North of Graveyard
        [911.9332,-1232.6490,16.9766,5.2999], # LS Film Studio
        [477.6021,-1496.6207,20.4345,266.9252], # Rodeo Place
        [255.4621,-1366.3256,53.1094,312.0852], # Outside propery in richman
        [281.5446,-1261.4562,73.9319,305.0017], # Another richman property
        [790.1918,-839.8533,60.6328,191.9514], # Mulholland house
        [1299.1859,-801.4249,84.1406,269.5274], # Maddoggs
        [1240.3170,-2036.6886,59.9575,276.4659], # Verdant Bluffs
        [2215.5181,-2627.8174,13.5469,273.7786], # Ocean docks 1
        [2509.4346,-2637.6543,13.6453,358.3565], # Ocean Docks spawn 2
        [1435.8024,2662.3647,11.3926,1.1650], #  Northern train station
        [1457.4762,2773.4868,10.8203,272.2754], #  Northern golf club
        [1739.6390,2803.0569,14.2735,285.3929], #  Northern housing estate 1
        [1870.3096,2785.2471,14.2734,42.3102], #  Northern housing estate 2
        [1959.7142,2754.6863,10.8203,181.4731], #  Northern house 1
        [2314.2556,2759.4504,10.8203,93.2711], #  Northern industrial estate 1
        [2216.5674,2715.0334,10.8130,267.6540], #  Northern industrial estate 2
        [2101.4192,2678.7874,10.8130,92.0607], #  Northern near railway line
        [1951.1090,2660.3877,10.8203,180.8461], #  Northern house 2
        [1666.6949,2604.9861,10.8203,179.8495], #  Northern house 3
        [2808.3367,2421.5107,11.0625,136.2060], #  Northern shopping centre
        [2633.3203,2349.7061,10.6719,178.7175], #  V-Rock
        [2606.6348,2161.7490,10.8203,88.7508], #  South V-Rock
        [2616.5286,2100.6226,10.8158,177.7834], #  North Ammunation 1
        [2491.8816,2397.9370,10.8203,266.6003], #  North carpark 1
        [2531.7891,2530.3223,21.8750,91.6686], #  North carpark 2
        [2340.6677,2530.4324,10.8203,177.8630], #  North Pizza Stack
        [2097.6855,2491.3313,14.8390,181.8117], #  Emerald Isle
        [1893.1000,2423.2412,11.1782,269.4385], #  Souvenir shop
        [1698.9330,2241.8320,10.8203,357.8584], #  Northern casino
        [1479.4559,2249.0769,11.0234,306.3790], #  Baseball stadium 1
        [1298.1548,2083.4016,10.8127,256.7034], #  Baseball stadium 2
        [1117.8785,2304.1514,10.8203,81.5490], #  North carparks
        [1108.9878,1705.8639,10.8203,0.6785], #  Dirtring racing 1
        [1423.9780,1034.4188,10.8203,90.9590], #  Sumo
        [1537.4377,752.0641,11.0234,271.6893], #  Church
        [1917.9590,702.6984,11.1328,359.2682], #  Southern housing estate
        [2089.4785,658.0414,11.2707,357.3572], #  Southern house 1
        [2489.8286,928.3251,10.8280,67.2245], #  Wedding chapel
        [2697.4717,856.4916,9.8360,267.0983], #  Southern construction site
        [2845.6104,1288.1444,11.3906,3.6506], #  Southern train station
        [2437.9370,1293.1442,10.8203,86.3830], #  Wedding chapel (near Pyramid)
        [2299.5430,1451.4177,10.8203,269.1287], #  Carpark (near Pyramid)
        [2214.3008,2041.9165,10.8203,268.7626], #  Central parking lot
        [2005.9174,2152.0835,10.8203,270.1372], #  Central motel
        [2222.1042,1837.4220,10.8203,88.6461], #  Clowns Pocket
        [2025.6753,1916.4363,12.3382,272.5852], #  The Visage
        [2087.9902,1516.5336,10.8203,48.9300], #  Royal Casino
        [2172.1624,1398.7496,11.0625,91.3783], #  Auto Bahn
        [2139.1841,987.7975,10.8203,0.2315], #  Come-a-lot
        [1860.9672,1030.2910,10.8203,271.6988], #  Behind 4 Dragons
        [1673.2345,1316.1067,10.8203,177.7294], #  Airport carpark
        [1412.6187,2000.0596,14.7396,271.3568], #  South baseball stadium houses
        [-2723.4639,-314.8138,7.1839,43.5562],  # golf course spawn
        [-2694.5344,64.5550,4.3359,95.0190],  # in front of a house
        [-2458.2000,134.5419,35.1719,303.9446],  # hotel
        [-2796.6589,219.5733,7.1875,88.8288],  # house
        [-2706.5261,397.7129,4.3672,179.8611],  # park
        [-2866.7683,691.9363,23.4989,286.3060],  # house
        [-2764.9543,785.6434,52.7813,357.6817],  # donut shop
        [-2660.9402,883.2115,79.7738,357.4440],  # house
        [-2861.0796,1047.7109,33.6068,188.2750], #  parking lot
        [-2629.2009,1383.1367,7.1833,179.7006],  # parking lot at the bridge
        [-2079.6802,1430.0189,7.1016,177.6486],  # pier
        [-1660.2294,1382.6698,9.8047,136.2952], #  pier 69
        [-1674.1964,430.3246,7.1797,226.1357],  # gas station]
        [-1954.9982,141.8080,27.1747,277.7342],  # train station
        [-1956.1447,287.1091,35.4688,90.4465],  # car shop
        [-1888.1117,615.7245,35.1719,128.4498],  # random
        [-1922.5566,886.8939,35.3359,272.1293],  # random
        [-1983.3458,1117.0645,53.1243,271.2390],  # church
        [-2417.6458,970.1491,45.2969,269.3676],  # gas station
        [-2108.0171,902.8030,76.5792,5.7139],  # house
        [-2097.5664,658.0771,52.3672,270.4487],  # random
        [-2263.6650,393.7423,34.7708,136.4152],  # random
        [-2287.5027,149.1875,35.3125,266.3989],  # baseball parking lot
        [-2039.3571,-97.7205,35.1641,7.4744],  # driving school
        [-1867.5022,-141.9203,11.8984,22.4499],  # factory
        [-1537.8992,116.0441,17.3226,120.8537],  # docks ship
        [-1708.4763,7.0187,3.5489,319.3260],  # docks hangar
        [-1427.0858,-288.9430,14.1484,137.0812],  # airport
        [-2173.0654,-392.7444,35.3359,237.0159],  # stadium
        [-2320.5286,-180.3870,35.3135,179.6980],  # burger shot
        [-2930.0049,487.2518,4.9141,3.8258]  # harbor
    ]


@dataclass(frozen=True)
class DeathMatchSpawns:
    spawns = {
        ServerMode.deathmatch_world_shotgun: (
            (-397.1293, 2250.9568, 42.4297, 290.0000),
            (-367.7202, 2255.0208, 42.4844, 195.0000) ,
            (-347.1474, 2230.7024, 42.4885, 100.0000),
            (-360.3025, 2201.7686, 42.4844, 15.0000),
            (-391.4041, 2195.4341, 42.4163, 5.0000),
            (-428.4577, 2204.6074, 42.4297, 280.0000),
            (-417.8091, 2236.6167, 42.4297, 280.0000),
        ),

        ServerMode.deathmatch_world_oc_deagle: (
            (-397.1293, 2250.9568, 42.4297, 290.0000),
            (-367.7202, 2255.0208, 42.4844, 195.0000) ,
            (-347.1474, 2230.7024, 42.4885, 100.0000),
            (-360.3025, 2201.7686, 42.4844, 15.0000),
            (-391.4041, 2195.4341, 42.4163, 5.0000),
            (-428.4577, 2204.6074, 42.4297, 280.0000),
            (-417.8091, 2236.6167, 42.4297, 280.0000),
        ),

        ServerMode.deathmatch_world_old_country: (
            (-397.1293, 2250.9568, 42.4297, 290.0000),
            (-367.7202, 2255.0208, 42.4844, 195.0000) ,
            (-347.1474, 2230.7024, 42.4885, 100.0000),
            (-360.3025, 2201.7686, 42.4844, 15.0000),
            (-391.4041, 2195.4341, 42.4163, 5.0000),
            (-428.4577, 2204.6074, 42.4297, 280.0000),
            (-417.8091, 2236.6167, 42.4297, 280.0000),
        ),
        ServerMode.deathmatch_world_farm: (
            (1055.6105, -366.2527, 73.9922,  90.0000),
            (1019.3500, -302.0771, 73.9931, 180.0000),
            (1045.9434, -296.9352, 73.9931, 180.0000),
            (1113.2708, -319.7141, 73.9922, 90.0000),
        ),
        ServerMode.deathmatch_world_abandoned_country: (
            (-1309.9337, 2487.3464, 87.1753, 360.0000),
            (-1283.0154, 2515.2380, 87.1064, 85.0000),
            (-1304.1638, 2557.9167, 86.8784, 85.0000),
        ),
        ServerMode.deathmatch_world_kass: (
            (2546.1135, 2837.3240, 10.8203, 0.0000),
            (2543.4514, 2810.3254, 10.8203, 270.0000),
            (2592.6772, 2847.3723, 10.8203, 185.0000),
            (2606.2842, 2807.8652, 10.8203, 0.0000),
        ),
    }


class DeathMatch:
    @staticmethod
    def give_guns_for_player(player: Player) -> None:
        if player.mode == ServerMode.deathmatch_world_oc_deagle:
            return player.give_weapon(24, 100)

        if player.mode == ServerMode.deathmatch_world_shotgun:
            return player.give_weapon(26, 100)

        player.give_weapon(24, 100)
        player.give_weapon(25, 100)
        player.give_weapon(31, 100)

    @classmethod
    def show_gangzones_for_player(cls, player: Player) -> None:
        cls.hide_gangzones_for_player(player)
        gz = gangzones.deathmatch[player.mode]
        gz.show_for_player(player, 0xBBBBBBAA)

    @staticmethod
    def hide_gangzones_for_player(player: Player) -> None:
        for gz in gangzones.deathmatch.values():
            gz.hide_for_player(player)

    @staticmethod
    def is_player_in_gangzone(player: Player) -> None:
        if not player.mode in ServerMode.deathmatch_worlds:
            return

        gz = gangzones.deathmatch[player.mode]
        if not player.is_in_area(gz.min_x, gz.min_y, gz.max_x, gz.max_y):
            i = randint(0, len(DeathMatchSpawns.spawns[player.mode]) - 1)
            player.set_pos(DeathMatchSpawns.spawns[player.mode][i][0], DeathMatchSpawns.spawns[player.mode][i][1], DeathMatchSpawns.spawns[player.mode][i][2])
            player.set_facing_angle(DeathMatchSpawns.spawns[player.mode][i][3])
            return player.send_notification_message("Вы были перемещены!")

    @staticmethod
    def set_spawn_info_for_player(player: Player):
        i = randint(0, len(DeathMatchSpawns.spawns[player.mode]) - 1)
        player.set_spawn_info(
            255,
            player.skin,
            DeathMatchSpawns.spawns[player.mode][i][0],
            DeathMatchSpawns.spawns[player.mode][i][1],
            DeathMatchSpawns.spawns[player.mode][i][2],
            DeathMatchSpawns.spawns[player.mode][i][3],
            0, 0, 0, 0, 0, 0)

    @classmethod
    def enable_mode_for_player(cls, player: Player):
        i = randint(0, len(DeathMatchSpawns.spawns[player.mode]) - 1)
        player.hide_bottom_commands()
        player.remove_unused_vehicle(ServerMode.freeroam_world)
        player.set_camera_behind()
        player.set_interior(0)
        player.set_color_ex(Colors.deathmatch)
        player.set_health(100.0)
        player.reset_weapons()
        GangWar.disable_gangzones_for_player(player)
        GangWar.hide_capture_textdraws(player)
        cls.show_gangzones_for_player(player)
        cls.give_guns_for_player(player)
        player.set_pos(
            DeathMatchSpawns.spawns[player.mode][i][0],
            DeathMatchSpawns.spawns[player.mode][i][1],
            DeathMatchSpawns.spawns[player.mode][i][2]
        )
        player.set_facing_angle(DeathMatchSpawns.spawns[player.mode][i][3])
        cls.set_spawn_info_for_player(player)
        cls.enable_timer_for_player(player)

    @classmethod
    def enable_timer_for_player(cls, player: Player) -> None:
        if player.timers.deathmatch_in_area == TIMER_ID_NONE:
            player.timers.deathmatch_in_area = set_timer(cls.is_player_in_gangzone, 1000, True, player)

    @classmethod
    def disable_timer_for_player(cls, player: Player) -> None:
        if player.timers.deathmatch_in_area != TIMER_ID_NONE:
            kill_timer(player.timers.deathmatch_in_area)
            player.timers.deathmatch_in_area = TIMER_ID_NONE


class Freeroam:
    @staticmethod
    def update_gun_slots_for_player(player: Player, slots) -> None:
        player.gun_slots.melee = slots.slot_melee
        player.gun_slots.pistol = slots.slot_pistol
        player.gun_slots.shotgun = slots.slot_shotgun
        player.gun_slots.machine_gun = slots.slot_machine_gun
        player.gun_slots.assault_rifle = slots.slot_assault_rifle
        player.gun_slots.long_rifle = slots.slot_long_rifle

    @staticmethod
    def give_guns_for_player(player: Player) -> None:
        player.give_weapon(player.gun_slots.melee, 100)
        player.give_weapon(player.gun_slots.pistol, 100)
        player.give_weapon(player.gun_slots.shotgun, 100)
        player.give_weapon(player.gun_slots.machine_gun, 100)
        player.give_weapon(player.gun_slots.assault_rifle, 100)
        player.give_weapon(player.gun_slots.long_rifle, 100)

    @staticmethod
    def set_spawn_info_for_player(player: Player) -> None:
        i = randint(0, len(RandomSpawns.spawns) - 1)
        player.set_spawn_info(
            255,
            player.skin,
            RandomSpawns.spawns[i][0],
            RandomSpawns.spawns[i][1],
            RandomSpawns.spawns[i][2],
            RandomSpawns.spawns[i][3],
            0, 0, 0, 0, 0, 0)

    @classmethod
    def enable_mode_for_player(cls, player: Player) -> None:
        player.show_bottom_commands()
        player.remove_unused_vehicle(ServerMode.freeroam_world)
        player.set_camera_behind()
        player.set_color_ex(randint(0, 16777215))
        player.reset_weapons()
        player.set_health(100.0)
        GangWar.disable_gangzones_for_player(player)
        GangWar.hide_capture_textdraws(player)
        DeathMatch.hide_gangzones_for_player(player)
        DeathMatch.disable_timer_for_player(player)
        if player.settings.spawn_in_house and player.house:
            # Если стоит спавн в доме и есть дом
            player.checks.in_house = True
            x, y, z = interiors[player.house.interior_id]
            player.set_pos(x, y, z)
            player.set_camera_behind()
            player.set_interior(player.house.interior_id)
            player.set_mode(player.house.interior_id + 1000)

        else:
            player.checks.in_house = False
            i = randint(0, len(RandomSpawns.spawns) - 1)
            player.set_pos(RandomSpawns.spawns[i][0], RandomSpawns.spawns[i][1], RandomSpawns.spawns[i][2])
            player.set_facing_angle(RandomSpawns.spawns[i][3])
            player.set_interior(0)

        cls.give_guns_for_player(player)
        player.game_text(f"Welcome~n~{player.get_name()}", 2000, 1)
        cls.set_spawn_info_for_player(player)


class GangWar:
    capture_dict: dict[str, tuple[str, int, int, str, str]] = {}

    @staticmethod
    def set_spawn_info_for_player(player: Player) -> None:
        player.set_spawn_info(
            255,
            player.skin,
            player.gang.spawn_pos[0],
            player.gang.spawn_pos[1],
            player.gang.spawn_pos[2],
            0.0, 0, 0, 0, 0, 0, 0)

    @classmethod
    def enable_mode_for_player(cls, player: Player) -> None:
        player.show_bottom_commands()
        player.reset_weapons()
        player.remove_unused_vehicle(ServerMode.freeroam_world)
        DeathMatch.hide_gangzones_for_player(player)
        DeathMatch.disable_timer_for_player(player)
        player.set_pos(player.gang.spawn_pos[0], player.gang.spawn_pos[1], player.gang.spawn_pos[2])
        player.set_camera_behind()
        player.set_interior(player.gang.interior_id)
        player.set_health(100.0)
        player.set_skin_ex(random.choice(player.gang.skins))
        player.set_color_ex(player.gang.color)
        cls.show_gangzones_for_player(player)
        if player.gang.is_capturing:
            gz = gangzone_pool[player.gang.capture_id]
            gz_db = DataBase.load_gangzone(gz.id)
            x, y = get_center(gz_db.min_x, gz_db.max_x, gz_db.min_y, gz_db.max_y)
            gang_zone_flash_for_player(player.id, player.gang.capture_id, gangs[gz.gang_atk_id].color)
            cls.show_capture_textdraws_for_player(player)

        player.game_text(f"Welcome~n~{player.gang.game_text_color}{player.get_name()}", 2000, 1)
        cls.set_spawn_info_for_player(player)

    @staticmethod
    def show_gangzones_for_player(player: Player) -> None:
        gangzones = DataBase.load_gangzones()
        for i in gangzones:
            gang_zone_show_for_player(player.id, i.id, i.color)

    @staticmethod
    def reload_gangzones_for_player(player: Player):
        gangzones = DataBase.load_gangzones()
        for i in gangzones:
            gang_zone_hide_for_player(player.id, i.id)
            gang_zone_show_for_player(player.id, i.id, i.color)

    @staticmethod
    def disable_gangzones_for_player(player: Player):
        gangzones = DataBase.load_gangzones()
        for i in gangzones:
            gang_zone_hide_for_player(player.id, i.id)

    @staticmethod
    def show_capture_textdraws_for_player(player: Player) -> None:
        for td in capture_td.values():
            td.show_for_player(player)

    @staticmethod
    def hide_capture_textdraws(player: Player) -> None:
        for td in capture_td.values():
            td.hide_for_player(player)

    @staticmethod
    def update_capture_textdraw(gz: GangZoneData):
        h, m, s = convert_seconds(gz.capture_time)
        capture_td[0].set_string(f"Time: {m}:{s}")
        capture_td[1].set_string(f"{gangs[gz.gang_atk_id].gang_name} ~r~{gz.gang_atk_score}")
        capture_td[1].color(gangs[gz.gang_atk_id].color)
        capture_td[2].set_string(f"{gangs[gz.gang_def_id].gang_name} ~r~{gz.gang_def_score}")
        capture_td[2].color(gangs[gz.gang_def_id].color)

    @classmethod
    def send_capture_message(cls, initiator: Player, player: Player) -> None:
        _capt = cls.capture_dict[initiator.name]
        player.send_notification_message(
            f"{{{gangs[_capt[1]].color_hex}}}{initiator.name}{{{Colors.white_hex}}} инициировал захват территории {{{Colors.cmd_hex}}}{_capt[4]}{{{Colors.white_hex}}}!"
        )
        player.send_notification_message(
            f"Началась война между {{{gangs[_capt[1]].color_hex}}}{gangs[_capt[1]].gang_name}{{{Colors.white_hex}}} и {{{gangs[_capt[2]].color_hex}}}{gangs[_capt[2]].gang_name}{{{Colors.white_hex}}}!"
        )

    @classmethod
    def start_capture(cls, player: Player, registry: dict[int, "Player"]) -> None: # player - Игрок, начавший захват
        _capt = cls.capture_dict[player.name]
        gz_db = DataBase.load_gangzone(_capt[3])
        x, y = get_center(gz_db.min_x, gz_db.max_x, gz_db.min_y, gz_db.max_y)
        gz = gangzone_pool[_capt[3]]
        gz.gang_atk_id = _capt[1]
        gz.gang_def_id = _capt[2]
        gz.gang_atk_score = 0
        gz.gang_def_score = 0
        gz.capture_time = 900
        gz.capture_cooldown = 0
        gz.is_capture = True
        del cls.capture_dict[player.name]
        cls.update_capture_textdraw(gz)
        for player in registry.values(): # Общий показ текстдрава капта для двух банд
            if player.mode != ServerMode.gangwar_world:
                continue

            if (player.gang_id == gz.gang_atk_id) or (player.gang_id == gz.gang_def_id):
                player.set_team(player.gang_id)
                player.send_notification_message("Во время войны урон по своим был отключён!")
                gang_zone_flash_for_player(player.id, gz.id, gangs[gz.gang_atk_id].color)
                GangWar.show_capture_textdraws_for_player(player)

        create_dynamic_map_icon(x, y, 0.0, gangs[gz.gang_atk_id].map_icon, 0, world_id=ServerMode.gangwar_world, interior_id=0, style=1)

    @staticmethod
    def end_capture(gangzone: GangZoneData, registry: dict[int, "Player"]) -> None:
        win = False
        if gangzone.gang_atk_score >= gangzone.gang_def_score:
            win = True
            gangzone.gang_id = gangzone.gang_atk_id
            gangzone.color = gangs[gangzone.gang_id].color

        DataBase.save_gangzone(
            id=gangzone.id,
            gang_id=gangzone.gang_id,
            color=gangzone.color,
            capture_cooldown=900,
        )
        for player in registry.values():
            if player.mode != ServerMode.gangwar_world:
                continue

            if (player.gang_id == gangzone.gang_atk_id) or (player.gang_id == gangzone.gang_def_id):
                player.set_team(255)
                player.send_notification_message(f"Банда {{{gangs[gangzone.gang_atk_id].color_hex}}}{gangs[gangzone.gang_atk_id].gang_name}{{{Colors.white_hex}}} {'захватила' if win else 'не смогла захватить'} территорию!")
                player.send_notification_message(f"Счёт: {{{gangs[gangzone.gang_atk_id].color_hex}}}{gangzone.gang_atk_score}{{{Colors.white_hex}}} - {{{gangs[gangzone.gang_def_id].color_hex}}}{gangzone.gang_def_score}{{{Colors.white_hex}}}.")
                GangWar.hide_capture_textdraws(player)
                gang_zone_stop_flash_for_player(player.id, gangzone.id)
                GangWar.reload_gangzones_for_player(player)

        destroy_dynamic_map_icon(0)
        destroy_dynamic_map_icon(1)
        atk_gang = gangs[gangzone.gang_atk_id]
        atk_gang.capture_id = -1
        atk_gang.is_capturing = False
        def_gang = gangs[gangzone.gang_def_id]
        def_gang.capture_id = -1
        def_gang.is_capturing = False
        gangzone.gang_atk_id = 0
        gangzone.gang_def_id = 0
        gangzone.gang_atk_score = 0
        gangzone.gang_def_score = 0
        gangzone.capture_time = 0
        gangzone.capture_cooldown = 900
        gangzone.is_capture = False
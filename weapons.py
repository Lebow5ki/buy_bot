from telebot import types
# PISTOLS = ['Glock-18', 'USP-S','Dual Berettas', 'P250', 'Tec-9', 'CZ75-Auto', 'Desert Eagle', 'R8 Revolver', 'P2000', 'Five-SeveN']
# PPS = ['MAC-10', 'MP7', 'UMP-45', 'P90', 'PP-Bizon', 'MP9']
# SHOTGUNS = ['Nova']
# HEAVY = ['M249']
# ARS = ['M4A4']
GUN_TYPES = ['PISTOLS', 'PPS', 'SHOTGUNS', 'HEAVY', 'ARS']
GUNS = {
    'PISTOLS': ['Glock-18', 'USP-S','Dual Berettas', 'P250', 'Tec-9', 'CZ75-Auto', 'Desert Eagle', 'R8 Revolver', 'P2000', 'Five-SeveN'],
    'PPS': ['MAC-10', 'MP7', 'UMP-45', 'P90', 'PP-Bizon', 'MP9'],
    'SHOTGUNS': ['Nova'],
    'HEAVY':  ['M249'],
    'ARS': ['M4A4']
    }



def gun_types():
    inl = types.ReplyKeyboardMarkup(resize_keyboard=True)
    def GetWeapType(inl):
        inl.add(
            types.KeyboardButton('SHOTGUNS'),
            types.KeyboardButton('HEAVY'),
            types.KeyboardButton('ARS'),
            types.KeyboardButton('PISTOLS')
        )
        return inl


    # inl = types.InlineKeyboardMarkup(row_width=1)
    # item = types.InlineKeyboardButton('DOTA2', callback_data='ok')


    # def GetKeyboardFowWeapon(weapon):
    #     inl = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     for key, value in GUNS.items():
    #         if key == weapon:
    #             print(value)
    #             for weapon in value:
    #                 inl.add(types.KeyboardButton(weapon))
    #     return inl
    #
    # def GetKeyboarsForPistols(PISTOLS):
    #     inl = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     for weapon in PISTOLS:
    #         inl.add(types.KeyboardButton(weapon))
    #     return inl
    GetWeapType(inl)



# MAC-10 = give weapon_mac10
# MP7 = give weapon_mp7
# UMP-45 = give weapon_ump45
# P90 = give weapon_p90
# PP-Bizon = give weapon_bizon
# Контр-террористы
#
# MP9 = give weapon_mp9
# MP7 = give weapon_mp7
# UMP-45 = give weapon_ump45
# P90 = give weapon_p90
# PP-Bizon = give weapon_bizon
# print(GetKeyboardFowWeapon('ARS'))
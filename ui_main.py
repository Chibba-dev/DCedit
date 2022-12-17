from PyQt5 import QtWidgets, uic
import os
import json
import glob


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()  # Call the inherited classes __init__ method
        uic.loadUi('deadcellsui.ui', self)  # Load the .ui file

         # USER: set paths to modding CDB and vanilla extracted CDB
        self.modded_folder_path = 'D:\\DeadCells\\ExpandedCDB\\'
        self.vanilla_folder_path = 'D:\\DeadCells\\vanillaCDB\\'

        # USER: add Weapon Name and json name to dict
        self.fast_weapons = {
            'Assassin\'s Dagger': '008---BackStabber.json',
            'Bladed Tonfas': '108---ElbowBlades.json',
            'Blood Sword': '010---Bleeder.json',
            'Ferryman\'s Lantern': '044---Lantern.json',
            'Ferryman\'s Offhand': '045---LanternOffHand.json',
            'Hard Light Gun': '036---HardLightGun.json',
            'Hard Light Sword': '035---HardLightSword.json',
            'Hattori\'s Katana': '103---Katana.json',
            'Hayabusa Boots': '021---MultiKickBoots.json',
            'King Scepter': '115---KingScepter.json',
            'Panchaku': '119---NunchuckPan.json',
            'Pure Nail': '052---PureNail.json',
            'Queen\'s Rapier': '111---QueenRapier.json',
            'Sadist\'s Stiletto': '004---BleedCrit.json',
            'Snake Fangs': '042---SnakeFang.json',
            'Starfury': '120---Starfury.json',
            'Twin Daggers': '007---DualDaggers.json',
            'Valmont\'s Whip': '030---Whip.json',
        }

        # USER: add Weapon Name and json name to dict
        self.slow_weapons = {
            'Broadsword': '011---BroadSword.json',
            'Giantkiller': '015---GiantKiller.json',
            'Gold Digger': '113---GoldDigger.json',
            'Nutcracker': '018---StunMace.json',
            'Scythe Claw Left': '038---TickScytheLeft.json',
            'Scythe Claw Right': '039---TickScytheRight.json',
            'Symmetrical Lance': '025---KingsSpear.json',
            'Tombstone': '048---Tombstone.json',
            'War Spear': '023---Spear.json',
            'Wrecking Ball': '110---WreckingBall.json',
        }

        # USER: add Weapon Name and json name to dict
        self.ranged_weapons = {
            'Alchemic Carbine': '070---AlchemicGun.json',
            'Electric Whip': '097---LightningWhip.json',
            'Explosive Crossbow': '068---ExplosiveCrossBow.json',
            'Explosive Offhand': '069---ExplosiveCrossBowOffHand.json',
            'Gilded Yumi': '109---HeavyBow.json',
            'Hemorrhage': '075---BleedAxe.json',
            'Hokuto\'s Bow': '071---MarkBow.json',
            'Ice Crossbow': '066---FrostCrossBow.json',
            'Ice Offhand': '067---FrostCrossBowOffHand.json',
            'Ice Shards': '100---ThrowingIce.json',
            'Laser Glaive': '118---LaserGlaive.json',
            'Lightning Bolt': '096---Lightning.json',
            'Magic Missiles': '094---MagicSalve.json',
            'Nerves of Steel': '072---PreciseBow.json',
            'Quick Bow': '060---FastBow.json',
            'Repeater Crossbow': '064---MultiCrossBow.json',
            'Repeater Offhand': '065---MultiCrossBowOffHand.json',
            'Sonic Carbine': '058---SonicCrossbow.json',
            'Throwing Knife': '073---ThrowingKnife.json',
            'War Javelin': '077---ThrowingSpear.json',
        }

        # USER: add Name and json name to dict (these are simply opened in the windows default app for json
        self.json_file_to_load = {
            'Adrenaline_DodgeHeal(M)': r'item\Perk\343---P_DodgeHeal.json',
            'Blind Faith_CDR_Parry(M)': r'item\Perk\365---P_CDR_Parry.json',
            'Counterattack_DmgParry(M)': r'item\Perk\366---P_DmgParry.json',
            'Initiative_DmgFirstHit(M)': r'item\Perk\347---P_DmgFirstHit.json',
            'Kill Rhythm_AttackSpeed_Combo(M)': r'item\Perk\374---P_AttackSpeed_Combo.json',
            'Melee_Slow enemy on melee(M)': r'item\Perk\339---P_ManyMobsAround.json',
            'Necromancy_HealOnKill(M)': r'item\Perk\368---P_HealOnKill.json',
            'Open Wounds_Bleeding on hit(M)': r'item\Perk\341---P_Bleed.json',
            'Soldier\'s Resistance_More Health(M)': r'item\Perk\363---P_ScaledHealth.json',
            'Spite_SuperParry(M)': r'item\Perk\371---P_SuperParry.json',
            'Vengeance_Buff on damage taken(M)': r'item\Perk\338---P_DmgRevenge.json',
            'What Doesn\'t Kill Me_HealOnParry(M)': r'item\Perk\367---P_HealOnParry.json',
            'Acrobatipack_Backpack_Ranged(M)': r'item\Perk\362---P_Backpack_Ranged.json',
            'Porcupack_Backpack_Melee(M)': r'item\Perk\349---P_Backpack_Melee.json',
            'Armadillopack_Backpack_Shield(M)': r'item\Perk\375---P_Backpack_Shield.json',
            'Barbed Tips_Dot on arrows(M)': r'item\Perk\355---P_DmgPlantedArrow.json',
            'Parting Gift(M)': r'item\Perk\351---P_DeathBomb.json',
            'Point Blank_Close-range damagebuff(M)': r'item\Perk\356---P_DmgNearRanged.json',
            'Support_DeployedDmg(M)': r'item\Perk\350---P_DeployedDmg.json',
            'Tranquility_NoMobAround(M)': r'item\Perk\352---P_NoMobAround.json',
            'Velocity_SpeedBuff(M)': r'item\Perk\380---P_SpeedBuff.json',
            'Lightspeed(Power)': r'item\Power\046---Dash.json',
            'Scarecrow\'s Sickles(Power)': r'item\Power\056---GardenerSickles.json',
            'Tombstone(Weapon)': r'item\Melee\116---Tombstone.json',
            'Bleed Propagation(Affix)': r'affix\Advanced\118---BleedPropagation.json',
            'Giantkiller(Weapon)': r'item\Melee\083---GiantKiller.json',
            'Hokuto\'s Bow(Weapon)': r'item\Ranged\157---MarkBow.json',
            'Nerves of Steel(Weapon)': r'item\Ranged\158---PreciseBow.json',
        }

        for entry in self.fast_weapons.keys():
            self.comboBox_fast.addItem(entry)
        for entry in self.slow_weapons.keys():
            self.comboBox_slow.addItem(entry)
        for entry in self.ranged_weapons.keys():
            self.comboBox_ranged.addItem(entry)
        for entry in self.json_file_to_load.keys():
            self.comboBox_json.addItem(entry)

        self.spin_box_list = [self.power_1,
                         self.power_2,
                         self.power_3,
                         self.power_4,
                         self.power_5,
                         self.power_6,
                         self.power_7,
                         self.power_8,
                         self.power_9,
                         self.power_10]

        self.double_spin_box_list = [self.crit_1,
                         self.crit_2,
                         self.crit_3,
                         self.crit_4,
                         self.crit_5,
                         self.crit_6,
                         self.crit_7,
                         self.crit_8,
                         self.crit_9,
                         self.crit_10]

        self.current_item_path = None
        self.modded_data = None

        for item in self.spin_box_list:
            item.valueChanged.connect(self.compute)
        for item in self.double_spin_box_list:
            item.valueChanged.connect(self.compute)

        self.comboBox_fast.currentIndexChanged.connect(self.load_from_comboBox)
        self.comboBox_slow.currentIndexChanged.connect(self.load_from_comboBox)
        self.comboBox_ranged.currentIndexChanged.connect(self.load_from_comboBox)
        self.comboBox_json.currentIndexChanged.connect(self.open_a_json)
        self.write_json.clicked.connect(self.write_data)
        self.show()  # Show the GUI

    def vanillaOut(self, path):
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        dpsData = ''
        hitsData = ''
        crit = 0.0
        time = 0.0
        timePerHit = 0.0
        damage = 0.0
        critDamage = 0.0
        counting = 1
        dpsData = f'{dpsData}{data["item"]}, '
        for item in data["strikeChain"]:
            if "critMul" in item.keys():
                crit = float(item["critMul"])
            if crit == 0.0 and item["canCrit"]:
                crit = 1.0
            damage = damage + float(item["power"][0])
            if crit > 0:
                critDamage = critDamage + float(item["power"][0]) * 2 * crit
            else:
                critDamage = critDamage + float(item["power"][0])
            # if len(strikeChain) == 1:
            if len(data["strikeChain"]) == 1:
                timePerHit = item["charge"] + max(item["lockCtrlAfter"], item["coolDown"])
                time = timePerHit
            else:
                timePerHit = float(item["charge"]) + float(item["lockCtrlAfter"])
                time = time + timePerHit
            if crit == 0:
                hitsData = hitsData + f'{counting} Hit: Damage: {item["power"][0]}   Cannot Crit    Time: {round(timePerHit, 2)}\n\n'
            else:
                hitsData = hitsData + f'{counting} Hit: Damage: {item["power"][0]}   CritMul: {crit} Time: {round(timePerHit, 2)}\n\n'
            counting += 1
        dpsData = dpsData + f'DPS: {round(damage / time)}    CritDPS: {round(critDamage / time)}\n'
        return f'{dpsData}\n{hitsData}'


    def moddedOut(self):
        with open(self.current_item_path, encoding='utf-8') as f:
           self.modded_data = json.load(f)
        for item1, item2 in zip(self.spin_box_list, self.double_spin_box_list):
            item1.setValue(0)
            item2.setValue(0.0)
            item1.setEnabled(False)
            item2.setEnabled(False)


        for i, item in enumerate(self.modded_data["strikeChain"]):
            self.spin_box_list[i].setValue(item['power'][0])
            self.spin_box_list[i].setEnabled(True)
            if "critMul" in item.keys():
                self.double_spin_box_list[i].setValue(float(item["critMul"]))
                self.double_spin_box_list[i].setEnabled(True)

    def open_a_json(self):
        os.startfile(f'{self.modded_folder_path}{self.json_file_to_load[self.comboBox_json.currentText()]}')

    def write_data(self):
        if not self.current_item_path:
            print('no data loaded!!!')
            return
        for i, item in enumerate(self.spin_box_list):
            if int(item.value()) != 0:
                self.modded_data["strikeChain"][i]['power'][0] = item.value()
        for i, item in enumerate(self.double_spin_box_list):
            if item.value() != 0.0:
                self.modded_data["strikeChain"][i]['critMul'] = round(item.value(), 2)

        with open(self.current_item_path, 'w', encoding = 'utf-8') as outfile:
            json.dump(self.modded_data, outfile, indent= 2, ensure_ascii=False)
        print('Saved Json')

    def compute(self):
        if not self.current_item_path:
            print('no data loaded!!!')
            return
        time_accu = 0.0
        combo = 0
        critical_damage = 0
        crit_accu = 0
        display_critical = ''
        for i, item in enumerate(self.modded_data["strikeChain"]):
            combo += self.spin_box_list[i].value()
            if self.double_spin_box_list[i].value() > 0:
                critical_damage = round(self.spin_box_list[i].value() * 2 * self.double_spin_box_list[i].value())
                crit_accu += critical_damage
                display_critical += f'{i+1} Hit Critical Damage = {critical_damage}\n'
            elif self.double_spin_box_list[i].value() == 0 and self.modded_data["strikeChain"][i]['canCrit'] == True:
                critical_damage = round(self.spin_box_list[i].value() * 2)
                crit_accu += critical_damage
                display_critical += f'{i+1} Hit Critical Damage = {critical_damage}\n'
            else:
                crit_accu += self.spin_box_list[i].value()

            if self.power_2.value() > 0:
                time_accu += self.modded_data['strikeChain'][i]["charge"] + self.modded_data['strikeChain'][i]["lockCtrlAfter"]
            else:
                time_accu = self.modded_data['strikeChain'][0]["charge"] + max(self.modded_data['strikeChain'][0]["lockCtrlAfter"], self.modded_data['strikeChain'][0]["coolDown"])
        if time_accu != 0.0:
            self.info_1.setText(f'DPS: {round(combo / time_accu)}    CritDPS: {round(crit_accu / time_accu)}\n{display_critical}')
        else:
            self.info_1.setText('Time for combo/attack is 0')

    def load_from_comboBox(self, combo_box):
        combo_name = self.sender().objectName()
        if combo_name == 'comboBox_fast':
            self.vanillainformation.setText(
                self.vanillaOut(
                    f'{self.vanilla_folder_path}weapon\\{self.fast_weapons[self.comboBox_fast.currentText()]}'))
            self.current_item_path = f'{self.modded_folder_path}weapon\\{self.fast_weapons[self.comboBox_fast.currentText()]}'
            self.comboBox_fast.setEditable(True)
            self.comboBox_slow.setEditable(False)
            self.comboBox_ranged.setEditable(False)
            self.comboBox_fast.setStyleSheet("QComboBox::editable"
                                         "{"
                                         "background-color: lightgreen;"
                                         "}")
        elif combo_name == 'comboBox_slow':
            self.vanillainformation.setText(
                self.vanillaOut(
                    f'{self.vanilla_folder_path}weapon\\{self.slow_weapons[self.comboBox_slow.currentText()]}'))
            self.current_item_path = f'{self.modded_folder_path}weapon\\{self.slow_weapons[self.comboBox_slow.currentText()]}'
            self.comboBox_fast.setEditable(False)
            self.comboBox_slow.setEditable(True)
            self.comboBox_ranged.setEditable(False)
            self.comboBox_slow.setStyleSheet("QComboBox::editable"
                                         "{"
                                         "background-color: lightgreen;"
                                         "}")
        else:
            self.vanillainformation.setText(
                self.vanillaOut(
                    f'{self.vanilla_folder_path}weapon\\{self.ranged_weapons[self.comboBox_ranged.currentText()]}'))
            self.current_item_path = f'{self.modded_folder_path}weapon\\{self.ranged_weapons[self.comboBox_ranged.currentText()]}'
            self.comboBox_fast.setEditable(False)
            self.comboBox_slow.setEditable(False)
            self.comboBox_ranged.setEditable(True)
            self.comboBox_ranged.setStyleSheet("QComboBox::editable"
                                         "{"
                                         "background-color: lightgreen;"
                                         "}")
        self.moddedOut()
        self.compute()






# DCedit
DCedit is a basic python script that runs from a Graphical User Interface (GUI) using PyQt5

<img width="362" alt="gui" src="https://user-images.githubusercontent.com/69771680/208263412-7690a45b-659a-42b8-940b-d26de59cf6a0.png">

The idea is to comfortably edit weapon damage for the weapon combos and see updated DPS and Critical DPS values for the changes in real time.
The unmodded (Vanilla) values are displayed on the left side for comparison.

**Play with your personal weapon balance with a few clicks!**

# Usage:
This is a basic but fully functional script with hardcoded paths for the weapons that are set via two variables for a vanilla folder and a working (modding) directory.
There are four dictionaries to fill that populate the four dropdown menus.

One for fast weapons, slow and lastly ranged. The fourth dropdown can take any json file path and opens it with the windows default app when selected.

Changes are **saved** when the 'write to json' button is pressed.

# In the Code:
All changes are done in **ui_main.py**

line 13 and 14 for the two paths

17 for the fast weapon dropdown

39 for slow wepaons

53 for ranged weapons

77 for select json files to be opened regularly

# Version
This is a basic first version, eventually I plan to add config files so there are no more hardcoded parts.

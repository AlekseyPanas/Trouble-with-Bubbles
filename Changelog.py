def get_current_version():
    return "v1.3"


def print_changes(version):
    if version == "ALPHA v1.0":
        print("- Added ball bouncing physics")
        print("- Added ball splitting")
        print("- Added player")
        print("- Added shooting ability")
        print("- Added ball-player collision")
        print("- Added game over screen")
        print("- Added blank screen as placeholder for menu")
        print("- Added timer")
        print("- Tweaked physics values to best simulate actual Bubble Trouble game")
    elif version == "BETA v1.1":
        print("- Fixed timer animation")
        print("- Tweaked values")
        print("- Added score and highscore saving")
        print("- Added lives")
        print("- Added new screens for when you get hit by ball and when time runs out")
    elif version == "v1.2":
        print("- Fixed lag")
        print("- Added menu")
        print("- Added player animation")
    elif version == "v1.3":
        print("- Score is now added for combos and for popping balls")
        print("- A combo popup appears when a combo is performed")
        print("- Added a pause menu")


def get_versions_in_order():
    return ["ALPHA v1.0", "BETA v1.1", "v1.2", "v1.3"]


def print_future_updates():
    print("- Add ball flags which will be passed down to each ball")
    print("- Add walls")
    print("- Add lowering ceiling")
    print("- Add arrays to specify custom ball split height and side speed")
    print("- Add powerups")
    print("- Add accounts and leader boards")
    print("- Add achievements")
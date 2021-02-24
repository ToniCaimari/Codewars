def hero(bullets, dragons):
    ammo = dragons*2
    if bullets-ammo < 0:
        return False
    else:
        return True

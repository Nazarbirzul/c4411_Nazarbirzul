class BuildingError(Exception):
    def __str__(self):
        return f"With so mush material the house cannot be built!"

def check_material(amount_of_material, limit_value):
    if amount_of_material < limit_value:
        raise "Enough material"
    else:
        return BuildingError(amount_of_material)

material = 123
check_material(material, 300)





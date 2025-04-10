import modules.unit as unit

INFANTRY = unit.UnitType(150,
                         50,
                         20,
                         30,
                         70,
                         "resources/units/infantry.jpg")

AMPHIBIAN_INFANTRY = unit.UnitType(50,
                         50,
                         20,
                         0,
                         60,
                         "resources/units/amphibian_infantry.jpg")

MOUNTAIN_INFANTRY = unit.UnitType(80,
                         50,
                         30,
                         60,
                         100,
                         "resources/units/mountain_infantry.jpg")

NAVAL_UNIT = unit.UnitType(60,
                         40,
                         40,
                         0,
                         30,
                         "resources/units/naval_unit.jpg")

RECONNAISSANCE = unit.UnitType(90,
                         100,
                         10,
                         30,
                         80,
                         "resources/units/reconnaissance.jpg")

ARMY_COMPOSITION = [INFANTRY,
                    INFANTRY,
                    INFANTRY,
                    INFANTRY,
                    AMPHIBIAN_INFANTRY,
                    AMPHIBIAN_INFANTRY,
                    MOUNTAIN_INFANTRY,
                    MOUNTAIN_INFANTRY,
                    NAVAL_UNIT,
                    NAVAL_UNIT,
                    RECONNAISSANCE,
                    RECONNAISSANCE
                    ]

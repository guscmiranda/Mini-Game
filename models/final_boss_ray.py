robot_shot_cores = {

    "casco": {
        "interior": (120,120,120),
        "borda": (30,30,30)
    },

    "energia": {
        "interior": (255,80,0),
        "borda": (255,200,0)
    }
}

robot_shot_partes = {

    "casco": [
        [
            (-12,-18),
            (-18,0),
            (-12,18),
            (12,18),
            (18,0),
            (12,-18)
        ],
        "polygon"
    ],

    "energia": [
        {
            "centro": (0,0),
            "raio": 6
        },
        "circle"
    ]
}

##########################################################################

demon_fireball_partes = {

    "fogo_externo": [
        [
            (0,-25),
            (-18,-5),
            (-25,20),
            (0,35),
            (25,20),
            (18,-5)
        ],
        "polygon"
    ],

    "fogo_interno": [
        [
            (0,-15),
            (-10,0),
            (-12,12),
            (0,20),
            (12,12),
            (10,0)
        ],
        "polygon"
    ]
}

demon_fireball_cores = {

    "fogo_externo": {
        "interior": (255,80,0),
        "borda": (120,0,0)
    },

    "fogo_interno": {
        "interior": (255,240,100),
        "borda": (255,150,0)
    }
}
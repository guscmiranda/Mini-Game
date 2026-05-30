bomba_cores = {

    "corpo": {
        "interior": (90, 90, 100),
        "borda": (30, 30, 30)
    },

    "anel": {
        "interior": (140, 140, 150),
        "borda": (40, 40, 40)
    },

    "olho_externo": {
        "interior": (180, 40, 40),
        "borda": (20, 20, 20)
    },

    "olho_interno": {
        "interior": (255, 220, 80),
        "borda": (0, 0, 0)
    },

    "espinho_topo": {
        "interior": (220, 220, 220),
        "borda": (20, 20, 20)
    },

    "espinho_baixo": {
        "interior": (220, 220, 220),
        "borda": (20, 20, 20)
    },

    "espinho_esq": {
        "interior": (220, 220, 220),
        "borda": (20, 20, 20)
    },

    "espinho_dir": {
        "interior": (220, 220, 220),
        "borda": (20, 20, 20)
    },

    "luz_esq": {
        "interior": (255, 120, 0),
        "borda": (255, 220, 100)
    },

    "luz_dir": {
        "interior": (255, 120, 0),
        "borda": (255, 220, 100)
    }
}

bomba_partes = {

    "corpo": [
        {
            "centro": (0, 0),
            "raio": 35
        },
        "circle"
    ],

    "anel": [
        {
            "centro": (0, 0),
            "raio": 28
        },
        "circle"
    ],

    "olho_externo": [
        {
            "centro": (0, 0),
            "raio": 12
        },
        "circle"
    ],

    "olho_interno": [
        {
            "centro": (0, 0),
            "raio": 5
        },
        "circle"
    ],

    "espinho_topo": [
        [
            (0, -55),
            (-8, -30),
            (8, -30)
        ],
        "polygon"
    ],

    "espinho_baixo": [
        [
            (0, 55),
            (-8, 30),
            (8, 30)
        ],
        "polygon"
    ],

    "espinho_esq": [
        [
            (-55, 0),
            (-30, -8),
            (-30, 8)
        ],
        "polygon"
    ],

    "espinho_dir": [
        [
            (55, 0),
            (30, -8),
            (30, 8)
        ],
        "polygon"
    ],

    "luz_esq": [
        {
            "centro": (-18, 18),
            "raio": 4
        },
        "circle"
    ],

    "luz_dir": [
        {
            "centro": (18, 18),
            "raio": 4
        },
        "circle"
    ]
}
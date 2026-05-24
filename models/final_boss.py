boss_cores = {

    "corpo_central": {
        "interior": (130, 130, 130),
        "borda": (40, 40, 40)
    },

    "olho_externo": {
        "interior": (180, 30, 30),
        "borda": (20, 20, 20)
    },

    "olho_interno": {
        "interior": (255, 220, 60),
        "borda": (0, 0, 0)
    },

    "pupila": {
        "interior": (10, 10, 10),
        "borda": (0, 0, 0)
    },

    "asa_esq_superior": {
        "interior": (160, 20, 20),
        "borda": (0, 0, 0)
    },

    "asa_esq_inferior": {
        "interior": (120, 120, 120),
        "borda": (0, 0, 0)
    },

    "asa_dir_superior": {
        "interior": (160, 20, 20),
        "borda": (0, 0, 0)
    },

    "asa_dir_inferior": {
        "interior": (120, 120, 120),
        "borda": (0, 0, 0)
    },

    "canhao_esq": {
        "interior": (220, 220, 220),
        "borda": (30, 30, 30)
    },

    "canhao_dir": {
        "interior": (220, 220, 220),
        "borda": (30, 30, 30)
    },

    "canhao_esq_miolo": {
        "interior": (200, 20, 20),
        "borda": (0, 0, 0)
    },

    "canhao_dir_miolo": {
        "interior": (200, 20, 20),
        "borda": (0, 0, 0)
    },

    "espinho_topo_centro": {
        "interior": (240, 210, 80),
        "borda": (0, 0, 0)
    },

    "espinho_topo_esq": {
        "interior": (240, 210, 80),
        "borda": (0, 0, 0)
    },

    "espinho_topo_dir": {
        "interior": (240, 210, 80),
        "borda": (0, 0, 0)
    },

    "perna_esq": {
        "interior": (100, 100, 100),
        "borda": (0, 0, 0)
    },

    "perna_dir": {
        "interior": (100, 100, 100),
        "borda": (0, 0, 0)
    },

    "broca_esq": {
        "interior": (255, 180, 40),
        "borda": (0, 0, 0)
    },

    "broca_dir": {
        "interior": (255, 180, 40),
        "borda": (0, 0, 0)
    },

    "motor_central": {
        "interior": (160, 20, 20),
        "borda": (0, 0, 0)
    },

    "fogo_motor": {
        "interior": (255, 140, 0),
        "borda": (255, 220, 80)
    }
}

boss_partes = {

    # núcleo principal
    "corpo_central": [
        [
            (-90, -120),
            (-280, 40),
            (-80, 140),
            (80, 140),
            (280, 40),
            (90, -120)
        ],
        "polygon"
    ],

    # olho central maligno
    "olho_externo": [
        {
            "centro": (0, 0),
            "raio": 45
        },
        "circle"
    ],

    "olho_interno": [
        {
            "centro": (0, 0),
            "raio": 22
        },
        "circle"
    ],

    # pupila vertical
    "pupila": [
        [
            (0, -30),
            (-8, 0),
            (0, 30),
            (8, 0)
        ],
        "polygon"
    ],

    # asas laterais gigantes
    "asa_esq_superior": [
        [
            (-140, -30),
            (-260, -70),
            (-220, 20)
        ],
        "polygon"
    ],

    "asa_esq_inferior": [
        [
            (-140, 60),
            (-240, 130),
            (-170, 120)
        ],
        "polygon"
    ],

    "asa_dir_superior": [
        [
            (140, -30),
            (260, -70),
            (220, 20)
        ],
        "polygon"
    ],

    "asa_dir_inferior": [
        [
            (140, 60),
            (240, 130),
            (170, 120)
        ],
        "polygon"
    ],

    # canhões laterais
    "canhao_esq": [
        {
            "centro": (-250, 10),
            "raio": 40
        },
        "circle"
    ],

    "canhao_dir": [
        {
            "centro": (250, 10),
            "raio": 40
        },
        "circle"
    ],

    # centro dos canhões
    "canhao_esq_miolo": [
        {
            "centro": (-250, 10),
            "raio": 18
        },
        "circle"
    ],

    "canhao_dir_miolo": [
        {
            "centro": (250, 10),
            "raio": 18
        },
        "circle"
    ],

    # espinhos superiores
    "espinho_topo_centro": [
        [
            (0, -170),
            (-35, -110),
            (35, -110)
        ],
        "polygon"
    ],

    "espinho_topo_esq": [
        [
            (-70, -130),
            (-95, -80),
            (-45, -80)
        ],
        "polygon"
    ],

    "espinho_topo_dir": [
        [
            (70, -130),
            (95, -80),
            (45, -80)
        ],
        "polygon"
    ],

    # pernas mecânicas inferiores
    "perna_esq": [
        [
            (-70, 140),
            (-110, 240),
            (-50, 220)
        ],
        "polygon"
    ],

    "perna_dir": [
        [
            (70, 140),
            (110, 240),
            (50, 220)
        ],
        "polygon"
    ],

    # brocas inferiores
    "broca_esq": [
        [
            (-80, 240),
            (-110, 300),
            (-50, 300)
        ],
        "polygon"
    ],

    "broca_dir": [
        [
            (80, 240),
            (110, 300),
            (50, 300)
        ],
        "polygon"
    ],

    # motor central
    "motor_central": [
        [
            (-40, 140),
            (40, 140),
            (55, 210),
            (-55, 210)
        ],
        "polygon"
    ],

    # chama do motor
    "fogo_motor": [
        [
            (0, 300),
            (-30, 210),
            (30, 210)
        ],
        "polygon"
    ]
}

# ---------------

boss_cores = {
    # Estruturas de fundo / anexos
    "antena_haste": {"interior": (100, 100, 100), "borda": (0, 0, 0)},
    "domo_superior": {"interior": (255, 50, 150), "borda": (0, 0, 0)},  # Rosa tóxico brilhante
    "canhao_esq": {"interior": (200, 80, 0), "borda": (0, 0, 0)},
    "canhao_dir": {"interior": (200, 80, 0), "borda": (0, 0, 0)},

    # Corpo Principal
    "base_disco": {"interior": (50, 50, 65), "borda": (0, 0, 0)},  # Aço escuro

    # Rosto Maluco
    "boca_fundo": {"interior": (10, 10, 10), "borda": (0, 0, 0)},  # Breu total
    "dente_1": {"interior": (240, 240, 220), "borda": (0, 0, 0)},  # Branco sujo
    "dente_2": {"interior": (240, 240, 220), "borda": (0, 0, 0)},
    "dente_3": {"interior": (240, 240, 220), "borda": (0, 0, 0)},
    "dente_4": {"interior": (240, 240, 220), "borda": (0, 0, 0)},

    "olho_esq": {"interior": (255, 230, 40), "borda": (0, 0, 0)},  # Amarelo insano
    "olho_dir": {"interior": (255, 230, 40), "borda": (0, 0, 0)},
    "pupila_esq": {"interior": (220, 0, 0), "borda": (0, 0, 0)},  # Vermelho
    "pupila_dir": {"interior": (220, 0, 0), "borda": (0, 0, 0)},

    # Detalhes finais por cima de tudo
    "antena_bola": {"interior": (0, 255, 255), "borda": (0, 0, 0)}  # Ciano brilhante
}

boss_partes = {

    # 1. Antena e Domo (Ficam por trás do corpo principal)
    "antena_haste": [
        [(-5, -120), (5, -120), (8, -50), (-8, -50)],
        "polygon"
    ],

    "domo_superior": [
        {
            "centro": (0, -50),
            "raio": 80
        },
        "circle"
    ],

    # 2. Armas laterais (ângulos agressivos e irregulares)
    "canhao_esq": [
        [(-140, -10), (-190, -30), (-210, 10), (-160, 0)],
        "polygon"
    ],

    "canhao_dir": [
        [(140, -10), (190, -30), (210, 10), (160, 0)],
        "polygon"
    ],

    # 3. Corpo Principal (Cobre a base do domo e os canhões)
    "base_disco": [
        [(-160, -10), (-100, -30), (100, -30), (160, -10), (120, 50), (-120, 50)],
        "polygon"
    ],

    # 4. Boca e Dentes (Sorriso gigante estilo vilão)
    "boca_fundo": [
        [(-90, 20), (90, 20), (60, 45), (-60, 45)],
        "polygon"
    ],

    "dente_1": [
        [(-80, 20), (-65, 35), (-50, 20)],
        "polygon"
    ],

    "dente_2": [
        [(-40, 20), (-25, 42), (-10, 20)],  # Dente mais longo
        "polygon"
    ],

    "dente_3": [
        [(10, 20), (25, 30), (40, 20)],  # Dente quebrado/menor
        "polygon"
    ],

    "dente_4": [
        [(50, 20), (65, 38), (80, 20)],
        "polygon"
    ],

    # 5. Olhos Assimétricos (A alma do estilo Cuphead)
    "olho_esq": [
        {
            "centro": (-50, -10),
            "raio": 28  # Olho esquerdo maior
        },
        "circle"
    ],

    "olho_dir": [
        {
            "centro": (50, 0),
            "raio": 22  # Olho direito menor e mais baixo
        },
        "circle"
    ],

    "pupila_esq": [
        {
            "centro": (-45, -5),
            "raio": 6  # Pupila minúscula
        },
        "circle"
    ],

    "pupila_dir": [
        {
            "centro": (50, 5),
            "raio": 10  # Pupila dilatada
        },
        "circle"
    ],

    # 6. Ponta da antena (Por cima de tudo)
    "antena_bola": [
        {
            "centro": (0, -130),
            "raio": 15
        },
        "circle"
    ]
}
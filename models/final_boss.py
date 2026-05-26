#--------------- v1
boss1_cores = {

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

boss1_partes = {

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

#--------------- v2

boss2_cores = {
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

boss2_partes = {

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

#--------------- v3

boss3_partes = {

    # ── CORPO CENTRAL ──────────────────────────────────────────────
    "corpo_central": [
        [(-100, -140), (100, -140), (150, 0), (-150, 0)],
        "polygon"
    ],

    "triangulo_interno": [
        [(-60, -110), (60, -110), (80, -20), (-80, -20)],
        "polygon"
    ],

    # ── OLHO CENTRAL ───────────────────────────────────────────────
    "olho_aro_externo": [
        {"centro": (0, -65), "raio": 38},
        "circle"
    ],

    "olho_iris": [
        {"centro": (0, -65), "raio": 27},
        "circle"
    ],

    "olho_pupila": [
        {"centro": (0, -65), "largura": 13, "altura": 22},
        "ellipse"
    ],

    # ── GRADE DE PONTOS (peito abaixo do olho) ─────────────────────
    "grade_peito": [
        [(-55, 2), (55, 2), "espacamento", 20, "pontos", 6],
        "dot_row"   # 6 círculos r=4 espaçados horizontalmente
    ],

    # ── OMBROS ─────────────────────────────────────────────────────
    "ombro_esq": [
        [(-165, -65), (-110, -65), (-110, -10), (-165, -10)],
        "polygon"
    ],

    "ombro_dir": [
        [(110, -65), (165, -65), (165, -10), (110, -10)],
        "polygon"
    ],

    "gem_ombro_esq": [
        {"centro": (-137, -37), "raio": 16},
        "circle"
    ],

    "gem_ombro_dir": [
        {"centro": (137, -37), "raio": 16},
        "circle"
    ],

    # ── ASAS INTERNAS (entre ombro e canhão) ───────────────────────
    "asa_esq": [
        [(-165, -65), (-225, -37), (-165, -10)],
        "polygon"
    ],

    "asa_dir": [
        [(165, -65), (225, -37), (165, -10)],
        "polygon"
    ],

    # ── CANHÕES LATERAIS ───────────────────────────────────────────
    "canhao_esq": [
        {"centro": (-262, -37), "largura": 95, "altura": 35},
        "rect_arredondado"
    ],

    "canhao_dir": [
        {"centro": (262, -37), "largura": 95, "altura": 35},
        "rect_arredondado"
    ],

    "gem_canhao_esq": [
        {"centro": (-237, -37), "raio": 13},
        "circle"
    ],

    "gem_canhao_dir": [
        {"centro": (237, -37), "raio": 13},
        "circle"
    ],

    # Pontas dos canhões (triângulos apontando para os lados)
    "ponta_canhao_esq": [
        [(-310, -50), (-280, -37), (-310, -22)],
        "polygon"
    ],

    "ponta_canhao_dir": [
        [(310, -50), (280, -37), (310, -22)],
        "polygon"
    ],

    # ── GEMAS SUPERIORES DOS CANHÕES (esferas com suporte) ─────────
    "gem_topo_canhao_esq": [
        {"centro": (-215, -85), "raio": 9},
        "circle"
    ],

    "gem_topo_canhao_dir": [
        {"centro": (215, -85), "raio": 9},
        "circle"
    ],

    # ── SPIKES / TRIÂNGULOS DECORATIVOS ────────────────────────────
    "spikes_topo": [
        # três triângulos no topo do corpo central
        [
            [(-25, -140), (-18, -170), (-11, -140)],
            [(-7,  -140), (0,  -178), (7,   -140)],
            [(11,  -140), (18, -170), (25,  -140)],
        ],
        "polygon_group"
    ],

    "spikes_laterais_esq": [
        [
            [(-165, -65), (-185, -78), (-165, -52)],
            [(-165, -38), (-190, -37), (-165, -18)],
        ],
        "polygon_group"
    ],

    "spikes_laterais_dir": [
        [
            [(165, -65), (185, -78), (165, -52)],
            [(165, -38), (190, -37), (165, -18)],
        ],
        "polygon_group"
    ],

    "spikes_inf_esq": [
        [
            [(-100, 0), (-115, 28), (-85, 15)],
            [(-70,  5), (-82,  30), (-56, 20)],
        ],
        "polygon_group"
    ],

    "spikes_inf_dir": [
        [
            [(100, 0), (115, 28), (85, 15)],
            [(70,  5), (82,  30), (56, 20)],
        ],
        "polygon_group"
    ],

    # ── GEMA DO TOPO (apex) ────────────────────────────────────────
    "gem_apex": [
        {"centro": (0, -148), "raio": 7},
        "circle"
    ],

    # ── CINTURA (conector corpo → propulsores) ─────────────────────
    "cintura": [
        [(-35, 0), (35, 0), (35, 35), (-35, 35)],
        "polygon"
    ],

    "gem_cintura": [
        {"centro": (0, 17), "raio": 8},
        "circle"
    ],

    # ── PROPULSOR CENTRAL ──────────────────────────────────────────
    "propulsor_central": [
        [(-20, 35), (20, 35), (20, 85), (-20, 85)],
        "polygon"
    ],

    "chama_central_esq": [
        [(-20, 85), (-10, 118), (0, 85)],
        "polygon"
    ],

    "chama_central_meio": [
        [(-10, 85), (0, 122), (10, 85)],
        "polygon"
    ],

    "chama_central_dir": [
        [(0, 85), (10, 118), (20, 85)],
        "polygon"
    ],

    # ── PROPULSORES INFERIORES LATERAIS ────────────────────────────
    "propulsor_esq_a": [
        [(-125, 20), (-93, 20), (-93, 62), (-125, 62)],
        "polygon"
    ],

    "propulsor_esq_b": [
        [(-90, 25), (-62, 25), (-62, 63), (-90, 63)],
        "polygon"
    ],

    "propulsor_dir_a": [
        [(93, 20), (125, 20), (125, 62), (93, 62)],
        "polygon"
    ],

    "propulsor_dir_b": [
        [(62, 25), (90, 25), (90, 63), (62, 63)],
        "polygon"
    ],

    "chama_propulsor_esq_a": [
        [(-125, 62), (-116, 82), (-108, 62)],
        "polygon"
    ],

    "chama_propulsor_esq_b": [
        [(-90, 63), (-82, 80), (-74, 63)],
        "polygon"
    ],

    "chama_propulsor_dir_a": [
        [(108, 62), (116, 82), (125, 62)],
        "polygon"
    ],

    "chama_propulsor_dir_b": [
        [(74, 63), (82, 80), (90, 63)],
        "polygon"
    ],
}

boss3_cores = {

    "corpo_central": {
        "interior": (158, 158, 155),   # cinza médio
        "borda":    (90,  0,   0)      # bordô escuro
    },

    "triangulo_interno": {
        "interior": (120, 118, 115),
        "borda":    (100, 5,   5)
    },

    "olho_aro_externo": {
        "interior": (20,  20,  20),    # quase preto
        "borda":    (140, 0,   0)      # vermelho escuro
    },

    "olho_iris": {
        "interior": (200, 160, 0),     # âmbar/dourado
        "borda":    (50,  50,  50)
    },

    "olho_pupila": {
        "interior": (15,  12,  0),     # preto esverdeado
        "borda":    (0,   0,   0)
    },

    "grade_peito": {
        "interior": (200, 160, 0),     # dourado
        "borda":    (100, 80,  0)
    },

    "ombro_esq": {
        "interior": (136, 136, 132),
        "borda":    (90,  0,   0)
    },

    "ombro_dir": {
        "interior": (136, 136, 132),
        "borda":    (90,  0,   0)
    },

    "gem_ombro_esq": {
        "interior": (200, 0,   0),     # vermelho vivo
        "borda":    (20,  20,  20)
    },

    "gem_ombro_dir": {
        "interior": (200, 0,   0),
        "borda":    (20,  20,  20)
    },

    "asa_esq": {
        "interior": (140, 0,   0),     # vermelho-borgonha
        "borda":    (40,  40,  40)
    },

    "asa_dir": {
        "interior": (140, 0,   0),
        "borda":    (40,  40,  40)
    },

    "canhao_esq": {
        "interior": (120, 118, 115),
        "borda":    (80,  0,   0)
    },

    "canhao_dir": {
        "interior": (120, 118, 115),
        "borda":    (80,  0,   0)
    },

    "gem_canhao_esq": {
        "interior": (200, 0,   0),
        "borda":    (20,  20,  20)
    },

    "gem_canhao_dir": {
        "interior": (200, 0,   0),
        "borda":    (20,  20,  20)
    },

    "ponta_canhao_esq": {
        "interior": (160, 158, 155),
        "borda":    (50,  50,  50)
    },

    "ponta_canhao_dir": {
        "interior": (160, 158, 155),
        "borda":    (50,  50,  50)
    },

    "gem_topo_canhao_esq": {
        "interior": (200, 0,   0),
        "borda":    (20,  20,  20)
    },

    "gem_topo_canhao_dir": {
        "interior": (200, 0,   0),
        "borda":    (20,  20,  20)
    },

    "spikes_topo": {
        "interior": (200, 160, 0),     # dourado
        "borda":    (80,  60,  0)
    },

    "spikes_laterais_esq": {
        "interior": (200, 160, 0),
        "borda":    (80,  60,  0)
    },

    "spikes_laterais_dir": {
        "interior": (200, 160, 0),
        "borda":    (80,  60,  0)
    },

    "spikes_inf_esq": {
        "interior": (200, 160, 0),
        "borda":    (80,  60,  0)
    },

    "spikes_inf_dir": {
        "interior": (200, 160, 0),
        "borda":    (80,  60,  0)
    },

    "gem_apex": {
        "interior": (220, 185, 0),     # amarelo-ouro brilhante
        "borda":    (255, 255, 255)
    },

    "cintura": {
        "interior": (120, 118, 115),
        "borda":    (80,  0,   0)
    },

    "gem_cintura": {
        "interior": (200, 0,   0),
        "borda":    (40,  40,  40)
    },

    "propulsor_central": {
        "interior": (136, 136, 132),
        "borda":    (80,  0,   0)
    },

    "chama_central_esq": {
        "interior": (200, 160, 0),     # dourado-laranja
        "borda":    (0,   0,   0)
    },

    "chama_central_meio": {
        "interior": (220, 80,  0),     # laranja mais quente
        "borda":    (0,   0,   0)
    },

    "chama_central_dir": {
        "interior": (200, 160, 0),
        "borda":    (0,   0,   0)
    },

    "propulsor_esq_a": {
        "interior": (136, 136, 132),
        "borda":    (80,  0,   0)
    },

    "propulsor_esq_b": {
        "interior": (136, 136, 132),
        "borda":    (80,  0,   0)
    },

    "propulsor_dir_a": {
        "interior": (136, 136, 132),
        "borda":    (80,  0,   0)
    },

    "propulsor_dir_b": {
        "interior": (136, 136, 132),
        "borda":    (80,  0,   0)
    },

    "chama_propulsor_esq_a": {
        "interior": (200, 160, 0),
        "borda":    (0,   0,   0)
    },

    "chama_propulsor_esq_b": {
        "interior": (200, 160, 0),
        "borda":    (0,   0,   0)
    },

    "chama_propulsor_dir_a": {
        "interior": (200, 160, 0),
        "borda":    (0,   0,   0)
    },

    "chama_propulsor_dir_b": {
        "interior": (200, 160, 0),
        "borda":    (0,   0,   0)
    },
}

#---------------- v4
boss4_partes = {

    # =========================
    # NÚCLEO CENTRAL
    # =========================

    "corpo_central": [
        [
            (-120, -170),
            (-190, -40),
            (-170, 120),
            (-80, 220),
            (80, 220),
            (170, 120),
            (190, -40),
            (120, -170)
        ],
        "polygon"
    ],

    "placa_central_superior": [
        [
            (-70, -120),
            (70, -120),
            (90, -40),
            (-90, -40)
        ],
        "polygon"
    ],

    "placa_central_inferior": [
        [
            (-90, 80),
            (90, 80),
            (120, 170),
            (-120, 170)
        ],
        "polygon"
    ],

    # =========================
    # OLHO GIGANTE
    # =========================

    "olho_externo": [
        {
            "centro": (0, 0),
            "raio": 65
        },
        "circle"
    ],

    "olho_intermediario": [
        {
            "centro": (0, 0),
            "raio": 42
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

    "pupila": [
        [
            (0, -45),
            (-14, 0),
            (0, 45),
            (14, 0)
        ],
        "polygon"
    ],

    # =========================
    # COROA SUPERIOR
    # =========================

    "torre_topo": [
        [
            (-40, -240),
            (40, -240),
            (65, -160),
            (-65, -160)
        ],
        "polygon"
    ],

    "espinho_topo_centro": [
        [
            (0, -330),
            (-45, -240),
            (45, -240)
        ],
        "polygon"
    ],

    "espinho_topo_esq_1": [
        [
            (-120, -250),
            (-150, -180),
            (-90, -180)
        ],
        "polygon"
    ],

    "espinho_topo_esq_2": [
        [
            (-200, -190),
            (-225, -130),
            (-175, -130)
        ],
        "polygon"
    ],

    "espinho_topo_dir_1": [
        [
            (120, -250),
            (150, -180),
            (90, -180)
        ],
        "polygon"
    ],

    "espinho_topo_dir_2": [
        [
            (200, -190),
            (225, -130),
            (175, -130)
        ],
        "polygon"
    ],

    # =========================
    # ASAS SUPERIORES
    # =========================

    "asa_esq_superior": [
        [
            (-180, -20),
            (-420, -120),
            (-330, 40)
        ],
        "polygon"
    ],

    "asa_esq_interna": [
        [
            (-140, 20),
            (-280, 100),
            (-170, 120)
        ],
        "polygon"
    ],

    "asa_dir_superior": [
        [
            (180, -20),
            (420, -120),
            (330, 40)
        ],
        "polygon"
    ],

    "asa_dir_interna": [
        [
            (140, 20),
            (280, 100),
            (170, 120)
        ],
        "polygon"
    ],

    # =========================
    # CANHÕES GIGANTES
    # =========================

    "canhao_esq_externo": [
        {
            "centro": (-390, 10),
            "raio": 75
        },
        "circle"
    ],

    "canhao_esq_interno": [
        {
            "centro": (-390, 10),
            "raio": 42
        },
        "circle"
    ],

    "canhao_esq_miolo": [
        {
            "centro": (-390, 10),
            "raio": 18
        },
        "circle"
    ],

    "canhao_dir_externo": [
        {
            "centro": (390, 10),
            "raio": 75
        },
        "circle"
    ],

    "canhao_dir_interno": [
        {
            "centro": (390, 10),
            "raio": 42
        },
        "circle"
    ],

    "canhao_dir_miolo": [
        {
            "centro": (390, 10),
            "raio": 18
        },
        "circle"
    ],

    # =========================
    # SATÉLITES FLUTUANTES
    # =========================

    "orbita_esq": [
        {
            "centro": (-250, -170),
            "raio": 35
        },
        "circle"
    ],

    "orbita_dir": [
        {
            "centro": (250, -170),
            "raio": 35
        },
        "circle"
    ],

    "orbita_esq_miolo": [
        {
            "centro": (-250, -170),
            "raio": 12
        },
        "circle"
    ],

    "orbita_dir_miolo": [
        {
            "centro": (250, -170),
            "raio": 12
        },
        "circle"
    ],

    # =========================
    # MANDÍBULAS
    # =========================

    "mandibula_esq": [
        [
            (-120, 170),
            (-220, 260),
            (-110, 240)
        ],
        "polygon"
    ],

    "mandibula_dir": [
        [
            (120, 170),
            (220, 260),
            (110, 240)
        ],
        "polygon"
    ],

    # =========================
    # PERNAS MECÂNICAS
    # =========================

    "perna_esq_1": [
        [
            (-120, 220),
            (-170, 360),
            (-110, 340)
        ],
        "polygon"
    ],

    "perna_esq_2": [
        [
            (-40, 220),
            (-70, 390),
            (-10, 350)
        ],
        "polygon"
    ],

    "perna_dir_1": [
        [
            (120, 220),
            (170, 360),
            (110, 340)
        ],
        "polygon"
    ],

    "perna_dir_2": [
        [
            (40, 220),
            (70, 390),
            (10, 350)
        ],
        "polygon"
    ],

    # =========================
    # BROCAS
    # =========================

    "broca_esq": [
        [
            (-145, 360),
            (-190, 450),
            (-100, 450)
        ],
        "polygon"
    ],

    "broca_dir": [
        [
            (145, 360),
            (190, 450),
            (100, 450)
        ],
        "polygon"
    ],

    "broca_central": [
        [
            (0, 390),
            (-55, 520),
            (55, 520)
        ],
        "polygon"
    ],

    # =========================
    # MOTORES
    # =========================

    "motor_esq": [
        [
            (-280, 120),
            (-210, 120),
            (-180, 220),
            (-250, 220)
        ],
        "polygon"
    ],

    "motor_dir": [
        [
            (280, 120),
            (210, 120),
            (180, 220),
            (250, 220)
        ],
        "polygon"
    ],

    "motor_central": [
        [
            (-70, 170),
            (70, 170),
            (100, 290),
            (-100, 290)
        ],
        "polygon"
    ],

    # =========================
    # CHAMAS
    # =========================

    "fogo_motor_esq": [
        [
            (-230, 340),
            (-260, 220),
            (-200, 220)
        ],
        "polygon"
    ],

    "fogo_motor_dir": [
        [
            (230, 340),
            (260, 220),
            (200, 220)
        ],
        "polygon"
    ],

    "fogo_motor_central": [
        [
            (0, 430),
            (-45, 290),
            (45, 290)
        ],
        "polygon"
    ]
}

boss4_cores = {

    # =========================
    # CORPO
    # =========================

    "corpo_central": {
        "interior": (125, 125, 125),
        "borda": (20, 20, 20)
    },

    "placa_central_superior": {
        "interior": (160, 30, 30),
        "borda": (0, 0, 0)
    },

    "placa_central_inferior": {
        "interior": (90, 90, 90),
        "borda": (0, 0, 0)
    },

    # =========================
    # OLHO
    # =========================

    "olho_externo": {
        "interior": (170, 30, 30),
        "borda": (0, 0, 0)
    },

    "olho_intermediario": {
        "interior": (255, 220, 80),
        "borda": (0, 0, 0)
    },

    "olho_interno": {
        "interior": (15, 15, 15),
        "borda": (0, 0, 0)
    },

    "pupila": {
        "interior": (0, 0, 0),
        "borda": (255, 0, 0)
    },

    # =========================
    # COROA
    # =========================

    "torre_topo": {
        "interior": (150, 150, 150),
        "borda": (0, 0, 0)
    },

    "espinho_topo_centro": {
        "interior": (255, 210, 70),
        "borda": (0, 0, 0)
    },

    "espinho_topo_esq_1": {
        "interior": (255, 210, 70),
        "borda": (0, 0, 0)
    },

    "espinho_topo_esq_2": {
        "interior": (255, 210, 70),
        "borda": (0, 0, 0)
    },

    "espinho_topo_dir_1": {
        "interior": (255, 210, 70),
        "borda": (0, 0, 0)
    },

    "espinho_topo_dir_2": {
        "interior": (255, 210, 70),
        "borda": (0, 0, 0)
    },

    # =========================
    # ASAS
    # =========================

    "asa_esq_superior": {
        "interior": (170, 20, 20),
        "borda": (0, 0, 0)
    },

    "asa_esq_interna": {
        "interior": (110, 110, 110),
        "borda": (0, 0, 0)
    },

    "asa_dir_superior": {
        "interior": (170, 20, 20),
        "borda": (0, 0, 0)
    },

    "asa_dir_interna": {
        "interior": (110, 110, 110),
        "borda": (0, 0, 0)
    },

    # =========================
    # CANHÕES
    # =========================

    "canhao_esq_externo": {
        "interior": (220, 220, 220),
        "borda": (0, 0, 0)
    },

    "canhao_esq_interno": {
        "interior": (150, 0, 0),
        "borda": (0, 0, 0)
    },

    "canhao_esq_miolo": {
        "interior": (255, 70, 70),
        "borda": (0, 0, 0)
    },

    "canhao_dir_externo": {
        "interior": (220, 220, 220),
        "borda": (0, 0, 0)
    },

    "canhao_dir_interno": {
        "interior": (150, 0, 0),
        "borda": (0, 0, 0)
    },

    "canhao_dir_miolo": {
        "interior": (255, 70, 70),
        "borda": (0, 0, 0)
    },

    # =========================
    # ÓRBITAS
    # =========================

    "orbita_esq": {
        "interior": (230, 230, 230),
        "borda": (0, 0, 0)
    },

    "orbita_dir": {
        "interior": (230, 230, 230),
        "borda": (0, 0, 0)
    },

    "orbita_esq_miolo": {
        "interior": (255, 40, 40),
        "borda": (0, 0, 0)
    },

    "orbita_dir_miolo": {
        "interior": (255, 40, 40),
        "borda": (0, 0, 0)
    },

    # =========================
    # MANDÍBULAS
    # =========================

    "mandibula_esq": {
        "interior": (150, 150, 150),
        "borda": (0, 0, 0)
    },

    "mandibula_dir": {
        "interior": (150, 150, 150),
        "borda": (0, 0, 0)
    },

    # =========================
    # PERNAS
    # =========================

    "perna_esq_1": {
        "interior": (90, 90, 90),
        "borda": (0, 0, 0)
    },

    "perna_esq_2": {
        "interior": (90, 90, 90),
        "borda": (0, 0, 0)
    },

    "perna_dir_1": {
        "interior": (90, 90, 90),
        "borda": (0, 0, 0)
    },

    "perna_dir_2": {
        "interior": (90, 90, 90),
        "borda": (0, 0, 0)
    },

    # =========================
    # BROCAS
    # =========================

    "broca_esq": {
        "interior": (255, 180, 40),
        "borda": (0, 0, 0)
    },

    "broca_dir": {
        "interior": (255, 180, 40),
        "borda": (0, 0, 0)
    },

    "broca_central": {
        "interior": (255, 230, 100),
        "borda": (0, 0, 0)
    },

    # =========================
    # MOTORES
    # =========================

    "motor_esq": {
        "interior": (160, 20, 20),
        "borda": (0, 0, 0)
    },

    "motor_dir": {
        "interior": (160, 20, 20),
        "borda": (0, 0, 0)
    },

    "motor_central": {
        "interior": (190, 30, 30),
        "borda": (0, 0, 0)
    },

    # =========================
    # FOGO
    # =========================

    "fogo_motor_esq": {
        "interior": (255, 120, 0),
        "borda": (255, 220, 120)
    },

    "fogo_motor_dir": {
        "interior": (255, 120, 0),
        "borda": (255, 220, 120)
    },

    "fogo_motor_central": {
        "interior": (255, 170, 0),
        "borda": (255, 255, 120)
    }
}

#----------------- v5

boss5_partes = {

    # =================================
    # CORPO CENTRAL
    # =================================

    "corpo_central": [
        [
            (-120, -90),
            (-180, -20),
            (-170, 60),
            (-80, 110),
            (80, 110),
            (170, 60),
            (180, -20),
            (120, -90)
        ],
        "polygon"
    ],

    "placa_topo": [
        [
            (-60, -140),
            (60, -140),
            (90, -80),
            (-90, -80)
        ],
        "polygon"
    ],

    "placa_inferior": [
        [
            (-90, 50),
            (90, 50),
            (120, 120),
            (-120, 120)
        ],
        "polygon"
    ],

    # =================================
    # OLHO CENTRAL
    # =================================

    "olho_externo": [
        {
            "centro": (0, 0),
            "raio": 40
        },
        "circle"
    ],

    "olho_intermediario": [
        {
            "centro": (0, 0),
            "raio": 26
        },
        "circle"
    ],

    "pupila": [
        [
            (0, -30),
            (-10, 0),
            (0, 30),
            (10, 0)
        ],
        "polygon"
    ],

    # =================================
    # ESPINHOS SUPERIORES
    # =================================

    "espinho_topo_centro": [
        [
            (0, -220),
            (-35, -140),
            (35, -140)
        ],
        "polygon"
    ],

    "espinho_topo_esq": [
        [
            (-130, -170),
            (-155, -110),
            (-105, -110)
        ],
        "polygon"
    ],

    "espinho_topo_dir": [
        [
            (130, -170),
            (155, -110),
            (105, -110)
        ],
        "polygon"
    ],

    # =================================
    # ASAS EXTERNAS
    # =================================

    "asa_esq_externa": [
        [
            (-180, -20),
            (-520, -60),
            (-410, 20)
        ],
        "polygon"
    ],

    "asa_esq_interna": [
        [
            (-120, 10),
            (-320, 60),
            (-180, 70)
        ],
        "polygon"
    ],

    "asa_dir_externa": [
        [
            (180, -20),
            (520, -60),
            (410, 20)
        ],
        "polygon"
    ],

    "asa_dir_interna": [
        [
            (120, 10),
            (320, 60),
            (180, 70)
        ],
        "polygon"
    ],

    # =================================
    # CANHÕES GIGANTES
    # =================================

    "canhao_esq_externo": [
        {
            "centro": (-470, 0),
            "raio": 60
        },
        "circle"
    ],

    "canhao_esq_interno": [
        {
            "centro": (-470, 0),
            "raio": 35
        },
        "circle"
    ],

    "canhao_esq_miolo": [
        {
            "centro": (-470, 0),
            "raio": 14
        },
        "circle"
    ],

    "canhao_dir_externo": [
        {
            "centro": (470, 0),
            "raio": 60
        },
        "circle"
    ],

    "canhao_dir_interno": [
        {
            "centro": (470, 0),
            "raio": 35
        },
        "circle"
    ],

    "canhao_dir_miolo": [
        {
            "centro": (470, 0),
            "raio": 14
        },
        "circle"
    ],

    # =================================
    # SATÉLITES
    # =================================

    "orbita_esq": [
        {
            "centro": (-250, -120),
            "raio": 24
        },
        "circle"
    ],

    "orbita_esq_miolo": [
        {
            "centro": (-250, -120),
            "raio": 10
        },
        "circle"
    ],

    "orbita_dir": [
        {
            "centro": (250, -120),
            "raio": 24
        },
        "circle"
    ],

    "orbita_dir_miolo": [
        {
            "centro": (250, -120),
            "raio": 10
        },
        "circle"
    ],

    # =================================
    # MANDÍBULAS
    # =================================

    "mandibula_esq": [
        [
            (-120, 100),
            (-230, 150),
            (-130, 145)
        ],
        "polygon"
    ],

    "mandibula_dir": [
        [
            (120, 100),
            (230, 150),
            (130, 145)
        ],
        "polygon"
    ],

    # =================================
    # PERNAS
    # =================================

    "perna_esq_1": [
        [
            (-110, 110),
            (-150, 220),
            (-100, 210)
        ],
        "polygon"
    ],

    "perna_esq_2": [
        [
            (-20, 120),
            (-40, 250),
            (0, 220)
        ],
        "polygon"
    ],

    "perna_dir_1": [
        [
            (110, 110),
            (150, 220),
            (100, 210)
        ],
        "polygon"
    ],

    "perna_dir_2": [
        [
            (20, 120),
            (40, 250),
            (0, 220)
        ],
        "polygon"
    ],

    # =================================
    # BROCAS
    # =================================

    "broca_esq": [
        [
            (-125, 220),
            (-155, 300),
            (-95, 300)
        ],
        "polygon"
    ],

    "broca_dir": [
        [
            (125, 220),
            (155, 300),
            (95, 300)
        ],
        "polygon"
    ],

    "broca_central": [
        [
            (0, 230),
            (-40, 300),
            (40, 300)
        ],
        "polygon"
    ],

    # =================================
    # MOTORES
    # =================================

    "motor_esq": [
        [
            (-320, 50),
            (-250, 50),
            (-220, 110),
            (-290, 110)
        ],
        "polygon"
    ],

    "motor_dir": [
        [
            (320, 50),
            (250, 50),
            (220, 110),
            (290, 110)
        ],
        "polygon"
    ],

    "motor_central": [
        [
            (-60, 110),
            (60, 110),
            (80, 180),
            (-80, 180)
        ],
        "polygon"
    ],

    # =================================
    # CHAMAS
    # =================================

    "fogo_motor_esq": [
        [
            (-255, 200),
            (-280, 110),
            (-230, 110)
        ],
        "polygon"
    ],

    "fogo_motor_dir": [
        [
            (255, 200),
            (280, 110),
            (230, 110)
        ],
        "polygon"
    ],

    "fogo_motor_central": [
        [
            (0, 280),
            (-35, 180),
            (35, 180)
        ],
        "polygon"
    ]
}
boss5_cores = {

    "corpo_central": {
        "interior": (120, 120, 120),
        "borda": (20, 20, 20)
    },

    "placa_topo": {
        "interior": (160, 20, 20),
        "borda": (0, 0, 0)
    },

    "placa_inferior": {
        "interior": (90, 90, 90),
        "borda": (0, 0, 0)
    },

    "olho_externo": {
        "interior": (170, 20, 20),
        "borda": (0, 0, 0)
    },

    "olho_intermediario": {
        "interior": (255, 220, 70),
        "borda": (0, 0, 0)
    },

    "pupila": {
        "interior": (0, 0, 0),
        "borda": (255, 0, 0)
    },

    "espinho_topo_centro": {
        "interior": (255, 220, 70),
        "borda": (0, 0, 0)
    },

    "espinho_topo_esq": {
        "interior": (255, 220, 70),
        "borda": (0, 0, 0)
    },

    "espinho_topo_dir": {
        "interior": (255, 220, 70),
        "borda": (0, 0, 0)
    },

    "asa_esq_externa": {
        "interior": (170, 20, 20),
        "borda": (0, 0, 0)
    },

    "asa_esq_interna": {
        "interior": (100, 100, 100),
        "borda": (0, 0, 0)
    },

    "asa_dir_externa": {
        "interior": (170, 20, 20),
        "borda": (0, 0, 0)
    },

    "asa_dir_interna": {
        "interior": (100, 100, 100),
        "borda": (0, 0, 0)
    },

    "canhao_esq_externo": {
        "interior": (220, 220, 220),
        "borda": (0, 0, 0)
    },

    "canhao_esq_interno": {
        "interior": (150, 0, 0),
        "borda": (0, 0, 0)
    },

    "canhao_esq_miolo": {
        "interior": (255, 50, 50),
        "borda": (0, 0, 0)
    },

    "canhao_dir_externo": {
        "interior": (220, 220, 220),
        "borda": (0, 0, 0)
    },

    "canhao_dir_interno": {
        "interior": (150, 0, 0),
        "borda": (0, 0, 0)
    },

    "canhao_dir_miolo": {
        "interior": (255, 50, 50),
        "borda": (0, 0, 0)
    },

    "orbita_esq": {
        "interior": (230, 230, 230),
        "borda": (0, 0, 0)
    },

    "orbita_esq_miolo": {
        "interior": (255, 50, 50),
        "borda": (0, 0, 0)
    },

    "orbita_dir": {
        "interior": (230, 230, 230),
        "borda": (0, 0, 0)
    },

    "orbita_dir_miolo": {
        "interior": (255, 50, 50),
        "borda": (0, 0, 0)
    },

    "mandibula_esq": {
        "interior": (140, 140, 140),
        "borda": (0, 0, 0)
    },

    "mandibula_dir": {
        "interior": (140, 140, 140),
        "borda": (0, 0, 0)
    },

    "perna_esq_1": {
        "interior": (90, 90, 90),
        "borda": (0, 0, 0)
    },

    "perna_esq_2": {
        "interior": (90, 90, 90),
        "borda": (0, 0, 0)
    },

    "perna_dir_1": {
        "interior": (90, 90, 90),
        "borda": (0, 0, 0)
    },

    "perna_dir_2": {
        "interior": (90, 90, 90),
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

    "broca_central": {
        "interior": (255, 220, 80),
        "borda": (0, 0, 0)
    },

    "motor_esq": {
        "interior": (170, 20, 20),
        "borda": (0, 0, 0)
    },

    "motor_dir": {
        "interior": (170, 20, 20),
        "borda": (0, 0, 0)
    },

    "motor_central": {
        "interior": (190, 30, 30),
        "borda": (0, 0, 0)
    },

    "fogo_motor_esq": {
        "interior": (255, 120, 0),
        "borda": (255, 220, 120)
    },

    "fogo_motor_dir": {
        "interior": (255, 120, 0),
        "borda": (255, 220, 120)
    },

    "fogo_motor_central": {
        "interior": (255, 170, 0),
        "borda": (255, 255, 120)
    }
}


#--------------v6

boss6_partes = {

    # =====================================
    # CABEÇA CENTRAL
    # =====================================

    "cabeca": [
        [
            (-140, -80),
            (-220, 0),
            (-180, 100),
            (-60, 150),
            (60, 150),
            (180, 100),
            (220, 0),
            (140, -80),
            (0, -140)
        ],
        "polygon"
    ],

    # =====================================
    # OLHO PRINCIPAL
    # =====================================

    "olho_externo": [
        {
            "centro": (0, 10),
            "raio": 75
        },
        "circle"
    ],

    "olho_meio": [
        {
            "centro": (0, 10),
            "raio": 45
        },
        "circle"
    ],

    "olho_pupila": [
        [
            (0, -40),
            (-18, 10),
            (0, 60),
            (18, 10)
        ],
        "polygon"
    ],

    # =====================================
    # DENTES
    # =====================================

    "dente_1": [
        [
            (-100, 140),
            (-80, 190),
            (-60, 140)
        ],
        "polygon"
    ],

    "dente_2": [
        [
            (-50, 145),
            (-25, 210),
            (0, 145)
        ],
        "polygon"
    ],

    "dente_3": [
        [
            (0, 145),
            (25, 210),
            (50, 145)
        ],
        "polygon"
    ],

    "dente_4": [
        [
            (60, 140),
            (80, 190),
            (100, 140)
        ],
        "polygon"
    ],

    # =====================================
    # CHIFRES
    # =====================================

    "chifre_esq": [
        [
            (-120, -90),
            (-260, -180),
            (-180, -40)
        ],
        "polygon"
    ],

    "chifre_dir": [
        [
            (120, -90),
            (260, -180),
            (180, -40)
        ],
        "polygon"
    ],

    # =====================================
    # ASAS ORGÂNICAS
    # =====================================

    "asa_esq": [
        [
            (-180, -10),
            (-520, -80),
            (-470, 40),
            (-300, 90)
        ],
        "polygon"
    ],

    "asa_dir": [
        [
            (180, -10),
            (520, -80),
            (470, 40),
            (300, 90)
        ],
        "polygon"
    ],

    # =====================================
    # OLHOS SECUNDÁRIOS
    # =====================================

    "olho_esq_1": [
        {
            "centro": (-260, 40),
            "raio": 28
        },
        "circle"
    ],

    "olho_esq_2": [
        {
            "centro": (-340, 10),
            "raio": 22
        },
        "circle"
    ],

    "olho_dir_1": [
        {
            "centro": (260, 40),
            "raio": 28
        },
        "circle"
    ],

    "olho_dir_2": [
        {
            "centro": (340, 10),
            "raio": 22
        },
        "circle"
    ],

    # =====================================
    # TENTÁCULOS
    # =====================================

    "tentaculo_esq_1": [
        [
            (-140, 140),
            (-220, 210),
            (-180, 260),
            (-110, 230)
        ],
        "polygon"
    ],

    "tentaculo_esq_2": [
        [
            (-40, 150),
            (-90, 250),
            (-40, 300),
            (0, 240)
        ],
        "polygon"
    ],

    "tentaculo_dir_1": [
        [
            (140, 140),
            (220, 210),
            (180, 260),
            (110, 230)
        ],
        "polygon"
    ],

    "tentaculo_dir_2": [
        [
            (40, 150),
            (90, 250),
            (40, 300),
            (0, 240)
        ],
        "polygon"
    ],

    # =====================================
    # GARRAS ÓSSEAS
    # =====================================

    "garra_esq": [
        [
            (-420, 20),
            (-520, 90),
            (-470, 120)
        ],
        "polygon"
    ],

    "garra_dir": [
        [
            (420, 20),
            (520, 90),
            (470, 120)
        ],
        "polygon"
    ],

    # =====================================
    # ESPINHOS
    # =====================================

    "espinho_topo_1": [
        [
            (-60, -130),
            (-30, -190),
            (0, -130)
        ],
        "polygon"
    ],

    "espinho_topo_2": [
        [
            (0, -140),
            (30, -220),
            (60, -140)
        ],
        "polygon"
    ],

    "espinho_topo_3": [
        [
            (60, -130),
            (90, -190),
            (120, -130)
        ],
        "polygon"
    ]
}

boss6_cores = {

    "cabeca": {
        "interior": (70, 60, 85),
        "borda": (15, 10, 20)
    },

    "olho_externo": {
        "interior": (210, 40, 50),
        "borda": (0, 0, 0)
    },

    "olho_meio": {
        "interior": (255, 230, 120),
        "borda": (0, 0, 0)
    },

    "olho_pupila": {
        "interior": (0, 0, 0),
        "borda": (255, 0, 0)
    },

    "dente_1": {
        "interior": (230, 220, 180),
        "borda": (40, 30, 20)
    },

    "dente_2": {
        "interior": (230, 220, 180),
        "borda": (40, 30, 20)
    },

    "dente_3": {
        "interior": (230, 220, 180),
        "borda": (40, 30, 20)
    },

    "dente_4": {
        "interior": (230, 220, 180),
        "borda": (40, 30, 20)
    },

    "chifre_esq": {
        "interior": (90, 85, 70),
        "borda": (20, 20, 20)
    },

    "chifre_dir": {
        "interior": (90, 85, 70),
        "borda": (20, 20, 20)
    },

    "asa_esq": {
        "interior": (50, 40, 70),
        "borda": (10, 10, 10)
    },

    "asa_dir": {
        "interior": (50, 40, 70),
        "borda": (10, 10, 10)
    },

    "olho_esq_1": {
        "interior": (255, 80, 80),
        "borda": (0, 0, 0)
    },

    "olho_esq_2": {
        "interior": (255, 80, 80),
        "borda": (0, 0, 0)
    },

    "olho_dir_1": {
        "interior": (255, 80, 80),
        "borda": (0, 0, 0)
    },

    "olho_dir_2": {
        "interior": (255, 80, 80),
        "borda": (0, 0, 0)
    },

    "tentaculo_esq_1": {
        "interior": (85, 70, 110),
        "borda": (15, 10, 20)
    },

    "tentaculo_esq_2": {
        "interior": (85, 70, 110),
        "borda": (15, 10, 20)
    },

    "tentaculo_dir_1": {
        "interior": (85, 70, 110),
        "borda": (15, 10, 20)
    },

    "tentaculo_dir_2": {
        "interior": (85, 70, 110),
        "borda": (15, 10, 20)
    },

    "garra_esq": {
        "interior": (120, 100, 140),
        "borda": (20, 20, 20)
    },

    "garra_dir": {
        "interior": (120, 100, 140),
        "borda": (20, 20, 20)
    },

    "espinho_topo_1": {
        "interior": (160, 150, 120),
        "borda": (20, 20, 20)
    },

    "espinho_topo_2": {
        "interior": (160, 150, 120),
        "borda": (20, 20, 20)
    },

    "espinho_topo_3": {
        "interior": (160, 150, 120),
        "borda": (20, 20, 20)
    }
}

#---------- v7
boss7_partes = {

    # =====================================
    # CABEÇA / CRÂNIO
    # =====================================

    "cranio": [
        [
            (0, -260),
            (-90, -220),
            (-150, -120),
            (-170, 20),
            (-120, 120),
            (-40, 180),
            (40, 180),
            (120, 120),
            (170, 20),
            (150, -120),
            (90, -220)
        ],
        "polygon"
    ],

    # =====================================
    # OLHOS
    # =====================================

    "olho_esq": [
        {
            "centro": (-45, -70),
            "raio": 18
        },
        "circle"
    ],

    "olho_dir": [
        {
            "centro": (45, -70),
            "raio": 18
        },
        "circle"
    ],

    "brilho_olho_esq": [
        {
            "centro": (-45, -70),
            "raio": 8
        },
        "circle"
    ],

    "brilho_olho_dir": [
        {
            "centro": (45, -70),
            "raio": 8
        },
        "circle"
    ],

    # =====================================
    # TENTÁCULOS CENTRAIS
    # =====================================

    "tentaculo_central_1": [
        [
            (-30, 40),
            (-70, 140),
            (-40, 300),
            (0, 240)
        ],
        "polygon"
    ],

    "tentaculo_central_2": [
        [
            (30, 40),
            (70, 140),
            (40, 300),
            (0, 240)
        ],
        "polygon"
    ],

    "tentaculo_central_3": [
        [
            (-80, 30),
            (-140, 120),
            (-120, 260),
            (-40, 210)
        ],
        "polygon"
    ],

    "tentaculo_central_4": [
        [
            (80, 30),
            (140, 120),
            (120, 260),
            (40, 210)
        ],
        "polygon"
    ],

    # =====================================
    # TENTÁCULOS LATERAIS
    # =====================================

    "tentaculo_esq_1": [
        [
            (-120, 20),
            (-220, 90),
            (-260, 210),
            (-180, 180)
        ],
        "polygon"
    ],

    "tentaculo_esq_2": [
        [
            (-140, 60),
            (-300, 130),
            (-340, 260),
            (-220, 220)
        ],
        "polygon"
    ],

    "tentaculo_dir_1": [
        [
            (120, 20),
            (220, 90),
            (260, 210),
            (180, 180)
        ],
        "polygon"
    ],

    "tentaculo_dir_2": [
        [
            (140, 60),
            (300, 130),
            (340, 260),
            (220, 220)
        ],
        "polygon"
    ],

    # =====================================
    # ASAS
    # =====================================

    "asa_esq_superior": [
        [
            (-120, -120),
            (-340, -260),
            (-260, -40)
        ],
        "polygon"
    ],

    "asa_esq_inferior": [
        [
            (-140, -20),
            (-320, 60),
            (-240, 120)
        ],
        "polygon"
    ],

    "asa_dir_superior": [
        [
            (120, -120),
            (340, -260),
            (260, -40)
        ],
        "polygon"
    ],

    "asa_dir_inferior": [
        [
            (140, -20),
            (320, 60),
            (240, 120)
        ],
        "polygon"
    ],

    # =====================================
    # GARRAS / ESPINHOS
    # =====================================

    "garra_esq": [
        [
            (-160, -180),
            (-230, -250),
            (-190, -120)
        ],
        "polygon"
    ],

    "garra_dir": [
        [
            (160, -180),
            (230, -250),
            (190, -120)
        ],
        "polygon"
    ],

    "espinho_topo": [
        [
            (0, -340),
            (-40, -250),
            (40, -250)
        ],
        "polygon"
    ],

    # =====================================
    # CORPO INFERIOR
    # =====================================

    "corpo_inferior": [
        [
            (-110, 140),
            (-150, 260),
            (-120, 360),
            (-40, 420),
            (40, 420),
            (120, 360),
            (150, 260),
            (110, 140)
        ],
        "polygon"
    ],

    # =====================================
    # MANTO AQUÁTICO
    # =====================================

    "manto_esq": [
        [
            (-80, 180),
            (-180, 340),
            (-100, 420)
        ],
        "polygon"
    ],

    "manto_dir": [
        [
            (80, 180),
            (180, 340),
            (100, 420)
        ],
        "polygon"
    ]
}

boss7_cores = {

    "cranio": {
        "interior": (55, 65, 70),
        "borda": (10, 15, 20)
    },

    "olho_esq": {
        "interior": (20, 220, 120),
        "borda": (0, 0, 0)
    },

    "olho_dir": {
        "interior": (20, 220, 120),
        "borda": (0, 0, 0)
    },

    "brilho_olho_esq": {
        "interior": (170, 255, 220),
        "borda": (0, 0, 0)
    },

    "brilho_olho_dir": {
        "interior": (170, 255, 220),
        "borda": (0, 0, 0)
    },

    "tentaculo_central_1": {
        "interior": (45, 70, 65),
        "borda": (10, 20, 20)
    },

    "tentaculo_central_2": {
        "interior": (45, 70, 65),
        "borda": (10, 20, 20)
    },

    "tentaculo_central_3": {
        "interior": (55, 85, 80),
        "borda": (10, 20, 20)
    },

    "tentaculo_central_4": {
        "interior": (55, 85, 80),
        "borda": (10, 20, 20)
    },

    "tentaculo_esq_1": {
        "interior": (40, 60, 70),
        "borda": (10, 15, 20)
    },

    "tentaculo_esq_2": {
        "interior": (35, 55, 65),
        "borda": (10, 15, 20)
    },

    "tentaculo_dir_1": {
        "interior": (40, 60, 70),
        "borda": (10, 15, 20)
    },

    "tentaculo_dir_2": {
        "interior": (35, 55, 65),
        "borda": (10, 15, 20)
    },

    "asa_esq_superior": {
        "interior": (30, 35, 40),
        "borda": (5, 5, 5)
    },

    "asa_esq_inferior": {
        "interior": (45, 50, 55),
        "borda": (5, 5, 5)
    },

    "asa_dir_superior": {
        "interior": (30, 35, 40),
        "borda": (5, 5, 5)
    },

    "asa_dir_inferior": {
        "interior": (45, 50, 55),
        "borda": (5, 5, 5)
    },

    "garra_esq": {
        "interior": (80, 85, 90),
        "borda": (15, 15, 15)
    },

    "garra_dir": {
        "interior": (80, 85, 90),
        "borda": (15, 15, 15)
    },

    "espinho_topo": {
        "interior": (70, 80, 85),
        "borda": (10, 10, 10)
    },

    "corpo_inferior": {
        "interior": (50, 70, 75),
        "borda": (10, 15, 20)
    },

    "manto_esq": {
        "interior": (65, 90, 100),
        "borda": (15, 20, 25)
    },

    "manto_dir": {
        "interior": (65, 90, 100),
        "borda": (15, 20, 25)
    }
}


#----------- v8
boss8_partes = {

    "cabeca": [
        {
            "centro": (0, -78),
            "raio": 28
        },
        "circle"
    ],

    "topo_cabeca": [
        [(-28, -78), (28, -78), (22, -96), (-22, -96)],
        "polygon"
    ],

    "antena": [
        [(-2, -105), (2, -105), (2, -128), (-2, -128)],
        "polygon"
    ],

    "ponta_antena": [
        {
            "centro": (0, -135),
            "raio": 6
        },
        "circle"
    ],

    "olho": [
        {
            "centro": (0, -78),
            "raio": 14
        },
        "circle"
    ],

    "corpo": [
        {
            "centro": (0, -5),
            "raio": 48
        },
        "circle"
    ],

    "tronco_inf": [
        [(-42, 28), (42, 28), (32, 58), (-32, 58)],
        "polygon"
    ],

    "grelha": [
        [(-12, -8), (12, -8), (12, 16), (-12, 16)],
        "polygon"
    ],

    "grelha_l1": [
        [(-10, -4), (10, -4), (10, -2), (-10, -2)],
        "polygon"
    ],

    "grelha_l2": [
        [(-10, 2), (10, 2), (10, 4), (-10, 4)],
        "polygon"
    ],

    "grelha_l3": [
        [(-10, 8), (10, 8), (10, 10), (-10, 10)],
        "polygon"
    ],

    "luz_sup_esq": [
        [(-32, -20), (-18, -20), (-18, -12), (-32, -12)],
        "polygon"
    ],

    "luz_sup_dir": [
        [(18, -20), (32, -20), (32, -12), (18, -12)],
        "polygon"
    ],

    "luz_inf_esq": [
        [(-32, 10), (-18, 10), (-18, 18), (-32, 18)],
        "polygon"
    ],

    "luz_inf_dir": [
        [(18, 10), (32, 10), (32, 18), (18, 18)],
        "polygon"
    ],

    "ombro_esq": [
        {
            "centro": (-62, -20),
            "raio": 16
        },
        "circle"
    ],

    "ombro_dir": [
        {
            "centro": (62, -20),
            "raio": 16
        },
        "circle"
    ],

    "ombro_esq_int": [
        {
            "centro": (-62, -20),
            "raio": 9
        },
        "circle"
    ],

    "ombro_dir_int": [
        {
            "centro": (62, -20),
            "raio": 9
        },
        "circle"
    ],

    "braco_sup_esq": [
        [(-76, -8), (-58, -2), (-74, 30), (-90, 24)],
        "polygon"
    ],

    "braco_sup_dir": [
        [(58, -2), (76, -8), (90, 24), (74, 30)],
        "polygon"
    ],

    "braco_inf_esq": [
        [(-90, 24), (-74, 30), (-74, 58), (-90, 58)],
        "polygon"
    ],

    "braco_inf_dir": [
        [(74, 30), (90, 24), (90, 58), (74, 58)],
        "polygon"
    ],

    "mao_esq": [
        [(-96, 58), (-78, 58), (-70, 70), (-76, 84),
         (-82, 74), (-90, 74), (-96, 84), (-102, 70)],
        "polygon"
    ],

    "mao_dir": [
        [(78, 58), (96, 58), (102, 70), (96, 84),
         (90, 74), (82, 74), (76, 84), (70, 70)],
        "polygon"
    ],

    "saia": [
        [(-48, 58), (48, 58), (38, 86), (-38, 86)],
        "polygon"
    ],

    "booster_esq": [
        [(-30, 86), (-16, 86), (-20, 108), (-26, 122)],
        "polygon"
    ],

    "booster_centro": [
        [(-8, 86), (8, 86), (12, 112), (0, 136), (-12, 112)],
        "polygon"
    ],

    "booster_dir": [
        [(16, 86), (30, 86), (26, 122), (20, 108)],
        "polygon"
    ]
}

boss8_cores = {

    "cabeca": {
        "interior": (140, 140, 140),
        "borda": (120, 0, 0)
    },

    "topo_cabeca": {
        "interior": (150, 150, 150),
        "borda": (120, 0, 0)
    },

    "antena": {
        "interior": (120, 0, 0),
        "borda": (80, 0, 0)
    },

    "ponta_antena": {
        "interior": (255, 210, 0),
        "borda": (120, 40, 0)
    },

    "olho": {
        "interior": (255, 230, 0),
        "borda": (120, 40, 0)
    },

    "corpo": {
        "interior": (125, 120, 120),
        "borda": (120, 0, 0)
    },

    "tronco_inf": {
        "interior": (120, 115, 115),
        "borda": (120, 0, 0)
    },

    "grelha": {
        "interior": (85, 85, 85),
        "borda": (60, 20, 20)
    },

    "grelha_l1": {
        "interior": (40, 40, 40),
        "borda": (20, 20, 20)
    },

    "grelha_l2": {
        "interior": (40, 40, 40),
        "borda": (20, 20, 20)
    },

    "grelha_l3": {
        "interior": (40, 40, 40),
        "borda": (20, 20, 20)
    },

    "luz_sup_esq": {
        "interior": (255, 220, 40),
        "borda": (120, 40, 0)
    },

    "luz_sup_dir": {
        "interior": (255, 220, 40),
        "borda": (120, 40, 0)
    },

    "luz_inf_esq": {
        "interior": (255, 220, 40),
        "borda": (120, 40, 0)
    },

    "luz_inf_dir": {
        "interior": (255, 220, 40),
        "borda": (120, 40, 0)
    },

    "ombro_esq": {
        "interior": (135, 135, 135),
        "borda": (120, 0, 0)
    },

    "ombro_dir": {
        "interior": (135, 135, 135),
        "borda": (120, 0, 0)
    },

    "ombro_esq_int": {
        "interior": (95, 95, 95),
        "borda": (70, 70, 70)
    },

    "ombro_dir_int": {
        "interior": (95, 95, 95),
        "borda": (70, 70, 70)
    },

    "braco_sup_esq": {
        "interior": (120, 120, 120),
        "borda": (120, 0, 0)
    },

    "braco_sup_dir": {
        "interior": (120, 120, 120),
        "borda": (120, 0, 0)
    },

    "braco_inf_esq": {
        "interior": (120, 120, 120),
        "borda": (120, 0, 0)
    },

    "braco_inf_dir": {
        "interior": (120, 120, 120),
        "borda": (120, 0, 0)
    },

    "mao_esq": {
        "interior": (140, 140, 140),
        "borda": (120, 0, 0)
    },

    "mao_dir": {
        "interior": (140, 140, 140),
        "borda": (120, 0, 0)
    },

    "saia": {
        "interior": (118, 112, 112),
        "borda": (120, 0, 0)
    },

    "booster_esq": {
        "interior": (255, 220, 0),
        "borda": (120, 80, 0)
    },

    "booster_centro": {
        "interior": (255, 220, 0),
        "borda": (120, 80, 0)
    },

    "booster_dir": {
        "interior": (255, 220, 0),
        "borda": (120, 80, 0)
    }
}

#----------- v9
boss9_cores = {

    "cabeca": {
        "interior": (145, 145, 145),
        "borda": (110, 0, 0)
    },

    "viseira": {
        "interior": (120, 120, 120),
        "borda": (110, 0, 0)
    },

    "nariz": {
        "interior": (130, 130, 130),
        "borda": (110, 0, 0)
    },

    "olho": {
        "interior": (255, 180, 0),
        "borda": (120, 50, 0)
    },

    "orelha": {
        "interior": (130, 130, 130),
        "borda": (110, 0, 0)
    },

    "orelha_int": {
        "interior": (90, 90, 90),
        "borda": (60, 60, 60)
    },

    "boca_sup": {
        "interior": (125, 125, 125),
        "borda": (110, 0, 0)
    },

    "boca_inf": {
        "interior": (115, 115, 115),
        "borda": (110, 0, 0)
    },

    "dente1": {
        "interior": (255, 210, 0),
        "borda": (120, 40, 0)
    },

    "dente2": {
        "interior": (255, 210, 0),
        "borda": (120, 40, 0)
    },

    "dente3": {
        "interior": (255, 210, 0),
        "borda": (120, 40, 0)
    },

    "antena_haste": {
        "interior": (120, 0, 0),
        "borda": (80, 0, 0)
    },

    "antena_ponta": {
        "interior": (180, 40, 40),
        "borda": (110, 0, 0)
    },

    "pescoco": {
        "interior": (80, 80, 80),
        "borda": (50, 50, 50)
    },

    "tronco": {
        "interior": (125, 120, 120),
        "borda": (110, 0, 0)
    },

    "painel": {
        "interior": (90, 90, 90),
        "borda": (50, 50, 50)
    },

    "luz1": {
        "interior": (255, 210, 0),
        "borda": (120, 40, 0)
    },

    "luz2": {
        "interior": (255, 210, 0),
        "borda": (120, 40, 0)
    },

    "ombro": {
        "interior": (130, 130, 130),
        "borda": (110, 0, 0)
    },

    "ombro_int": {
        "interior": (100, 100, 100),
        "borda": (60, 60, 60)
    },

    "braco_sup": {
        "interior": (130, 130, 130),
        "borda": (110, 0, 0)
    },

    "cotovelo": {
        "interior": (135, 135, 135),
        "borda": (110, 0, 0)
    },

    "cotovelo_int": {
        "interior": (95, 95, 95),
        "borda": (60, 60, 60)
    },

    "braco_inf": {
        "interior": (120, 120, 120),
        "borda": (110, 0, 0)
    },

    "pulso": {
        "interior": (130, 130, 130),
        "borda": (110, 0, 0)
    },

    "garra": {
        "interior": (145, 145, 145),
        "borda": (110, 0, 0)
    },

    "dedo1": {
        "interior": (150, 150, 150),
        "borda": (110, 0, 0)
    },

    "dedo2": {
        "interior": (150, 150, 150),
        "borda": (110, 0, 0)
    },

    "dedo3": {
        "interior": (150, 150, 150),
        "borda": (110, 0, 0)
    },

    "motor_sup": {
        "interior": (100, 100, 100),
        "borda": (110, 0, 0)
    },

    "motor_meio": {
        "interior": (100, 100, 100),
        "borda": (110, 0, 0)
    },

    "motor_inf": {
        "interior": (100, 100, 100),
        "borda": (110, 0, 0)
    },

    "fogo_sup": {
        "interior": (255, 210, 0),
        "borda": (255, 120, 0)
    },

    "fogo_meio": {
        "interior": (255, 210, 0),
        "borda": (255, 120, 0)
    },

    "fogo_inf": {
        "interior": (255, 210, 0),
        "borda": (255, 120, 0)
    },

    "base_foguete": {
        "interior": (90, 90, 90),
        "borda": (110, 0, 0)
    },

    "fogo_principal": {
        "interior": (255, 220, 0),
        "borda": (255, 130, 0)
    }
}
boss9_partes = {

    "cabeca": [
        [(-20, -230), (70, -200), (70, -120), (-5, -105), (-55, -140)],
        "polygon"
    ],

    "viseira": [
        [(-18, -210), (60, -190), (25, -170), (-35, -180)],
        "polygon"
    ],

    "nariz": [
        [(-52, -175), (-25, -160), (-45, -145), (-70, -150)],
        "polygon"
    ],

    "olho": [
        {
            "centro": (-18, -165),
            "raio": 14
        },
        "circle"
    ],

    "orelha": [
        {
            "centro": (48, -155),
            "raio": 18
        },
        "circle"
    ],

    "orelha_int": [
        {
            "centro": (48, -155),
            "raio": 10
        },
        "circle"
    ],

    "boca_sup": [
        [(-45, -132), (30, -122), (45, -112), (-10, -118)],
        "polygon"
    ],

    "boca_inf": [
        [(-45, -132), (40, -122), (40, -100), (-45, -108)],
        "polygon"
    ],

    "dente1": [
        [(-40, -128), (-26, -128), (-33, -108)],
        "polygon"
    ],

    "dente2": [
        [(-20, -126), (-6, -126), (-13, -106)],
        "polygon"
    ],

    "dente3": [
        [(0, -124), (14, -124), (7, -106)],
        "polygon"
    ],

    "antena_haste": [
        [(-2, -250), (2, -250), (2, -275), (-2, -275)],
        "polygon"
    ],

    "antena_ponta": [
        [(0, -292), (10, -275), (0, -258), (-10, -275)],
        "polygon"
    ],

    "pescoco": [
        [(-10, -100), (45, -92), (35, -75), (-18, -82)],
        "polygon"
    ],

    "tronco": [
        [(-55, -70), (55, -70), (90, 40), (78, 120),
         (-5, 120), (-40, 60), (-55, 0)],
        "polygon"
    ],

    "painel": [
        {
            "centro": (-62, 0),
            "raio": 24
        },
        "circle"
    ],

    "luz1": [
        [(-55, -15), (-35, -15), (-35, -5), (-55, -5)],
        "polygon"
    ],

    "luz2": [
        [(-50, 18), (-30, 18), (-30, 32), (-50, 32)],
        "polygon"
    ],

    "ombro": [
        {
            "centro": (18, -8),
            "raio": 38
        },
        "circle"
    ],

    "ombro_int": [
        {
            "centro": (18, -8),
            "raio": 10
        },
        "circle"
    ],

    "braco_sup": [
        [(-2, 18), (40, 28), (15, 118), (-20, 95)],
        "polygon"
    ],

    "cotovelo": [
        {
            "centro": (-8, 98),
            "raio": 18
        },
        "circle"
    ],

    "cotovelo_int": [
        {
            "centro": (-8, 98),
            "raio": 9
        },
        "circle"
    ],

    "braco_inf": [
        [(-18, 110), (8, 120), (-48, 220), (-72, 208)],
        "polygon"
    ],

    "pulso": [
        [(-78, 208), (-18, 228), (-28, 258), (-88, 240)],
        "polygon"
    ],

    "garra": [
        [(-92, 240), (-25, 258), (-38, 290), (-102, 272)],
        "polygon"
    ],

    "dedo1": [
        [(-96, 272), (-84, 278), (-112, 322)],
        "polygon"
    ],

    "dedo2": [
        [(-72, 270), (-60, 278), (-84, 330)],
        "polygon"
    ],

    "dedo3": [
        [(-48, 266), (-36, 274), (-54, 318)],
        "polygon"
    ],

    "motor_sup": [
        [(72, -82), (120, -72), (122, -10), (76, -18)],
        "polygon"
    ],

    "motor_meio": [
        [(78, -5), (132, 8), (132, 72), (82, 60)],
        "polygon"
    ],

    "motor_inf": [
        [(84, 72), (138, 88), (138, 152), (90, 136)],
        "polygon"
    ],

    "fogo_sup": [
        [(122, -52), (152, -34), (122, -16)],
        "polygon"
    ],

    "fogo_meio": [
        [(132, 24), (164, 44), (132, 62)],
        "polygon"
    ],

    "fogo_inf": [
        [(138, 104), (170, 126), (138, 144)],
        "polygon"
    ],

    "base_foguete": [
        [(-10, 120), (72, 120), (60, 152), (0, 152)],
        "polygon"
    ],

    "fogo_principal": [
        [(10, 152), (52, 152), (64, 192), (32, 250), (0, 192)],
        "polygon"
    ]
}
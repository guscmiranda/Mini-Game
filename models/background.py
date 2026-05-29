bg_atmosfera_cores = {
    # Céu Lavanda Pastel (Bem final de tarde animado)
    "ceu_fundo": {"interior": (225, 215, 235), "borda": (225, 215, 235)},

    # Astro distante (Pêssego/Amarelo bem suave)
    "astro_apagado": {"interior": (255, 245, 200), "borda": (235, 220, 180)},

    # Curvatura da Terra (Um verde menta/teal pastel lindão)
    "terra_curva": {"interior": (140, 190, 185), "borda": (120, 160, 155)},

    # Nuvens distantes (Rosa bebê e Azul bebê)
    "nuvem_longe_esq": {"interior": (255, 220, 225), "borda": (225, 190, 195)},
    "nuvem_longe_dir": {"interior": (220, 240, 255), "borda": (190, 210, 225)},

    # Nuvens médias (Amarelinho creme e Lilás pastel)
    "nuvem_media_esq": {"interior": (250, 250, 230), "borda": (220, 220, 200)},
    "nuvem_media_dir": {"interior": (235, 230, 255), "borda": (205, 200, 225)}
}

bg_atmosfera_partes = {

    # 1. Base do Céu (Cobrindo toda a tela de 1280x720 com folga)
    "ceu_fundo": [
        [(-100, -100), (1380, -100), (1380, 820), (-100, 820)],
        "polygon"
    ],

    # 2. Astro distante (Deslocado para a direita e para o alto)
    "astro_apagado": [
        {
            "centro": (490, 140),
            "raio": 90
        },
        "circle"
    ],

    # 3. Curvatura da Terra (Centro no X=640, mas afundado lá no Y=1960)
    "terra_curva": [
        {
            "centro": (640, 1960),
            "raio": 1300
        },
        "circle"
    ],

    # 4. Nuvem distante 1 (Esquerda - Rosa pastel)
    "nuvem_longe_esq": [
        [(140, 240), (340, 240), (360, 225), (330, 200),
         (290, 185), (240, 180), (190, 195), (150, 210), (130, 225)],
        "polygon"
    ],

    # 5. Nuvem distante 2 (Direita - Azul pastel)
    "nuvem_longe_dir": [
        [(840, 340), (1090, 340), (1110, 320), (1080, 290),
         (1020, 270), (960, 265), (900, 280), (850, 300), (830, 320)],
        "polygon"
    ],

    # 6. Nuvem média 1 (Baixo Esquerda - Creme)
    "nuvem_media_esq": [
        [(40, 560), (390, 560), (420, 530), (380, 490),
         (310, 460), (220, 450), (130, 470), (60, 500), (20, 530)],
        "polygon"
    ],

    # 7. Nuvem média 2 (Baixo Direita - Lilás)
    "nuvem_media_dir": [
        [(1040, 610), (1240, 610), (1260, 590), (1220, 560),
         (1140, 540), (1070, 560), (1020, 590)],
        "polygon"
    ]
}
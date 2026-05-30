heart_cores = {
    "corpo": {
        "interior": (220, 20, 60),  # Vermelho carmesim
        "borda": (139, 0, 0)       # Vermelho escuro para contorno
    },
    "brilho_esq": {
        "interior": (255, 255, 255), # Branco para o reflexo
        "borda": (255, 255, 255)
    },
    "brilho_dir": {
        "interior": (255, 255, 255), # Branco para o reflexo
        "borda": (255, 255, 255)
    }
}

heart_partes = {
    "corpo": [
        [
            (0, -5),   # Topo do corte central
            (-6, -10), # Esquerda superior
            (-10, 0),  # Esquerda média
            (0, 10),   # Ponta inferior
            (10, 0),   # Direita média
            (6, -10)   # Direita superior
        ],
        "polygon"
    ],

    # Adicionando pequenos círculos para suavizar o topo
    "brilho_esq": [
        {
            "centro": (-4, -6),
            "raio": 1
        },
        "circle"
    ],
    "brilho_dir": [
        {
            "centro": (4, -6),
            "raio": 1
        },
        "circle"
    ]
}
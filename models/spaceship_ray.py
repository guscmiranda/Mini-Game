tiro_cores = {

    "corpo": {
        "interior": (80, 180, 255),   # azul claro
        "borda": (20, 80, 200)        # azul escuro
    },

    "nucleo": {
        "interior": (220, 245, 255),  # brilho central
        "borda": (255, 255, 255)
    }
}


tiro_partes = {

    "corpo": [
        [
            (0, -12),   # topo
            (8, 0),     # direita
            (0, 12),    # baixo
            (-8, 0)     # esquerda
        ],
        "polygon"
    ],

    "nucleo": [
        {
            "centro": (0, 0),
            "raio": 3
        },
        "circle"
    ]
}
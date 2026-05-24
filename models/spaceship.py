spaceship_cores = {

            "corpo": {
                "interior": (120, 120, 120),
                "borda": (120, 0, 0)
            },

            "asa_esq": {
                "interior": (180, 0, 20),
                "borda": (0, 0, 0)
            },

            "asa_dir": {
                "interior": (180, 0, 20),
                "borda": (0, 0, 0)
            },

            "motor": {
                "interior": (180, 0, 20),
                "borda": (0, 0, 0)
            },

            "janela": {
                "interior": (150, 240, 255),
                "borda": (120, 0, 0)
            }
        }

spaceship_partes = {

    # asas entrando um pouco no corpo
    "asa_esq": [
        [(-20, 20), (-55, 60), (-10, 60)],
        "polygon"
    ],

    "asa_dir": [
        [(20, 20), (10, 60), (55, 60)],
        "polygon"
    ],


    "motor": [
        [(-7.5, 30), (7.5, 30), (12.5, 47.5), (-12.5, 47.5)],
        "polygon"
    ],

    "corpo": [
        [(0, -50), (-30, 30), (30, 30)],
        "polygon"
    ],

    "janela": [
        {
            "centro": (0, -3),
            "raio": 11
        },
        "circle"
    ]
}






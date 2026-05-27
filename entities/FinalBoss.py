from entities.Entity import Entity
import copy
import math

class FinalBoss(Entity):

    def __init__(self, partes, cores, centro=(0,0), partes_criticas=[]):

        super().__init__(
            copy.deepcopy(partes),
            copy.deepcopy(cores),
            centro,
            partes_criticas
        )

        self.vida = 200

        self.velocidade = 100

        self.alive = True

        # começa fora da tela
        self.mover(1600, 300)

        # timers
        self.attack_timer = 0
        self.move_timer = 0

        # estados
        self.entering = True

        # direção vertical
        self.vertical_direction = 1

    def entrada(self, dt):

        alvo_x = 1000

        if self.cx > alvo_x:

            self.mover(
                -(self.velocidade-40) * dt,
                0
            )

        else:
            self.entering = False

    def movimento_fantasma(self, dt):

        velocidade_y = 120

        self.mover(
            0,
            velocidade_y *
            self.vertical_direction *
            dt
        )

        # temos que mudar esses valores !!!
        if self.cy > 550:
            self.vertical_direction = -1

        elif self.cy < 180:
            self.vertical_direction = 1


    def olhar_para_player(self, player):

        # =========================
        # OLHO
        # =========================

        olho_base = (-18, -165)

        olho = self.partes["olho"][0]["centro"]

        dx = player.cx - olho[0]
        dy = player.cy - olho[1]

        distancia = math.sqrt(dx ** 2 + dy ** 2)

        if distancia != 0:
            dx /= distancia
            dy /= distancia

        # pequeno movimento só pra "olhar"
        offset_olho = 4

        self.partes["olho"][0]["centro"] = (
            self.cx + olho_base[0] + dx * offset_olho,
            self.cy + olho_base[1] + dy * offset_olho
        )

        # =========================
        # BRAÇO / GARRA
        # =========================

        ombro = self.partes["ombro"][0]["centro"]

        dx_braco = player.cx - ombro[0]
        dy_braco = player.cy - ombro[1]

        angulo = math.atan2(dy_braco, dx_braco)

        comprimento_sup = 95
        comprimento_inf = 120

        # cotovelo
        cotovelo_x = ombro[0] + math.cos(angulo) * comprimento_sup
        cotovelo_y = ombro[1] + math.sin(angulo) * comprimento_sup

        # mão
        mao_x = cotovelo_x + math.cos(angulo) * comprimento_inf
        mao_y = cotovelo_y + math.sin(angulo) * comprimento_inf

        self.partes["cotovelo"][0]["centro"] = (
            cotovelo_x,
            cotovelo_y
        )

        self.partes["cotovelo_int"][0]["centro"] = (
            cotovelo_x,
            cotovelo_y
        )

        largura_sup = 22
        largura_inf = 18

        perp_x = -math.sin(angulo)
        perp_y = math.cos(angulo)

        # =========================
        # BRAÇO SUPERIOR
        # =========================

        self.partes["braco_sup"][0] = [

            (
                ombro[0] + perp_x * largura_sup,
                ombro[1] + perp_y * largura_sup
            ),

            (
                ombro[0] - perp_x * largura_sup,
                ombro[1] - perp_y * largura_sup
            ),

            (
                cotovelo_x - perp_x * largura_sup,
                cotovelo_y - perp_y * largura_sup
            ),

            (
                cotovelo_x + perp_x * largura_sup,
                cotovelo_y + perp_y * largura_sup
            )
        ]

        # =========================
        # BRAÇO INFERIOR
        # =========================

        self.partes["braco_inf"][0] = [

            (
                cotovelo_x + perp_x * largura_inf,
                cotovelo_y + perp_y * largura_inf
            ),

            (
                cotovelo_x - perp_x * largura_inf,
                cotovelo_y - perp_y * largura_inf
            ),

            (
                mao_x - perp_x * largura_inf,
                mao_y - perp_y * largura_inf
            ),

            (
                mao_x + perp_x * largura_inf,
                mao_y + perp_y * largura_inf
            )
        ]

        # =========================
        # PULSO
        # =========================

        pulso_largura = 28

        self.partes["pulso"][0] = [

            (
                mao_x + perp_x * pulso_largura,
                mao_y + perp_y * pulso_largura
            ),

            (
                mao_x - perp_x * pulso_largura,
                mao_y - perp_y * pulso_largura
            ),

            (
                mao_x - perp_x * pulso_largura
                + math.cos(angulo) * 26,

                mao_y - perp_y * pulso_largura
                + math.sin(angulo) * 26
            ),

            (
                mao_x + perp_x * pulso_largura
                + math.cos(angulo) * 26,

                mao_y + perp_y * pulso_largura
                + math.sin(angulo) * 26
            )
        ]

        # =========================
        # GARRA
        # =========================

        garra_x = mao_x + math.cos(angulo) * 42
        garra_y = mao_y + math.sin(angulo) * 42

        largura_garra = 36

        self.partes["garra"][0] = [

            (
                mao_x + perp_x * largura_garra,
                mao_y + perp_y * largura_garra
            ),

            (
                mao_x - perp_x * largura_garra,
                mao_y - perp_y * largura_garra
            ),

            (
                garra_x - perp_x * largura_garra,
                garra_y - perp_y * largura_garra
            ),

            (
                garra_x + perp_x * largura_garra,
                garra_y + perp_y * largura_garra
            )
        ]

        # =========================
        # DEDOS
        # =========================

        distancia_dedos = 26
        tamanho_dedo = 55

        bases = [
            -24,
            0,
            24
        ]

        dedos = ["dedo1", "dedo2", "dedo3"]

        for i, offset in enumerate(bases):
            base_x = (
                    garra_x
                    + perp_x * offset
            )

            base_y = (
                    garra_y
                    + perp_y * offset
            )

            ponta_x = (
                    base_x
                    + math.cos(angulo) * tamanho_dedo
            )

            ponta_y = (
                    base_y
                    + math.sin(angulo) * tamanho_dedo
            )

            largura = 10

            self.partes[dedos[i]][0] = [

                (
                    base_x + perp_x * largura,
                    base_y + perp_y * largura
                ),

                (
                    base_x - perp_x * largura,
                    base_y - perp_y * largura
                ),

                (
                    ponta_x,
                    ponta_y
                )
            ]

    def update(self, dt, player):

        if self.entering:

            self.entrada(dt)

        else:

            self.movimento_fantasma(dt)
            self.olhar_para_player(player)
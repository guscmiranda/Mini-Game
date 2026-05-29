# models/parede_laser.py

parede_cores = {}
parede_partes = {}
partes_criticas_parede = []

# Tamanho do buraco (Gap).
# A nave grande não passa, a nave pequena (isBig=False) passa!
GAP_Y = 40
ALTURA_BLOCO = 80
LARGURA_BLOCO = 80

# Margem interna: o bloco da hitbox será 20px menor de cada lado
PADDING_HITBOX = 13

# Gerar 9 blocos para cima e 9 para baixo (suficiente para cobrir a tela)
for i in range(1, 10):
    # Nomes das partes VISUAIS (maiores)
    nome_sup = f"sup_{i}"
    nome_inf = f"inf_{i}"

    # Nomes das partes INTERNAS (menores, que serão as hitboxes)
    nome_sup_hit = f"sup_hit_{i}"
    nome_inf_hit = f"inf_hit_{i}"

    # Cores do bloco visual (Borda brilhante)
    parede_cores[nome_sup] = {"interior": (220, 20, 20), "borda": (255, 100, 100)}
    parede_cores[nome_inf] = {"interior": (220, 20, 20), "borda": (255, 100, 100)}

    # Cores do bloco interno (Mesma cor do interior para ficar "invisível" dentro do visual)
    parede_cores[nome_sup_hit] = {"interior": (220, 20, 20), "borda": (220, 20, 20)}
    parede_cores[nome_inf_hit] = {"interior": (220, 20, 20), "borda": (220, 20, 20)}

    # O SEGREDO: Apenas as partes INTERNAS entram na lista de colisão!
    partes_criticas_parede.extend([nome_sup_hit, nome_inf_hit])

    # ==========================================
    # CONSTRUINDO OS BLOCOS SUPERIORES
    # ==========================================
    y_bottom_sup = -GAP_Y - (i - 1) * ALTURA_BLOCO
    y_top_sup = y_bottom_sup - ALTURA_BLOCO

    # 1. Bloco Visual Superior
    parede_partes[nome_sup] = [
        [(-LARGURA_BLOCO / 2, y_bottom_sup), (LARGURA_BLOCO / 2, y_bottom_sup),
         (LARGURA_BLOCO / 2, y_top_sup), (-LARGURA_BLOCO / 2, y_top_sup)],
        "polygon"
    ]

    # 2. Bloco Hitbox Superior (Encolhido pelo PADDING)
    y_bottom_sup_hit = y_bottom_sup - PADDING_HITBOX
    y_top_sup_hit = y_top_sup + PADDING_HITBOX
    x_esq_hit = -LARGURA_BLOCO / 2 + PADDING_HITBOX
    x_dir_hit = LARGURA_BLOCO / 2 - PADDING_HITBOX

    parede_partes[nome_sup_hit] = [
        [(x_esq_hit, y_bottom_sup_hit), (x_dir_hit, y_bottom_sup_hit),
         (x_dir_hit, y_top_sup_hit), (x_esq_hit, y_top_sup_hit)],
        "polygon"
    ]

    # ==========================================
    # CONSTRUINDO OS BLOCOS INFERIORES
    # ==========================================
    y_top_inf = GAP_Y + (i - 1) * ALTURA_BLOCO
    y_bottom_inf = y_top_inf + ALTURA_BLOCO

    # 3. Bloco Visual Inferior
    parede_partes[nome_inf] = [
        [(-LARGURA_BLOCO / 2, y_top_inf), (LARGURA_BLOCO / 2, y_top_inf),
         (LARGURA_BLOCO / 2, y_bottom_inf), (-LARGURA_BLOCO / 2, y_bottom_inf)],
        "polygon"
    ]

    # 4. Bloco Hitbox Inferior (Encolhido pelo PADDING)
    y_top_inf_hit = y_top_inf + PADDING_HITBOX
    y_bottom_inf_hit = y_bottom_inf - PADDING_HITBOX

    parede_partes[nome_inf_hit] = [
        [(x_esq_hit, y_top_inf_hit), (x_dir_hit, y_top_inf_hit),
         (x_dir_hit, y_bottom_inf_hit), (x_esq_hit, y_bottom_inf_hit)],
        "polygon"
    ]
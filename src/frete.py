def calcular_frete(valor_carrinho, regiao=None, cupom=None):
    if valor_carrinho >= 200:
        return 0.0

    frete = 15.0
    if cupom and str(cupom).strip().upper() == "DESCONTO10":
        frete *= 0.9

    return frete

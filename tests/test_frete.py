from src.frete import calcular_frete


def test_frete_padrao():
    assert calcular_frete(150) == 15.0


def test_frete_gratis():
    assert calcular_frete(200) == 0.0
    assert calcular_frete(250) == 0.0


def test_frete_com_cupom_desconto10():
    assert calcular_frete(150, cupom="DESCONTO10") == 13.5


def test_frete_gratis_com_cupom():
    assert calcular_frete(200, cupom="DESCONTO10") == 0.0

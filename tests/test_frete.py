from src.frete import calcular_frete


def test_frete_padrao():
    assert calcular_frete(150) == 15.0
    assert calcular_frete(200) == 15.0


def test_frete_gratis():
    assert calcular_frete(250) == 0.0
    assert calcular_frete(300) == 0.0
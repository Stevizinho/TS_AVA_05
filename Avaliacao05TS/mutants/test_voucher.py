from voucher import validar_voucher;

 # Testes de AVL
def test_validar_voucher_menor50():
    assert validar_voucher(49.99) == False

def test_validar_voucher_igual50():
    assert validar_voucher(50.00) == True

def test_validar_voucher_maior50():
    assert validar_voucher(50.01) == True

def test_validar_voucher_menor500():
    assert validar_voucher(499.99) == True

def test_validar_voucher_igual500():
    assert validar_voucher(500.00) == True

def test_validar_voucher_maior500():
    assert validar_voucher(500.01) == False

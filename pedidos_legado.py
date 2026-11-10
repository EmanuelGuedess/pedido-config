# pedidos_legado.py
# Sistema "legado" de pedidos de uma loja virtual (exemplo didático inédito).
# Aula: Reengenharia e engenharia reversa I (Modelagem e Análise de Sistemas Computacionais)
# ATENÇÃO: o código é propositalmente mal estruturado. Não use como modelo de boas práticas.

import sqlite3

db = sqlite3.connect(":memory:")
c = db.cursor()
c.execute("create table prod (id integer, nome text, preco real, qtd integer)")
c.execute("create table ped (id integer, cli text, tot real, st text)")
c.execute("create table cli (nome text, tipo text, email text)")
c.executemany("insert into prod values (?,?,?,?)", [
    (1, "Teclado", 150.0, 10),
    (2, "Mouse", 80.0, 5),
    (3, "Monitor", 900.0, 2),
])
c.executemany("insert into cli values (?,?,?)", [
    ("Ana", "VIP", "ana@exemplo.com"),
    ("Bruno", "ATC", "bruno@exemplo.com"),
    ("Carla", "NORMAL", "carla@exemplo.com"),
])
db.commit()

n = 0
log = []


def proc(cli, itens, cupom, pg):
    global n
    n = n + 1
    log.append("inicio pedido " + str(n))

    # busca cliente
    c.execute("select * from cli where nome = '" + cli + "'")
    r = c.fetchone()
    if r is None:
        print("ERRO: cliente nao existe")
        log.append("cliente invalido")
        return "CLIENTE_INVALIDO"

    # calcula total e confere estoque
    tot = 0
    for i in itens:
        c.execute("select * from prod where id = " + str(i[0]))
        p = c.fetchone()
        if p is None or p[3] < i[1]:
            print("ERRO: sem estoque do item " + str(i[0]))
            log.append("sem estoque")
            c.execute("insert into ped values (" + str(n) + ", '" + cli + "', 0, 'SEM_ESTOQUE')")
            db.commit()
            return "SEM_ESTOQUE"
        tot = tot + p[2] * i[1]

    # descontos
    if r[1] == "VIP":
        tot = tot - tot * 0.15
    elif r[1] == "ATC":
        if tot > 1000:
            tot = tot - tot * 0.15
    if cupom == "PROMO5":
        tot = tot - tot * 0.05
    elif cupom == "BEMVINDO":
        if tot > 100:
            tot = tot - 20

    # frete
    if tot < 200:
        tot = tot + 25

    # forma de pagamento
    if pg == "cartao":
        tot = tot + tot * 0.025
    elif pg == "boleto":
        tot = tot + 3.0
    elif pg == "pix":
        tot = tot
    else:
        print("ERRO: pagamento invalido")
        return "PAGAMENTO_INVALIDO"

    # baixa estoque
    for i in itens:
        c.execute("update prod set qtd = qtd - " + str(i[1]) + " where id = " + str(i[0]))

    # grava pedido
    tot = round(tot, 2)
    c.execute("insert into ped values (" + str(n) + ", '" + cli + "', " + str(tot) + ", 'OK')")
    db.commit()

    # avisa cliente
    print("Enviando email para " + r[2] + ": pedido " + str(n) + " no valor de R$ " + str(tot))
    log.append("fim pedido " + str(n))
    return "OK"


if __name__ == "__main__":
    print(proc("Ana", [(1, 2), (2, 1)], "PROMO5", "pix"))
    print(proc("Bruno", [(3, 2)], "", "cartao"))
    print(proc("Carla", [(2, 1)], "BEMVINDO", "boleto"))
    print(proc("Zeca", [(1, 1)], "", "pix"))
    print(proc("Carla", [(3, 5)], "", "pix"))
    print(log)

# Changelog

Todas as mudanças relevantes deste projeto são registradas aqui.
O formato segue o [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e o projeto usa [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.1.0] - 2026-11-09

### Adicionado
- `CHANGELOG.md` com o histórico de versões.
- ADR `docs/adr-001-desconto-vip.md`, que registra a decisão sobre o desconto VIP.
- Análise estática com Semgrep no pull request (verificação em Checks).

### Alterado
- O cupom `BEMVINDO` passa a dar R$ 30 de desconto em vez de R$ 20, em pedidos acima de R$ 100 (#1, PR #2).

### Corrigido
- Nada nesta versão.

## [1.0.0] - 2026-11-09

### Adicionado
- Sistema de pedidos legado (`pedidos_legado.py`), com cadastro de clientes, produtos e pedidos, cupons (`PROMO5` e `BEMVINDO`), frete e formas de pagamento.
- `README.md` com a identificação do autor e as instruções de execução.

### Alterado
- O desconto do cliente VIP passa de 10% para 15%. O conflito entre as branches `campanha` (12%) e `ajuste-comercial` (15%) foi resolvido a favor do ajuste comercial (ver ADR-001).

### Corrigido
- Nada nesta versão.

[1.1.0]: https://github.com/ArthurBorges002/pedidos-config/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/ArthurBorges002/pedidos-config/releases/tag/v1.0.0

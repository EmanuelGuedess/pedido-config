# ADR-001: Desconto do cliente VIP

- **Status:** Aceito
- **Data:** 2026-11-09
- **Autor:** Arthur Gabriel Borges

## Contexto

O desconto do cliente VIP em `pedidos_legado.py` era de 10%. Duas áreas da empresa pediram mudanças nessa mesma regra ao mesmo tempo:

- **Marketing (branch `campanha`):** 12%, para uma campanha promocional.
- **Comercial (branch `ajuste-comercial`):** 15%, como nova política comercial para clientes VIP.

As duas branches alteraram a mesma linha. Ao integrar as duas na `main`, o Git acusou conflito, e foi preciso decidir qual regra vale.

## Decisão

O desconto VIP passa a ser de **15%**, a regra da branch `ajuste-comercial`. A proposta de 12% da campanha foi descartada.

Motivos:
- O ajuste comercial é uma política permanente. A campanha é temporária e não deve sobrescrever a regra vigente.
- 15% é o maior dos dois valores, então nenhum cliente VIP sai perdendo em relação ao que a campanha prometia.
- O código só aceita um valor para essa regra, e manter os dois exigiria uma lógica de vigência que não existe hoje.

## Consequências

- **Positivas:** a regra fica única e clara. A decisão está documentada aqui, no commit de merge e no release v1.0.0.
- **Negativas:** a receita por pedido VIP diminui. A campanha de marketing precisa ser reavaliada, porque o desconto de 12% ficou abaixo do que o cliente VIP já recebe.
- **Riscos e próximos passos:** o percentual continua fixo no código. Se as campanhas temporárias voltarem a se repetir, vale extrair os descontos para configuração, com data de vigência, para evitar novos conflitos na mesma linha.

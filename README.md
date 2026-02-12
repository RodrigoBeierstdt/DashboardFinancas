# Dashboard de Controle Financeiro para Obras

Criei este projeto em Python para resolver um problema que vejo muito em construtoras: a dificuldade de acompanhar os gastos que ficam perdidos em várias planilhas de Excel. 

O objetivo foi transformar esses dados brutos em um painel visual simples, onde qualquer pessoa do escritório consiga bater o olho e entender se a obra está no lucro ou no prejuízo.

### O que o sistema faz:
- Mostra o orçamento total planejado contra o que já foi gasto de verdade.
- Calcula o saldo atual automaticamente para cada projeto.
- Tem um gráfico de barras que compara os gastos por categoria (materiais, mão de obra, etc).
- Gera um relatório em PDF na hora para quem precisa imprimir ou mandar por e-mail.

### O que usei para construir:
- Python (Lógica principal)
- Streamlit (Para criar a interface do site)
- Pandas (Para organizar as tabelas e fazer as somas)
- Plotly (Para os gráficos interativos)
- FPDF (Para a parte do relatório em PDF)

### Como visualizar o projeto:
O dashboard está rodando online neste link: [[DASHBOARD FINANCEIRO](https://dashboardrodrigo.streamlit.app)]

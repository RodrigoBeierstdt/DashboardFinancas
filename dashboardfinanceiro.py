# --- ROTEIRO DO SISTEMA DE INTELIGÊNCIA FINANCEIRA (PARA O LINKEDIN) ---

# 1. OBJETIVO DO SISTEMA:
# Criar um Dashboard Web que transforma dados de custos de obra em indicadores visuais.
# Foco total em análise financeira: Orçado vs. Gasto Real.

# 2. FERRAMENTAS QUE ESTOU USANDO:
# - Streamlit: Para criar a interface do site (botões, abas e textos).
# - Pandas: Para ler a planilha e fazer os cálculos (soma, subtração, filtros).
# - Plotly: Para gerar os gráficos interativos que mudam conforme o filtro.
# - FPDF: Para gerar o relatório em PDF com um clique.

# 3. O QUE O CÓDIGO PRECISA FAZER (PASSO A PASSO):
# A) Carregar os dados: Ler o arquivo Excel ou gerar dados fictícios com Pandas.
# B) Calcular KPIs: Somar o Orçamento Total, o Gasto Real e calcular o Saldo.
# C) Criar a Interface:
#    - Aba 1 (Painel): Mostrar cartões com os números grandes e uma barra de progresso.
#    - Aba 2 (Gráficos): Mostrar um gráfico de barras comparando categorias.
#    - Filtros: Criar uma caixinha (selectbox) para o usuário escolher qual obra ou categoria quer ver.
# D) Exportar: Criar a lógica para transformar os números da tela em um arquivo PDF.

# 4. DIFERENCIAL PARA O MEU ESTÁGIO:
# Mostrar que eu sei tratar dados (Pandas), criar visualizações (Plotly) 
# e entregar uma solução pronta para o usuário final (Streamlit).

import streamlit as st
import pandas as pd
import os
from PIL import Image
from datetime import datetime
import plotly.express as px

# Função para carregar os dados (pode ser de um arquivo ou gerados aleatoriamente)
def carregar_dados():
    # Verificar se o arquivo existe
    if os.path.exists('dados_obras.xlsx'):
        df = pd.read_excel('dados_obras.xlsx')
    else:
        # Gerar dados fictícios
        data = {
            'Obra': ['Obra A', 'Obra B', 'Obra C'],
            'Categoria': ['Materiais', 'Mão de Obra', 'Equipamentos'],
            'Orçamento': [100000, 150000, 50000],
            'Gasto Real': [90000, 160000, 45000]
        }
        df = pd.DataFrame(data)
    return df

# Função para calcular os KPIs
def calcular_kpis(df):
    orcamento_total = df['Orçamento'].sum()
    gasto_real_total = df['Gasto Real'].sum()
    saldo = orcamento_total - gasto_real_total
    return orcamento_total, gasto_real_total, saldo
# Função para criar o dashboard
def criar_dashboard(df):
    st.title("Dashboard de Inteligência Financeira")
    
    # Calcular KPIs
    orcamento_total, gasto_real_total, saldo = calcular_kpis(df)
    
    # Exibir KPIs
    st.subheader("KPIs")
    col1, col2, col3 = st.columns(3)
    col1.metric("Orçamento Total", f"R$ {orcamento_total:,.2f}")
    col2.metric("Gasto Real Total", f"R$ {gasto_real_total:,.2f}")
    col3.metric("Saldo", f"R$ {saldo:,.2f}")
    
    # Filtro para selecionar obra ou categoria
    filtro = st.selectbox("Selecione a Obra ou Categoria", options=['Todas'] + df['Obra'].unique().tolist() + df['Categoria'].unique().tolist())
    
    if filtro != 'Todas':
        df_filtrado = df[(df['Obra'] == filtro) | (df['Categoria'] == filtro)]
    else:
        df_filtrado = df
    
    # Gráfico de barras comparando Orçamento e Gasto Real
    st.subheader("Comparação Orçamento vs Gasto Real")
    fig = px.bar(df_filtrado, x='Obra', y=['Orçamento', 'Gasto Real'], barmode='group')
    st.plotly_chart(fig)
    
    # Botão para exportar PDF
    if st.button("Exportar Relatório em PDF"):
        exportar_pdf(df_filtrado)
# Função para exportar o relatório em PDF
def exportar_pdf(df):
    from fpdf import FPDF
    
    pdf = FPDF()
    pdf.add_page()
    
    # Título
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Relatório de Inteligência Financeira", ln=True, align='C')
    
    # Data
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Data: {datetime.now().strftime('%Y-%m-%d')}", ln=True, align='C')
    
    # Tabela de dados
    pdf.set_font("Arial", size=12)
    for index, row in df.iterrows():
        pdf.cell(40, 10, txt=row['Obra'], border=1)
        pdf.cell(40, 10, txt=row['Categoria'], border=1)
        pdf.cell(40, 10, txt=f"R$ {row['Orçamento']:,.2f}", border=1)
        pdf.cell(40, 10, txt=f"R$ {row['Gasto Real']:,.2f}", border=1)
        pdf.ln()
    
    # Salvar o PDF
    pdf.output("relatorio_inteligencia_financeira.pdf")
    st.success("Relatório exportado com sucesso!")
# Função principal
def main():
    df = carregar_dados()
    criar_dashboard(df)
if __name__ == "__main__":
    main()
    

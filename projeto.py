# comparador_precos_interativo.py
# Comparador de preços moderno e interativo com Streamlit

import streamlit as st
from streamlit_extras.let_it_rain import rain
from streamlit_extras.colored_header import colored_header

# Configuração da página
st.set_page_config(page_title="Comparador de Preços", page_icon="🛒", layout="centered")

# Cabeçalho estilizado
colored_header(
    label="🛍️ Comparador de Preços Inteligente",
    description="Descubra rapidamente onde o mesmo produto está **mais barato**.",
    color_name="blue-70",
)

# Entrada do produto
produto = st.text_input("**Produto:**", placeholder="Exemplo: Arroz 5kg")

# Divisão em 3 colunas para supermercados
st.markdown("### 🏪 Informe os supermercados e preços:")

col1, col2, col3 = st.columns(3)
mercados = []

with col1:
    nome1 = st.text_input("Supermercado 1", placeholder="Ex: Central")
    preco1 = st.number_input("Preço", min_value=0.0, step=0.01, format="%.2f")
    if nome1:
        mercados.append((nome1, preco1))

with col2:
    nome2 = st.text_input("Supermercado 2", placeholder="Ex: Super Bom")
    preco2 = st.number_input("Preço ", min_value=0.0, step=0.01, format="%.2f")
    if nome2:
        mercados.append((nome2, preco2))

with col3:
    nome3 = st.text_input("Supermercado 3", placeholder="Ex: Preço Justo")
    preco3 = st.number_input("Preço  ", min_value=0.0, step=0.01, format="%.2f")
    if nome3:
        mercados.append((nome3, preco3))

# Botão principal
st.markdown("---")
botao = st.button("🔍 Comparar agora")

# Quando clicar
if botao:
    if not produto:
        st.warning("Por favor, digite o nome do produto.")
    elif len(mercados) < 3:
        st.warning("Preencha o nome e o preço dos três supermercados.")
    else:
        menor_preco = min(preco for _, preco in mercados)
        mais_baratos = [nome for nome, preco in mercados if preco == menor_preco]

        # Efeito visual se houver empate
        if len(mais_baratos) > 1:
            rain(emoji="🎉", font_size=40, falling_speed=3, animation_length=1)
            st.balloons()
        else:
            rain(emoji="💰", font_size=40, falling_speed=4, animation_length=1)

        # Exibir resultado em destaque
        st.success(f"### ✅ Resultado para **{produto}**")
        st.markdown(
            f"""
            **Mais barato em:** {', '.join(mais_baratos)}  
            **Preço:** R$ {menor_preco:.2f}
            """
        )

        # Mostrar tabela comparativa
        st.markdown("#### 🧾 Comparativo completo:")
        st.dataframe(
            {"Supermercado": [m[0] for m in mercados], "Preço (R$)": [m[1] for m in mercados]},
            use_container_width=True,
            hide_index=True,
        )

# Rodapé bonito
st.markdown("---")
st.caption("✨ Desenvolvido com [Streamlit](https://streamlit.io) — Projeto de comparação de preços minimalista e interativo.")

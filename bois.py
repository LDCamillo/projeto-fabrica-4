import streamlit as st
import pandas as pd

# ⚙️ Configurações da página
st.set_page_config(
    page_title="Ranking dos Bois 🐂",
    page_icon="🐄",
    layout="centered"
)

# 🧾 Cabeçalho
st.title("🐄 Fazenda Rio Claro — Ranking dos Bois")
st.caption("Organize os bois do mais pesado para o mais leve.")

st.divider()

# 🧠 Entrada de dados (input → conversão → processamento)
with st.form("form_bois"):
    st.subheader("📥 Dados dos bois")

    col1, col2 = st.columns(2)
    with col1:
        boi1 = st.text_input("Nome do boi 1:")
        boi2 = st.text_input("Nome do boi 2:")
        boi3 = st.text_input("Nome do boi 3:")
    with col2:
        peso1 = st.number_input(f"Peso de {boi1 or 'boi 1'} (kg, use ponto):", min_value=0.0, format="%.2f")
        peso2 = st.number_input(f"Peso de {boi2 or 'boi 2'} (kg, use ponto):", min_value=0.0, format="%.2f")
        peso3 = st.number_input(f"Peso de {boi3 or 'boi 3'} (kg, use ponto):", min_value=0.0, format="%.2f")

    enviar = st.form_submit_button("📊 Gerar Ranking")

# 🧩 Processamento
if enviar:
    # Verifica se todos os campos estão preenchidos
    if not boi1 or not boi2 or not boi3:
        st.warning("⚠️ Preencha o nome de todos os bois.")
    elif peso1 == 0 or peso2 == 0 or peso3 == 0:
        st.warning("⚠️ Todos os pesos devem ser maiores que zero.")
    else:
        # Cria a lista com tuplas (nome, peso)
        bois = [
            (boi1, peso1),
            (boi2, peso2),
            (boi3, peso3)
        ]

        # Ordena em ordem decrescente de peso
        ranking = sorted(bois, key=lambda x: x[1], reverse=True)

        # 🖨️ Saída formatada (simulando um terminal moderno)
        st.divider()
        st.subheader("=== 🏆 Ranking (mais pesado → mais leve) ===")

        for i, (nome, peso) in enumerate(ranking, start=1):
            st.write(f"{i}) **{nome}** — {peso:.2f} kg")

        # Mostra também em formato de tabela
        df = pd.DataFrame(ranking, columns=["Nome do Boi", "Peso (kg)"])
        df["Peso (kg)"] = df["Peso (kg)"].map(lambda x: f"{x:.2f}")
        st.table(df)

        st.success("✅ Ranking gerado com sucesso!")
    
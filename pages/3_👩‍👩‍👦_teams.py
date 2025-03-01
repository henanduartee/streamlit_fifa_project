import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Teams",
    page_icon="⚽",
    layout="wide"
)

# Verifica se os dados estão carregados na session state
if "data" not in st.session_state:
    st.error("Os dados ainda não foram carregados. Retorne à página inicial e recarregue o dataset.")
    st.stop()

# Carregar dados
df_data = st.session_state["data"]

# Seleção de Clube
clubes = sorted(df_data["Club"].dropna().unique())
club = st.sidebar.selectbox("🏟️ Selecione um Clube", clubes)

# Filtrar jogadores do clube selecionado
df_filtered = df_data[df_data["Club"] == club].set_index("Name")

# Exibir Logo do Clube
if "Club Logo" in df_filtered.columns and not df_filtered["Club Logo"].isna().all():
    st.image(df_filtered.iloc[0]["Club Logo"], width=150)

st.markdown(f"## {club}")

# Definir colunas para exibição
columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)",
           "Joined", "Height(cm.)", "Weight(lbs.)", "Contract Valid Until", "Release Clause(£)"]

# Remover colunas ausentes para evitar erro
columns = [col for col in columns if col in df_filtered.columns]

# Exibir Tabela de Jogadores
with st.container():
    st.dataframe(df_filtered[columns],
                 column_config={
                     "Overall": st.column_config.ProgressColumn(
                         "Overall", format="%d", min_value=0, max_value=100),
                     "Wage(£)": st.column_config.ProgressColumn(
                         "Salário Semanal", format="£{:,.0f}".format, 
                         min_value=0, max_value=df_filtered["Wage(£)"].max()),
                     "Photo": st.column_config.ImageColumn("Foto"),
                     "Flag": st.column_config.ImageColumn("Nacionalidade"),
                 })
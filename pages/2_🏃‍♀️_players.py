import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Player Stats",
    page_icon="🏃‍♂️",
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
df_players = df_data[df_data["Club"] == club]
players = sorted(df_players["Name"].dropna().unique())

# Seleção de Jogador
player = st.sidebar.selectbox("🎽 Selecione um Jogador", players)

# Filtrar estatísticas do jogador selecionado
player_stats = df_players[df_players["Name"] == player].iloc[0]

# Exibir Informações do Jogador
st.image(player_stats["Photo"], width=150)
st.title(player_stats["Name"])
st.markdown(f"**🏠 Clube:** {player_stats['Club']}")
st.markdown(f"**🎯 Posição:** {player_stats['Position']}")

# Informações Físicas
col1, col2, col3 = st.columns(3)
col1.markdown(f"**📅 Idade:** {player_stats['Age']} anos")
col2.markdown(f"**📏 Altura:** {player_stats['Height(cm.)'] / 100:.2f} m")
col3.markdown(f"**⚖️ Peso:** {player_stats['Weight(lbs.)'] * 0.453:.1f} kg")
st.divider()

# Overall
st.subheader(f"⭐ Overall: {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

# Métricas Financeiras
col1, col2, col3 = st.columns(3)
col1.metric(label="💰 Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="💵 Salário semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="📑 Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")
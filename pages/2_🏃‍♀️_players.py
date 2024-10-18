import streamlit as st

st.set_page_config(
    page_title="Player",
    page_icon="🏃‍♀️",
    layout="wide"
)
# essa é a forma de importar os dados de '1__home.py' para manipulacao.
df_data = st.session_state["data"]

clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Club", clubes)

df_players = df_data[(df_data["Club"] == club)]

players = df_players["Name"].unique()
player = st.sidebar.selectbox("Jogador", players)

# cria um novo dataframe baseado no nome do jogador selecionado no 'selectbox'
players_stats = df_data[df_data["Name"] == player].iloc[0]
st.image(players_stats["Photo"])
st.title(players_stats["Name"])
st.markdown(f"**Clube:** {players_stats['Club']}")
st.markdown(f"**Posição:** {players_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {players_stats['Age']}")
col2.markdown(f"**Altura:** {players_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {players_stats['Weight(lbs.)'] * 0.453:.2f}")
st.divider()

st.subheader(f"Overall {players_stats['Overall']}")
st.progress(int(players_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {players_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {players_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {players_stats['Release Clause(£)']:,}")
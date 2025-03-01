import pandas as pd
import streamlit as st
from datetime import datetime
from pathlib import Path

# Configuração da Página
st.set_page_config(
    page_title="FIFA 23 Dataset",
    page_icon="⚽",
    layout="wide"
)

# Caminho do dataset
DATASET_PATH = Path(__file__).parent / 'data' / "CLEAN_FIFA23_official_data.csv"

@st.cache_data
def load_data(filepath: Path) -> pd.DataFrame:
    """
    Carrega o dataset do FIFA 23 e aplica filtros iniciais.
    
    Args:
        filepath (Path): Caminho do arquivo CSV.
    
    Returns:
        pd.DataFrame: DataFrame filtrado e ordenado.
    """
    df = pd.read_csv(filepath, index_col=0)
    
    # Filtrando jogadores com contrato válido e valor positivo
    df = df[df["Contract Valid Until"] >= datetime.today().year]
    df = df[df["Value(£)"] > 0]

    # Ordenando por Overall (Melhores jogadores primeiro)
    df = df.sort_values(by="Overall", ascending=False)
    
    return df

# Carregar dados na session state
if "data" not in st.session_state:
    st.session_state["data"] = load_data(DATASET_PATH)

# Interface Streamlit
st.title("📊 FIFA 23 Official Dataset")
st.sidebar.markdown("Desenvolvido por **Henan L. Duarte**")

# Botão para acessar os dados no Kaggle
st.link_button(
    "📂 Acesse os dados no Kaggle", 
    "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data"
)

st.markdown(
    """
    Este dataset contém informações detalhadas sobre jogadores de futebol profissionais de **2017 a 2023**.  
    São **mais de 17.000 registros**, incluindo:
    
    - 📌 Estatísticas dos jogadores  
    - 📊 Características físicas e demográficas  
    - 🏆 Afiliações a clubes e contratos  
    - 💰 Avaliação de mercado e atributos técnicos  
    
    🔍 O conjunto de dados é útil para análises de desempenho, evolução de jogadores e tendências do mercado de transferências.
    """
)

import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)

# Verifica se 'data' está no session_state
# O session_state armazena dados entre execuções, ou seja, se já houver dados armazenados, não é necessário recarregar ou solicitar novamente
if "data" in st.session_state:
    dadosfifa = st.session_state['data']  # 'dadosfifa' armazena o DataFrame com os dados do FIFA

    # Obtém todos os clubes disponíveis
    # 'value_counts()' retorna a contagem de cada clube e 'index' nos dá a lista dos nomes dos clubes
    clubes = dadosfifa['Club'].unique()

    # Cria um seletor de clubes no Streamlit
    # Aqui o usuário pode selecionar um clube da lista de clubes disponíveis
    clube = st.sidebar.selectbox('Selecione o clube', clubes)

    # Filtra os dados para o clube selecionado
    # Filtra o DataFrame 'dadosfifa' onde o clube corresponde ao clube selecionado
    clubefiltro = dadosfifa[dadosfifa['Club'] == clube].set_index("Name")
    clubeselecione = clubefiltro.iloc[0]
    st.image(clubeselecione['Club Logo'])

    st.title(f"_Equipe: {clubeselecione['Club']}_")
    

    columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

    st.dataframe(clubefiltro[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Progresso", format="%d", min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn("Ganhos semana", format="£%f", 
                                                    min_value=0, max_value=clubefiltro["Wage(£)"].max()),
                "Photo": st.column_config.ImageColumn("Foto"),
                "Flag": st.column_config.ImageColumn("Paises"),
             })
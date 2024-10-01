import streamlit as st
import pandas as pd

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
    clubefiltro = dadosfifa[dadosfifa['Club'] == clube]

    # Obtém todos os jogadores disponíveis no clube filtrado
    # Aqui filtramos os jogadores que pertencem ao clube selecionado
    jogadores = clubefiltro['Name'].unique()

    # Cria um seletor de jogadores no Streamlit
    # Aqui o usuário pode selecionar um jogador da lista de jogadores disponíveis no clube filtrado
    jogador = st.sidebar.selectbox('Selecione o jogador', jogadores)

    # Filtra os dados para o jogador selecionado
    # Filtra os dados do 'clubefiltro' para exibir apenas o jogador selecionado
    jogadorfiltrado = clubefiltro[clubefiltro['Name'] == jogador]

    #st.write(jogadorfiltrado)
    jogadorSelecionado = jogadorfiltrado.iloc[0]
    clubeSelecionado = clubefiltro.iloc[0]
    st.title(f"Jogador {jogadorSelecionado["Name"]}")
    st.image(jogadorSelecionado['Photo'])
    coluna1,coluna2 = st.columns(2)
    coluna1.markdown(f"Clube {clubeSelecionado['Club']}")
    #coluna2.image(jogadorSelecionado['Club Logo'])
    st.divider()
    coluna1perfil,coluna2perfil,coluna3perfil,coluna4perfil = st.columns(4)
    coluna1perfil.markdown(f"Altura: {jogadorSelecionado['Height(cm.)']/100}")
    coluna2perfil.markdown(f"Idade {jogadorSelecionado['Age']}")
    coluna3perfil.markdown(f'Número do uniforme {int(jogadorSelecionado['Kit Number'])}')
    coluna4perfil.markdown(f"Posição do jogador : {jogadorSelecionado['Position']}")
    st.divider()
    st.subheader(f"Progresso do jogador: {jogadorSelecionado['Overall']}")
    st.progress(int(jogadorSelecionado['Overall']))
    st.divider()
    st.subheader(f"Potencial do jogador: {jogadorSelecionado['Potential']} ")
    st.progress(int(jogadorSelecionado['Potential']))
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Valor de mercado", value=f"£ {jogadorSelecionado['Value(£)']:,}")
    col2.metric(label="Remuneração semanal", value=f"£ {jogadorSelecionado['Wage(£)']:,}")
    col3.metric(label="Cláusula de rescisão", value=f"£ {jogadorSelecionado['Release Clause(£)']:,}")
   




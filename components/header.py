from config import COLORS

def show_header():
    from streamlit import markdown
    
    header_html = f"""
    <div class="main-header">
        <h1>🌿 HortView - Análise de Preços de Hortaliças</h1>
        <p>Monitoramento e previsão de preços de produtos agrícolas</p>
    </div>
    """
    markdown(header_html, unsafe_allow_html=True)
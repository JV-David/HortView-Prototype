def show_footer():
    from streamlit import markdown
    
    footer_html = """
    <div style="text-align: center; color: #666; margin-top: 2rem;">
        <p><strong>HortView</strong> - Sistema de Análise de Preços de Hortaliças</p>
        <p>Desenvolvido para monitoramento e previsão de preços agrícolas</p>
    </div>
    """
    markdown(footer_html, unsafe_allow_html=True)
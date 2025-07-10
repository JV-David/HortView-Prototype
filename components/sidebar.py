def show_sidebar(vegetables):
    from streamlit import sidebar, title, selectbox
    
    with sidebar:
        title("🌱 Hortaliças")
        selected_vegetable = selectbox(
            "Selecione uma hortaliça:", 
            vegetables,
            key="vegetable_select"
        )
    return selected_vegetable
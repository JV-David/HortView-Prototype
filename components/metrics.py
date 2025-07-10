from config import COLORS

def create_metric_card(title, value, unit="MZN"):
    from streamlit import markdown
    
    card_html = f"""
    <div class="metric-card">
        <h3>{title}</h3>
        <h2>{value} {unit}</h2>
    </div>
    """
    markdown(card_html, unsafe_allow_html=True)

def show_price_metrics(data):
    from streamlit import columns
    
    cols = columns(3)
    with cols[0]:
        create_metric_card("Preço Atual", f"{data['Preço'].iloc[-1]:.2f}")
    
    with cols[1]:
        monthly_change = ((data['Preço'].iloc[-1] - data['Preço'].iloc[-2])/data['Preço'].iloc[-2])*100
        create_metric_card("Variação Mensal", f"{monthly_change:.1f}", "%")
    
    with cols[2]:
        create_metric_card("Período Analisado", len(data), "meses")
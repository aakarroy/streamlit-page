import streamlit as st

st.title("My Projects: ",text_alignment="justify",)
st.space("medium")
with st.container(width="stretch",horizontal_alignment="center",gap="large"):
    col1,col2 = st.columns([1,1],vertical_alignment="center",gap="large")
    with col1:
        st.latex(r'''
        \min_{\theta} \left[ \frac{1}{n} \sum_{i=1}^{n} L(f(x_i; \theta), y_i) + \lambda R(\theta) \right]
        ''')
        st.space("stretch")
        _,cent,_ = st.columns([0.15,1,0.15])
        with cent:
            st.link_button("Machine Learning Algorithms","https://github.com/aakarroy/Machine-Learning-Algorithms",)
    with col2:
        st.markdown("""
        <div style="text-align: left; font-family: 'Arial Black', Gadget, sans-serif;padding-left:40px">
            <span style="color: #3776ab; font-size: 60px; font-weight: 900; letter-spacing: -5px;">PY</span><span style="color: #ffd43b; font-size: 60px; font-weight: 900; letter-spacing: -5px;">THON</span>
        </div>
        """, unsafe_allow_html=True)
        _,cent,_ = st.columns([0.61,1,0.61])
        with cent:
            st.link_button("Python Projects","https://github.com/aakarroy/Nexus-Of-Knowledge-Library-Management-System")
    st.divider()
    col3,col4 = st.columns([1,1],vertical_alignment="center",gap="large")
    with col3:
        st.latex(r'''
        \mathbf{a}^{(l)} = \sigma\left(\mathbf{W}^{(l)}\mathbf{a}^{(l-1)} + \mathbf{b}^{(l)}\right)
        ''')
        _,cent,_ = st.columns([0.15,1,0.15])
        with cent:
            st.link_button("Deep Learning Models","https://github.com/aakarroy/BCI-CNN-LSTM")
    with col4:
        st.markdown("""
    <div style="
        text-align: left; 
        font-family: 'Arial Black', Gadget, sans-serif;
        padding-left:45px;">
        <span style="color: #086a35; font-size: 60px; font-weight: 900; letter-spacing: -3px;">Sahi</span><span style="color: #b5614b; font-size: 60px; font-weight: 900; letter-spacing: -3px;">bin</span>
    </div>
    """, unsafe_allow_html=True)
        _,cent,_ = st.columns([1,1,1])
        with cent:
            st.link_button("SAHI-BIN","https://github.com/aakarroy/SahiBin-AI")


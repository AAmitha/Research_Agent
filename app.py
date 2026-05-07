import streamlit as st
from agent import run_research

st.set_page_config(page_title="Research Agent", page_icon="🔍", layout="wide")

st.markdown(
    """
<style>
    body { background-color: #1a1a1a; }
    .stApp { background-color: #1a1a1a; }
    .user-message {
        background-color: #2d2d2d;
        border-radius: 18px 18px 4px 18px;
        padding: 12px 18px;
        margin: 8px 0;
        margin-left: 20%;
        color: #ffffff;
        font-size: 15px;
        line-height: 1.6;
    }
    .assistant-message {
        background-color: #1e1e1e;
        border: 1px solid #333;
        border-radius: 18px 18px 18px 4px;
        padding: 16px 20px;
        margin: 8px 0;
        margin-right: 20%;
        color: #e8e8e8;
        font-size: 15px;
        line-height: 1.6;
    }
    .header-title {
        text-align: center;
        color: #ffffff;
        font-size: 24px;
        font-weight: 600;
        margin-bottom: 4px;
    }
    .header-sub {
        text-align: center;
        color: #888;
        font-size: 13px;
        margin-bottom: 30px;
    }
    .stTextArea textarea {
        background-color: #2d2d2d !important;
        border: 1px solid #444 !important;
        border-radius: 12px !important;
        color: #ffffff !important;
        font-size: 15px !important;
        padding: 14px !important;
    }
    .stButton button {
        background-color: #cc785c !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 8px 20px !important;
        font-size: 14px !important;
    }
    footer { display: none; }
    #MainMenu { display: none; }
    header { display: none; }
</style>
""",
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "input_key" not in st.session_state:
    st.session_state.input_key = 0

st.markdown('<div class="header-title">🔍 Research Agent</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="header-sub">Powered by LangGraph · Tavily · Llama 3.2</div>',
    unsafe_allow_html=True,
)

if not st.session_state.messages:
    st.markdown("**Try asking:**")
    examples = [
        "What are the latest developments in AI agents?",
        "Compare Python vs JavaScript for machine learning",
        "What is retrieval augmented generation?",
        "Explain microservices architecture pros and cons",
    ]
    cols = st.columns(2)
    for i, ex in enumerate(examples):
        if cols[i % 2].button(ex, key=f"ex{i}"):
            st.session_state.pending_question = ex
            st.rerun()

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f'<div class="user-message">{msg["content"]}</div>', unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="assistant-message">🔍 {msg["content"]}</div>',
            unsafe_allow_html=True,
        )

question = st.text_area(
    "",
    value=st.session_state.get("pending_question", ""),
    height=80,
    placeholder="Ask a research question...",
    label_visibility="collapsed",
    key=f"input_{st.session_state.input_key}",
)

col1, col2 = st.columns([1, 6])
with col1:
    send = st.button("Send ↗")

if send and question.strip():
    st.session_state.pending_question = ""
    st.session_state.input_key += 1
    st.session_state.messages.append({"role": "user", "content": question})

    with st.spinner("Researching..."):
        answer = run_research(question)

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.rerun()

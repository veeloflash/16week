import streamlit as st
from src.ai.ai_client import ask_ai
from src.ai.classifier import classify_question
from src.data.data_logger import log_interaction
from src.data.data_reader import load_logs
from src.data.data_analysis import analyze_logs
from src.security.input_validator import validate_input

st.set_page_config(page_title="AI Step-by-Step Solver", layout="wide")

# Header Section
st.title("🤖 AI Step-by-Step Solver v1")

# Product Description Section
st.markdown("---")
st.subheader("📚 Product Overview")
st.markdown("""
This is an **AI-powered learning companion** designed to help students understand complex concepts 
through step-by-step explanations. The system:

- **Provides detailed solutions** to user questions
- **Categorizes questions** automatically (math, science, language, etc.)
- **Tracks learning progress** through interaction history
- **Maintains usage statistics** for learning insights

Learn at your own pace with intelligent, personalized explanations!
""")

# Security Section
st.markdown("---")
st.subheader("🔒 Security & Privacy")
st.markdown("""
Your data and privacy are protected through:

✅ **Input Validation** - All inputs are validated for malicious content
✅ **Prompt Injection Guard** - Advanced detection prevents prompt injection attacks  
✅ **Secure API Key Management** - API keys are loaded from environment variables, never hardcoded
✅ **Logging Protection** - All interactions are securely logged in JSONL format

The system actively blocks prompt injection attacks and malicious input patterns.
""")

# Input Section
st.markdown("---")
st.subheader("❓ Ask a Question")
question = st.text_area("Enter your question")

if st.button("Solve"):
    ok, msg = validate_input(question)
    if not ok:
        st.error(msg)
    else:
        category = classify_question(question)

        with st.spinner("Generating answer..."):
            answer = ask_ai(question)

        log_interaction(question, answer, category)

        st.subheader("✅ Answer")
        st.write(answer)

        st.session_state["question_input"] = ""


# Analytics Section
st.markdown("---")
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("📊 Show Stats"):
        df = load_logs()
        stats = analyze_logs(df)
        st.subheader("Usage Statistics")
        st.write(stats)

# Future Roadmap Section
with col2:
    st.subheader("🚀 Future Features")
    
st.markdown("""
We're constantly improving! Upcoming features include:

🔄 **User Accounts & Authentication** - Save your learning history across sessions  
📈 **Progress Tracking** - Visualize your learning journey and identify weak areas  
👨‍🏫 **Teacher Dashboard** - Educators can monitor student progress and customize questions  
🌍 **Multi-language Support** - Learn in your preferred language  
📱 **Mobile App** - Full mobile experience with offline mode  
🎯 **Personalized Recommendations** - AI-powered learning path suggestions  
🏆 **Gamification** - Earn badges and rewards for consistent learning  

Stay tuned for exciting updates!
""")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888; font-size: 12px;">
📝 AI Step-by-Step Solver v1.0 | Week 16 Capstone Project  
🔐 Security-First Design | 💾 Local Data Storage | 🤖 Powered by Groq API
</div>
""", unsafe_allow_html=True)


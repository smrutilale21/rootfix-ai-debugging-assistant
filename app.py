from datetime import datetime

import streamlit as st

from agent import analyze_bug
from sample_bugs import SAMPLE_BUGS
from utils import build_download_report

st.set_page_config(
    page_title="AI Debugging & Root Cause Assistant",
    page_icon="🛠️",
    layout="wide",
)


if "debug_history" not in st.session_state:
    st.session_state.debug_history = []


def get_code_language(language: str) -> str:
    language_map = {
        "Python": "python",
        "JavaScript": "javascript",
        "React": "javascript",
        "Java": "java",
        "SQL": "sql",
        "Other": "text",
    }

    return language_map.get(language, "text")


st.title("🛠️ AI Debugging & Root Cause Assistant")
st.caption(
    "Convert messy code errors into structured root-cause reports with fixes, severity, confidence score, assumptions, and prevention tips."
)


with st.sidebar:
    st.header("📌 Demo Samples")

    selected_sample = st.selectbox(
        "Choose a sample bug",
        list(SAMPLE_BUGS.keys()),
    )

    st.divider()

    st.header("🕘 Session History")

    if not st.session_state.debug_history:
        st.info("No debug reports yet.")
    else:
        for item in reversed(st.session_state.debug_history):
            st.markdown(f"""
**{item["bug_type"]}**  
Language: `{item["language"]}`  
Severity: `{item["severity"]}`  
Confidence: `{item["confidence_score"]}%`  
Time: {item["timestamp"]}

---
""")


sample = SAMPLE_BUGS[selected_sample]

languages = ["Python", "JavaScript", "React", "Java", "SQL", "Other"]

default_language = sample["language"] if sample["language"] in languages else "Other"

language = st.selectbox(
    "Programming Language",
    languages,
    index=languages.index(default_language),
)


if selected_sample != "None" and language != sample["language"]:
    st.warning(
        f"Selected sample is for {sample['language']}, but current language is {language}."
    )


col1, col2 = st.columns(2)

with col1:
    code = st.text_area(
        "Buggy Code",
        value=sample["code"],
        height=300,
        placeholder="Paste your buggy code here...",
    )

with col2:
    error = st.text_area(
        "Error / Traceback",
        value=sample["error"],
        height=300,
        placeholder="Paste the error message or traceback here...",
    )


expected_behavior = st.text_area(
    "Expected Behavior",
    value=sample["expected_behavior"],
    height=100,
    placeholder="What did you expect the code to do?",
)


context = st.text_area(
    "Additional Context",
    value=sample["context"],
    height=100,
    placeholder="Framework, library, environment, recent changes, API behavior, etc.",
)


analyze_button = st.button("🔍 Analyze Bug", type="primary")


if analyze_button:
    if not code.strip() or not error.strip():
        st.error("Please provide both buggy code and error/traceback.")
    else:
        with st.spinner("Analyzing root cause..."):
            try:
                result = analyze_bug(
                    language=language,
                    code=code,
                    error=error,
                    expected_behavior=expected_behavior,
                    context=context,
                )

                result_dict = result.model_dump()

                st.success("Debug analysis completed!")

                st.subheader("📊 Debug Summary")

                metric_col1, metric_col2, metric_col3 = st.columns(3)

                with metric_col1:
                    st.metric("Severity", result.severity)

                with metric_col2:
                    st.metric("Confidence", f"{result.confidence_score}%")

                with metric_col3:
                    st.metric("Bug Type", result.bug_type)

                tab1, tab2, tab3, tab4, tab5 = st.tabs(
                    [
                        "Root Cause",
                        "Fixed Code",
                        "Assumptions",
                        "Learning",
                        "Report JSON",
                    ]
                )

                with tab1:
                    st.markdown("### Bug Summary")
                    st.write(result.bug_summary)

                    st.markdown("### Root Cause")
                    st.write(result.root_cause)

                    st.markdown("### Error Location")
                    st.write(result.error_location)

                    st.markdown("### Confidence Explanation")
                    st.info(result.confidence_explanation)

                with tab2:
                    st.markdown("### Fixed Code")
                    st.code(result.fixed_code, language=get_code_language(language))

                with tab3:
                    st.markdown("### Assumptions")
                    if result.assumptions:
                        for assumption in result.assumptions:
                            st.markdown(f"- {assumption}")
                    else:
                        st.write("No major assumptions were required.")

                with tab4:
                    st.markdown("### Explanation of Fix")
                    st.write(result.explanation_of_fix)

                    st.markdown("### Prevention Tips")
                    for tip in result.prevention_tips:
                        st.markdown(f"- {tip}")

                    st.markdown("### Interview-style Learning Note")
                    st.info(result.learning_note)

                with tab5:
                    st.json(result_dict)

                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                st.session_state.debug_history.append(
                    {
                        "timestamp": timestamp,
                        "language": language,
                        "bug_type": result.bug_type,
                        "severity": result.severity,
                        "confidence_score": result.confidence_score,
                    }
                )

                download_report = build_download_report(
                    language=language,
                    code=code,
                    error=error,
                    expected_behavior=expected_behavior,
                    context=context,
                    result=result_dict,
                )

                st.download_button(
                    label="⬇️ Download Debug Report JSON",
                    data=download_report,
                    file_name="debug_report.json",
                    mime="application/json",
                )

            except Exception as e:
                st.error(f"Something went wrong: {e}")


st.divider()

st.markdown("""
### Why this matters

Developers, students, and freelancers often waste time understanding errors and stack traces.  
This assistant converts raw debugging information into a structured report containing root cause, fixed code, severity, assumptions, confidence explanation, prevention tips, and downloadable documentation.
""")

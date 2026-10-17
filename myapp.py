import streamlit as st
st.set_page_config(
    page_title="Soham Ajgaonkar",
    # page_icon="💻",
    layout="wide"
)
LEETCODE_BG = "#E67E22"
LEETCODE_TEXT = "#FFFFFF"
LEETCODE_FONT = "Arial"
LEETCODE_SIZE = "16px"
CODEFORCES_BG = "#2980B9"
CODEFORCES_TEXT = "#FFFFFF"
CODEFORCES_FONT = "Arial"
CODEFORCES_SIZE = "16px"
BUTTON_RADIUS = "10px"
BUTTON_PADDING = "10px 4px"
BUTTON_BORDER = "none"

# st.markdown(
#     f"""
#     <style>
#     /* Common button styling */
#     div.stButton > button,
#     div.stLinkButton > a {{
#         width: 100%;
#         border-radius: {BUTTON_RADIUS};
#         padding: {BUTTON_PADDING};
#         border: {BUTTON_BORDER};
#         font-weight: bold;
#         transition: all 0.3s ease;
#     }}

#     /* LeetCode button */
#     .st-key-leetcode a {{
#         background-color: {LEETCODE_BG};
#         color: {LEETCODE_TEXT};
#         font-family: {LEETCODE_FONT};
#         font-size: {LEETCODE_SIZE};
#     }}

#     /* Codeforces button */
#     .st-key-codeforces a {{
#         background-color: {CODEFORCES_BG};
#         color: {CODEFORCES_TEXT};
#         font-family: {CODEFORCES_FONT};
#         font-size: {CODEFORCES_SIZE};
#     }}

#     /* Hover effect */
#     div.stLinkButton > a:hover {{
#         filter: brightness(0.85);
#         border: {BUTTON_BORDER};
#         # transform: translateY(-2px);
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )
left_margin, photo_col, gap, intro_col, right_margin = st.columns([1, 2, 0.5, 5, 1],vertical_alignment="center")
with photo_col:
    st.image("assets/profile_photo.png",use_container_width=True)

with intro_col:
    st.title("Soham Ajgaonkar")

    st.write(
        "Hello! My name is Soham Ajgaonkar. I am an engineering "
        "student with interests in Machine Learning, "
        "Reinforcement Learning and Competitive Programming."
    )

    st.write("")  # Small vertical gap

    # Center both buttons under the introduction
    left, lc_col, cf_col, right= st.columns(
        [2, 2, 2, 3],
        gap="small"
    )

    with lc_col:
        with st.container(key="leetcode"):
            st.link_button(
                "LeetCode",
                "https://leetcode.com/u/sohamsa7/",
                use_container_width=True
            )

    with cf_col:
        with st.container(key="codeforces"):
            st.link_button(
                "Codeforces",
                "https://codeforces.com/profile/sohamsa7/",
                use_container_width=True
            )
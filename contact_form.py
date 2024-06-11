import streamlit as st

st.header(":mailbox: We are here help you!!!")

contact_form = """
<form action="https://formsubmit.co/honeyvasu159@gmail.com"  method="POST">
     <input type="text" name="name" required>
     <input type="email" name="email" required>
     <button type="submit">Send</button>
</form>

"""
st.markdown(contact_form,unsafe_allow_html=True)
def main_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

main_css("main_css.css")

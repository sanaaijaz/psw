import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker",page_icon="🔐")
st.title("Password Strength Checker")
st.markdown("""
## Welcome to the ultimate password strength checker!
use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
         we will give you helpful tips to create "a **Strong Password** 🔐""")


password=st.text_input("Enter your password" ,type="password")

feedback =[]
score = 0
if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be atleast 8 characters long. ")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):      
        score += 1

    
    else:
        feedback.append("password should contain both upper and lower case characters.")
    if  re.search(r'\d', password):         
        score += 1
    else:
        feedback.append("password should contain atleast one digit.")

    if re.search(r'[@!$%&]' ,password):
            score += 1
    else:
        feedback.append("password should contain at least one special character(@!$%&).")
    if score == 4:
                feedback.append("✔Your password is strong!")
    elif score == 3:
                feedback.append ("❌your password is medium strength it could be strong.")
    else:
                feedback.append("❌your password is weak.Please make it stronger.")

    if feedback:
                      st.markdown("## Improvement suggestion")
                      for tip in feedback:
                            st.write(tip)
else:
        st.info("please enter your password to get started.")                        

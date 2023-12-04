import streamlit as st





def cipher(text, key):
    results = ""
    ord_high = ord("Z")
    alfa = 26
    ord_low = ord("A")

    for i in text.upper():
        if i.isalpha():
            char_code = ord(i)
            new_char_code = char_code + key
            if new_char_code > ord_high:
                new_char_code -= alfa
            if new_char_code < ord_low:
                new_char_code += alfa
            new_char = chr(new_char_code)
            results += new_char
        else:
            results += i
    return results.title()


st.set_page_config(page_title="Ceaser Cipher", page_icon="⚔", layout="wide")



st.subheader("By Neros29 ⚔")
st.title("Ceaser Cipher")
st.write("---")
st.subheader("How to use this Cipher")
st.write("""
         To use this cipher start by putting in the text you would like to encod or decode. Then you should put the 
         key in the key in the key row. make sure your key is a number between one and twenty six. You will then 
         press the button to encipher or decipher. Your encrypted text or plain text will appear below the buttons.
         """)

text = st.text_input("Enter your text here", key="text_input")
key = st.text_input("Enter your key (an integer) here", key="key_input")

encode = st.button("Encode")
decode = st.button("Decode")
st.write("---")

if encode or decode:
    result = ""
    if not text or not key:
        st.error("Please enter text and key before encoding/decoding.")
    else:
        try:
            key = int(key)
            if encode:
                result = cipher(text, key)
            elif decode:
                result = cipher(text, -key)

            st.header("Result:")
            st.write(result)
        except ValueError:
            st.error("Please enter a valid integer key.")



st.write("---")
def unique_character(words):
    st=set()
    for i in words:
        st.add(i)
    return st
print(unique_character("hello"))

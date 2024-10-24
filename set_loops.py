def unique_character(string):
    st=set()
    for i in string:
        st.add(i)
    return st
print(unique_character("hello"))

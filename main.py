import streamlit as st
import pandas as pd


def main():
    # Importing the csv file

    name_file = 'train.csv'
    try:
        df = pd.read_csv(name_file)
    except IOError:
        print(" [ERROR] Can't read CSV file!"
              "\n 1) Remember to download the 'train.csv' file. "
              "\n 2) Put the file in the same directory of your project!"
              "\n 3) Make sure name_file is the same name of the file in your directory.")

    # The start of the page
    st.header('PANDAS RESUME')
    # General Information
    st.subheader('General Visualization of Data Frames')
    # Data Frame Head function:

    selectbox_options = ['Head of Data Frame', 'Numbers of Indexes']
    select = st.selectbox('Choose Function', selectbox_options)
    if select == selectbox_options[0]:

        slider = st.slider('Select the number of rows', 1, 890)
        st.dataframe(df.head(slider))
        st.subheader(f' Pandas Command: ')
        st.markdown(f'df.head({slider})')







if __name__ == '__main__':
    main()

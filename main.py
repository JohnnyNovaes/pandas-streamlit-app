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

    # Start of the page
    st.header('PANDAS RESUME')
    # General Information
    st.subheader('General Visualization of Data Frames')
    st.text('Provides examples of the basic functions for general visualization of data frames,\nin a '
            'interactive way.')
    # Select Box List
    selection_options = ['List Resume', 'dataFrame.head()', 'dataFrame.index']
    select = st.selectbox('Choose Function', selection_options)

    # Resume List
    if select == selection_options[0]:
        st.text(f'1){selection_options[1]} : Returns the first n rows')
        st.text(f'2){selection_options[2]} : The index (row labels) of the DataFrame.')

    # dataFrame.head()
    if select == selection_options[1]:

        slider = st.slider('Select the number of rows', 1, 890)
        st.dataframe(df.head(slider))
        st.subheader('Description')
        st.text(f'Returns the first {slider} rows')
        st.subheader(f'Command: ')
        st.text(f'df.head({slider})')

    # dataFrame.index
    if select == selection_options[2]:
        st.text(f'{df.index}')






if __name__ == '__main__':
    main()

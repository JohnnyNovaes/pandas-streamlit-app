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

    # Select Box List
    selection_options = ['Index',
                         'dataFrame.head()',
                         'dataFrame.index',
                         'dataFrame.shape',
                         'dataFrame.isna()',
                         'dataFrame.columns']

    select = st.sidebar.selectbox('General Information of DF', selection_options)

    # Resume List
    if select == selection_options[0]:
        # General Information
        st.subheader('General Information of Data Frames')
        st.text('Provides examples of the basic functions for general information of data frames,\nin a '
                'interactive way.')
        st.text(f'1){selection_options[1]} : Returns the first n rows')
        st.text(f'2){selection_options[2]} : The index (row labels) of the DataFrame.')
        st.text(f'3){selection_options[3]} : Return a tuple representing the dimensionality of the DataFrame.')
        st.text(f'4){selection_options[4]} : Return a boolean same-sized object indicating if the values are NA.')
        st.text(f'5){selection_options[5]} : The column labels of the DataFrame.')

    # dataFrame.head()
    if select == selection_options[1]:
        st.header('General Information of Data Frames')
        st.header("(pandas.DataFrame.head)")
        st.subheader("Result")
        slider = st.slider('Select the number of rows', 1, 890)
        st.dataframe(df.head(slider))
        st.subheader('Description')
        st.text(f'Returns the first {slider} rows')
        st.subheader(f'Command ')
        st.text(f'df.head({slider})')

    # dataFrame.index
    if select == selection_options[2]:
        st.header('General Information of Data Frames')
        st.header("(pandas.DataFrame.index)")
        st.subheader('Description')
        st.text('The index (row labels) of the DataFrame.')
        st.subheader("Result")
        st.text(f'{df.index}')
        st.dataframe(df.index)
        st.subheader('Command')
        st.text('dataFrame.index')

    # dataFrame.shape
    if select == selection_options[3]:
        st.header('General Information of Data Frames')
        st.header("(pandas.DataFrame.shape)")
        st.subheader("Result")
        st.text(f'{df.shape}')
        st.dataframe(df.shape)
        st.subheader('Description')
        st.text('Return a tuple representing the dimensionality of the DataFrame.')
        st.subheader("Command")
        st.text("dataFrame.shape")

    # dataFrame.isna()
    if select == selection_options[4]:
        st.header('General Information of Data Frames')
        st.header("(pandas.DataFrame.isna)")
        st.subheader("Result")
        st.text(f'{df.isna()}')
        st.dataframe(df.isna())
        st.subheader('Description')
        st.text('Return a boolean same-sized object indicating if the values are NA.')
        st.subheader("Command")
        st.text("dataFrame.isna()")

    # dataFrame.columns()
    if select == selection_options[5]:
        st.header('General Information of Data Frames')
        st.header("(pandas.DataFrame.columns)")
        st.subheader("Result")
        st.text(f'{df.columns}')
        st.dataframe(df.columns)
        st.subheader('Description')
        st.text('The column labels of the DataFrame.')
        st.subheader("Command")
        st.text("dataFrame.columns")





if __name__ == '__main__':
    main()

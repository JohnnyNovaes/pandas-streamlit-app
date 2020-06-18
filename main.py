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
                         '1) DataFrame.head()',
                         '2) DataFrame.index',
                         '3) DataFrame.shape',
                         '4) DataFrame.isna()',
                         '5) DataFrame.columns',
                         '6) DataFrame.loc[]',
                         '7) Filtering']

    select = st.sidebar.selectbox('General Information of DF', selection_options)

    # Resume List
    if select == selection_options[0]:
        # General Information
        st.subheader('General Information of Data Frames')
        st.text('Provides examples of the basic functions for general information of data frames,\nin a '
                'interactive way.')
        st.text(f'{selection_options[1]} : Returns the first n rows')
        st.text(f'{selection_options[2]} : The index (row labels) of the DataFrame.')
        st.text(f'{selection_options[3]} : Return a tuple representing the dimensionality of the DataFrame.')
        st.text(f'{selection_options[4]} : Return a boolean same-sized object indicating if the values are NA.')
        st.text(f'{selection_options[5]} : The column labels of the DataFrame.')
        st.text(f'{selection_options[6]} : Access a group of rows and columns by label(s) or a boolean array.')
        st.text(f'{selection_options[7]} : How to filter and select some data in your Data Frame.')

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
        st.subheader('Description')
        st.text('Return a tuple representing the dimensionality of the DataFrame.')
        st.subheader("Result")
        st.text(f'{df.shape}')
        st.dataframe(df.shape)
        st.subheader("Command")
        st.text("dataFrame.shape")

    # dataFrame.isna()
    if select == selection_options[4]:
        st.header('General Information of Data Frames')
        st.header("(pandas.DataFrame.isna)")
        st.subheader('Description')
        st.text('Return a boolean same-sized object indicating if the values are NA.')
        st.subheader("Result")
        st.text(f'{df.isna()}')
        st.dataframe(df.isna())
        st.subheader("Command")
        st.text("dataFrame.isna()")

    # dataFrame.columns()
    if select == selection_options[5]:
        st.header('General Information of Data Frames')
        st.header("(pandas.DataFrame.columns)")
        st.subheader('Description')
        st.text('The column labels of the DataFrame.')
        st.subheader("Result")
        st.text(f'{df.columns}')
        st.dataframe(df.columns)
        st.subheader("Command")
        st.text("dataFrame.columns")
        # Selecting Columns
        st.header("Selecting Columns")
        st.subheader("Description ")
        st.text("Selecting columns in a Data Frame.")
        st.subheader("Result")
        num_columns = st.slider("Select n° of column(s)", 1, 12)
        index = range(0, num_columns)
        # Concatenate in a string of the columns.
        col = " "
        for n in index:
            col = col + " " + df.columns[n]
        # Show Data Frame Columns
        st.dataframe(df[col.split()])
        st.subheader("Command")
        st.text(f'dataFrame[{col.split()}]')

    # dataFrame.loc
    if select == selection_options[6]:
        st.header('General Information of Data Frames')
        st.header("(pandas.DataFrame.columns)")
        st.subheader('Description')
        st.text('Access a group of rows and columns by label(s) or a boolean array.')
        st.subheader("Result")
        start_row = st.slider('Start Row', 0, len(df.index))
        finish_row = st.slider('Finish Row', start_row, len(df.index))
        st.dataframe(df.loc[start_row: finish_row])
        st.subheader("Command")
        st.text(f'dataFrame.loc[{start_row}:{finish_row}]')

    # Filtering
    if select == selection_options[7]:
        st.header('General Information of Data Frames')
        st.subheader('Filtering')
        st.text('This sector shows how to select some specifics data in your data frame. ')
        st.text('The data set used here is the Titanic, from kaggle.com')
        st.subheader('Titanic Data Set')
        st.dataframe(df.head())
        st.subheader('Selecting data')
        st.text('1º - Select the columns you want (You can chose more than one!)')
        columns = st.multiselect('Chose the columns', df.columns)
        st.text('2º - Select the rows you want ')
        start_row = st.slider('Start Row', 0, len(df.index))
        finish_row = st.slider('Finish Row', start_row, len(df.index))
        st.text('3º - Chose a column and a word - or number -  you want to find in this column.')
        column = st.selectbox('Chose a Columns', df.columns)
        word_num = st.radio('Do you want to find a word or a number?', ['Word', 'Number'])
        find_word = st.text_input(f'Type a ({word_num}) you want to find in the ({column}) column')
        if word_num == 'Number':
            operator = st.radio(f'Do you want to find in {column} a number(s) (smaller|bigger|equal)?'
                                f' :', ['Smaller( < )', 'Bigger( > )', 'Equal( == )'])
        st.subheader('Result')
        button = st.button('Filter')
        if len(columns) == 0:
            st.text('Please select some column(s)!')
        else:
            if button:
                if word_num == 'Word':
                    try:
                        st.dataframe(df[df[column].str.contains(find_word)][columns].loc[start_row:finish_row])
                    except AttributeError:
                        st.text("ERROR - Please, type a word to find in the data frame!!")
                elif word_num == 'Number':

                    try:
                        if operator == 'Smaller( < )':
                            st.dataframe(df[df[column] < int(find_word)][columns].loc[start_row:finish_row])
                        elif operator == 'Bigger( > )':
                            st.dataframe(df[df[column] > int(find_word)][columns].loc[start_row:finish_row])
                        elif operator == 'Equal( == )':
                            st.dataframe(df[df[column] == int(find_word)][columns].loc[start_row:finish_row])
                    except ValueError:
                        st.text("ERROR - Please, type a number to find in the data frame!!")


if __name__ == '__main__':
    main()

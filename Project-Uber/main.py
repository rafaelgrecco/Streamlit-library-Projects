import streamlit as st
import pandas as pd
import numpy as np

data = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

def main():

    st.title('Uber data application')

    @st.cache
    def data_load(nrows):
        df = pd.read_csv(data, nrows=nrows)
        lower_str = lambda x: str(x).lower()
        df.rename(lower_str, axis='columns', inplace=True)
        df['date/time'] = pd.to_datetime(df['date/time'])
        return df

    df = data_load(1000)

    if st.sidebar.checkbox('Show first thousand lines'):
        st.success('The first thousand lines were loaded')
        st.write(df)
        

    st.subheader('Number of runs per hour')
    hist = np.histogram(df['date/time'].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist)

    hour_filter = st.slider('hour', 0,23,1)
    f_data = df[df['date/time'].dt.hour == hour_filter]
    st.subheader('Map:')
    st.map(f_data)
    
if __name__ == '__main__':
    main()

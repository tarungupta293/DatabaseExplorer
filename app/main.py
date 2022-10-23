import streamlit as st
import pandas as pd
import constants

def set_app_config():
    st.set_page_config(
        "AT3 - Database Explorer WebApp",
        "🧊",
        "wide",
        "expanded",
        {
            'Get Help': 'https://www.extremelycoolapp.com/help',
            'Report a bug': "https://www.extremelycoolapp.com/bug",
            'About': "# This is a header. This is an extremely cool app!"
        }
    )
    # to hide the top right toolbar option
    st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style> """, True)
    df = pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    })
    df
    st.write("Here's our first attempt at using data to create a table:")
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))
    st.title("this is the app title")
    st.header("this is the markdown")
    st.markdown("this is the header")
    st.subheader("this is the subheader")
    st.caption("this is the caption")
    st.code("x=2021")
    st.latex(r''' a+a r^1+a r^2+a r^3 ''')


def set_session_state(key, value=None):
    st.session_state[key] = value


def set_session_states(keys, value=None):
    for key in keys:
        set_session_state(key)


def get_session_value_from_key(key):
    return st.session_state[key]


def display_session_state():
    for item in st.session_state.items():
        item


set_app_config()
set_session_state(constants.Constants.SESSION_STATE_LAUNCH_KEY)
set_session_state(constants.Constants.SESSION_STATE_LAUNCH2_KEY, 12)
set_session_state(constants.Constants.SESSION_STATE_LAUNCH3_KEY, 122)
get_session_value_from_key(constants.Constants.SESSION_STATE_LAUNCH_KEY)
print(get_session_value_from_key(constants.Constants.SESSION_STATE_LAUNCH2_KEY))
set_session_states(['db', 'db_host', 'db_name', 'db_port', 'db_user', 'db_pass', 'db_status', 'db_infos_df', 'schema_selected', 'table_selected', 'data'])

display_session_state()


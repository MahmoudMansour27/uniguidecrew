import pickle
from pathlib import Path
import streamlit_authenticator as stauths

names = ['Roaa', 'Yasmeen', 'Merhan', 'Arwa', 'Dr. Nora', 'Mahmoud']
usernames = ['roaa', 'yasmeen', 'merhan', 'arwa', 'dr.nora', 'mahmoud']
passwords = ['xxx', 'xxx', 'xxx', 'xxx', 'xxx', 'xxx']
hashed_passwords = stauths.Hasher(passwords).generate()
file_path = Path('hashed_pw.pkl')
with file_path.open('wb') as file:
    pickle.dump(hashed_passwords, file)
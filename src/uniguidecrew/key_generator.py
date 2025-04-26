import pickle
from pathlib import Path
import streamlit_authenticator as stauths

data = {
    'Roaa': {
        'username': 'r.abdulmajed2498@su.edu.eg',
        'password': 'xxx',
    },
    'Yasmeen': {
        'username': 'y.khalaf1600@su.edu.eg',
        'password': 'xxx',
    },
    'Merhan': {
        'username': 'm.hassan3800@su.edu.eg',
        'password': 'xxx',
    },
    'Arwa': {
        'username': 'a.mohammed2312@su.edu.eg',
        'password': 'xxx',
    },
    'Dr. Nora': {
        'username': 'dr.nora',
        'password': 'xxx',
    },
    'Dr Emad': {
        'username': 'dr.emad',
        'password': 'xxx',
    },
    'Mahmoud': {
        'username': 'mahmoud',
        'password': 'xxx',
    }
}

names = data.keys()
usernames = [info['username'] for info in data.values()]
passwords = [info['password'] for info in data.values()]

# Hash the passwords
hashed_passwords = stauths.Hasher(passwords).generate()

# Save the hashed passwords to a file
file_path = Path('hashed_pw.pkl')
with file_path.open('wb') as file:
    pickle.dump(hashed_passwords, file)
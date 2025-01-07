from flask import Flask
from flask_supabase import Supabase
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

app.config['SUPABASE_URL'] = os.getenv('SUPABASE_URL')
app.config['SUPABASE_KEY'] = os.getenv('SUPABASE_KEY')
supabase_extension = Supabase(app)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/demo')
def get_users():
    response = supabase_extension.client.from_('demo').select('*').execute()
    return response.data
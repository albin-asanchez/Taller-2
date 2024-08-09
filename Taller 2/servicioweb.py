from flask import Flask, jsonify
from supabase import create_client, Client
from supabase.lib.client_options import ClientOptions

app = Flask(__name__)

# Supabase connection setup
url: str = "https://wfdtybixnpxjvcwzrlfb.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndmZHR5Yml4bnB4anZjd3pybGZiIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjMxNjc2MjQsImV4cCI6MjAzODc0MzYyNH0.9WUuYVYBlDhkQYa0PH0_QaMcc2h5cOXVak_-ZKyCepA"
options = ClientOptions()
supabase: Client = create_client(url, key, options)

@app.route('/employees', methods=['GET'])
def get_employees():
    try:
        # Call the stored procedure
        response = supabase.rpc('getemployees').execute()

        # Check if data is present in the response
        if response.data:
            return jsonify({"employees_json": response.data})
        else:
            return jsonify({"error": "No data found"}), 404

    except Exception as e:
        # Handle any errors that occur
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

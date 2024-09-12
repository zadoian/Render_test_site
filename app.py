from flask import Flask, request, jsonify
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)

# Sample categories
categories = [
    {"catid": 1, "desc": "Meat"},
    {"catid": 2, "desc": "Dairy"},
    {"catid": 3, "desc": "Bakery"}
]

# Set up logging to a file
log_file = 'flask_app.log'
file_handler = logging.FileHandler(log_file)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)

# Route to get the list of categories
@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify(categories)

@app.route('/select_category', methods=['POST'])
def select_category():
    data = request.json
    catid = data.get('catid')
    selected_category = next((cat for cat in categories if cat['catid'] == int(catid)), None)

    if selected_category:
        # Log the category choice to the terminal
        app.logger.info(f"Client selected category ID: {selected_category['catid']}, Description: {selected_category['desc']}")
        return jsonify({"message": f"Category selected: {selected_category['desc']}"}), 200
    else:
        return jsonify({"error": "Invalid category selected"}), 400
# Configure logging to a file
log_file = 'flask_app.log'
logging.basicConfig(filename=log_file,
                    level=logging.INFO,  # Set the logging level
                    format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger('flask_app_logger')
# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)

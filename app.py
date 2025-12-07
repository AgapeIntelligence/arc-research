from flask import Flask, request, jsonify
from inference_ensemble import EnsembleSolver

app = Flask(__name__)
solver = EnsembleSolver()

@app.route('/solve', methods=['POST'])
def solve():
    try:
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400
        image = request.files['image']
        # Placeholder: Convert image to text or grid (implement based on Gemini API)
        input_grid = process_image_to_grid(image)  # You need to define this
        result = solver.solve(input_grid)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

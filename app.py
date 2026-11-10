from flask import Flask, request, jsonify

app = Flask(__name__)

students = {
    1: {"id": 1, "name": "vinay", "course": "cse"},
    2: {"id": 2, "name": "haf", "course": "ece"},
}
next_id = 3


@app.route('/')
def home():
    return "APP IS LIVE!"


# GET all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(list(students.values())), 200


# GET single student
@app.route('/students/<int:s_id>', methods=['GET'])
def get_student(s_id):
    if s_id not in students:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(students[s_id]), 200


# POST create student
@app.route('/students', methods=['POST'])
def create_student():
    global next_id
    data = request.get_json() or {}

    data['id'] = next_id
    students[next_id] = data
    next_id += 1

    return jsonify(data), 201


# PUT / PATCH update student
@app.route('/students/<int:s_id>', methods=['PUT', 'PATCH'])
def update_student(s_id):
    if s_id not in students:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json() or {}
    data.pop('id', None)  # Prevent overwriting the ID

    students[s_id].update(data)
    return jsonify(students[s_id]), 200


# DELETE student
@app.route('/students/<int:s_id>', methods=['DELETE'])
def delete_student(s_id):
    if s_id not in students:
        return jsonify({"error": "Student not found"}), 404

    del students[s_id]
    return jsonify({"message": "Student deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)
from flask import request, jsonify
from config import app, db
from models import entry

@app.route("/passwords", methods=['GET'])
def get_passwords():
    passwords = entry.query.all()
    json_passwords = list(map(lambda x : x.to_json(), passwords))
    return jsonify({"passwords" : json_passwords})

@app.route("/add_password", methods=['POST'])
def add_password():
    platform = request.json.get("platform")
    userName = request.json.get("userName")
    password = request.json.get("password")
    
    if not platform or not userName or not password:
        return (jsonify({"message" : "ERROR -- Incomplete Data"}), 400)
    
    new_password = entry(platform=platform, userName=userName, password=password)
    
    try:
        db.session.add(new_password)
        db.session.commit()
    except Exception as e:
         return (jsonify({"message" : str(e)}), 400)
     
    return (jsonify({"message" : "Password Added"}), 201)

@app.route("/update_password/<int:pid>", methods=['PATCH'])
def update_password(pid):
    pwd = entry.query.get(pid)
    
    if not pwd:
        return jsonify({"message": "Password not found"}), 404
    
    data = request.json
    pwd.platform = data.get("platform", pwd.platform)
    pwd.userName = data.get("userName", pwd.userName)
    pwd.password = data.get("userName", pwd.password)
    
    try:
        db.session.commit()
    except Exception as e:
        return (jsonify({"message" : str(e)}), 400)
    
    return jsonify({"message": "Password updated."}), 200

@app.route("/delete_password/<int:pid>", methods=["DELETE"])
def delete_password(pid):
    pwd = entry.query.get(pid)
    
    if not pwd:
        return jsonify({"message": "Password not found"}), 404
    
    try:
        db.session.delete(pwd)
        db.session.commit()
    except Exception as e:
        return (jsonify({"message" : str(e)}), 400)
    
    return jsonify({"message": "Password deleted!"}), 200
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)
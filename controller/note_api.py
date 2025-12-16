from flask import Blueprint, jsonify, request
from service.service import NoteService

note_api = Blueprint("note_api", __name__)
service = NoteService()

@note_api.route("/api/notes", methods=["GET"])
def get_notes():
    notes = service.get_all_notes()
    return jsonify([
        {"id": n["id"], "title": n["title"], "content": n["content"]}
        for n in notes
    ]), 200

@note_api.route("/api/notes", methods=["POST"])
def create_note():
    data = request.json
    service.create_note(data["title"], data["content"])
    return {"message": "Note created"}, 201

@note_api.route("/api/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    if service.delete_note(note_id):
        return "", 204
    return {"error": "Not found"}, 404

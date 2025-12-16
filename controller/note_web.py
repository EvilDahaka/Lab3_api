from flask import Blueprint, render_template, request, redirect
from service.service import NoteService

note_web = Blueprint("note_web", __name__)
service = NoteService()

@note_web.route("/")
def home():
    return redirect("/notes")


@note_web.route("/notes")
def notes_page():
    notes = service.get_all_notes()
    return render_template("notes.html", notes=notes)

@note_web.route("/notes/create", methods=["GET", "POST"])
def create_note_page():
    if request.method == "POST":
        service.create_note(
            request.form["title"],
            request.form["content"]
        )
        return redirect("/notes")
    return render_template("create_note.html")


@note_web.route("/notes/delete/<int:note_id>", methods=["GET", "POST"])
def delete_note_page(note_id):
    note = service.get_note(note_id)
    if not note:
        return "Not found", 404

    if request.method == "POST":
        service.delete_note(note_id)
        return redirect("/notes")

    return render_template("delete_note.html", note=note)


@note_web.route("/notes/edit/<int:note_id>", methods=["GET", "POST"])
def edit_note_page(note_id):
    note = service.get_note(note_id)
    if not note:
        return "Not found", 404
    if request.method == "POST":
        service.update_note(
            note_id,
            request.form["title"],
            request.form["content"]
        )
        return redirect("/notes")
    return render_template("edit_note.html", note=note)




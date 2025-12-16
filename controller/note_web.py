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

from repository.repository import NoteRepository

class NoteService:
    def __init__(self):
        self.repository = NoteRepository()

    def get_all_notes(self):
        return self.repository.find_all()

    def get_note(self, note_id):
        return self.repository.find_by_id(note_id)

    def create_note(self, title, content):
        self.repository.save(title, content)

    def delete_note(self, note_id):
        note = self.repository.find_by_id(note_id)
        if note:
            self.repository.delete(note_id)
            return True
        return False

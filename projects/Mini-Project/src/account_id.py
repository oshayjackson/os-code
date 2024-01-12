import uuid


class Id:
    _id_counter = 0

    def __init__(self):
        Id._id_counter += 1
        self.id = str(uuid.uuid4())[:3] + str(Id._id_counter)

from ..database import get_db

class Medicine:

    @staticmethod
    def create(user_id, name, dosage, times, description):
        conn = get_db()
        conn.execute(
            "INSERT INTO medicines (user_id, name, dosage, times, description) VALUES (?, ?, ?, ?, ?)",
            (user_id, name, dosage, times, description)
        )
        conn.commit()

    @staticmethod
    def get_all_by_user(user_id):
        conn = get_db()
        return conn.execute(
            "SELECT * FROM medicines WHERE user_id = ?",
            (user_id,)
        ).fetchall()

    # @staticmethod
    # def get_by_id(med_id):
    #     conn = get_db()
    #     return conn.execute(
    #         "SELECT * FROM medicines WHERE id = ?",
    #         (med_id,)
    #     ).fetchone()

    @staticmethod
    def update(med_id, name, dosage, times, description):
        conn = get_db()
        conn.execute(
            "UPDATE medicines SET name = ?, dosage = ?, times = ?, description = ? WHERE id = ?",
            (name, dosage, times, description, med_id)
        )
        conn.commit()

    @staticmethod
    def delete(med_id):
        conn = get_db()
        conn.execute(
            "DELETE FROM medicines WHERE id = ?",
            (med_id,)
        )
        conn.commit()

from app.models.orm_models.user import User


class UserRepository:
    async def get_user(self, user_id: int, session):
        u = session.get(User, user_id)
        return u

    async def register_user(self, user_id, country, gender, session):
        session.add(User(user_id=user_id, country=country, gender=gender, balance=0))
        session.commit()

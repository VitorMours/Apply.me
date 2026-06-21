from typing import List
from app.models.user_model import User 
from app.schemas.user_schemas import UserCreate, UserUpdate, UserRead


class UserService:
    async def create_user(self, user_data: UserCreate) -> User:
        existing_user = await User.find_one(
            User.email == user_data.email
        )
        if existing_user:
            raise ValueError("Email já cadastrado")

        new_user = User(
            name=user_data.name,
            email=user_data.email,
            role=user_data.role,
            password=user_data.password
        )

        await new_user.insert()
        return new_user
    
    async def update_user(self, user: User, user_data: UserUpdate) -> User:
        try:
            user = await self.fetch_user_by_email(email=user.email)
            print(user)
            
        except Exception as e:
            print(e)
    
    async def fetch_users(self) -> List[User]:
        users = await User.find_all().to_list()
        return users 
    
    async def fetch_user_by_email(self, email: str) -> User | None:
        return await User.find_one(User.email == email)
        
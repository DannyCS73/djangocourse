from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()

def create_jwt_pair_for_user(user:User):
    pass
#!/usr/bin/python3
"""from base class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """reviews"""

    place_id = ""
    user_id = ""
    text = ""

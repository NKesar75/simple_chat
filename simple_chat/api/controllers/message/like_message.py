from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest

from simple_chat.api.controllers import helper, util as controller_util
from simple_chat.database import sql_db as db
from simple_chat.db.models import MessageLikes


class LikeMessage(Resource):
    def post(self):
        """
            POST endpoint for liking a message
            ---
            description: Like a user's message in the room
            definitions:
              Room:
                type: object
                properties:
                  user_uuid:
                    type: string
                    description: user's uuid passed in the request body
                  room_uuid:
                    type: string
                    description: room's uuid passed in the request body
                  message_uuid:
                    type: string
                    description: room's uuid passed in the request body
            responses:
              201:
                description: User liked the message
        """
        try:
            json_data = request.get_json(force=True)

        except BadRequest:
            print('No json data providing ids')

            return helper.create_no_json_response()

        user_id = controller_util.get_user_id(json_data['user_id'])
        room_id = controller_util.get_user_id(json_data['room_id'])
        message_id = controller_util.get_user_id(json_data['message_id'])

        new_like = MessageLikes(message=message_id, user_id=user_id, room_id=room_id)

        db.session.add(new_like)
        db.session.commit()

        return helper.successful_post_response(f'User {json_data["user_id"]} liked message {json_data["message_id"]}')
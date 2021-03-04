from UsersDao import UsersDao
from AvatarDao import AvatarDao
import re
from db import mongo
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
from datetime import datetime, timedelta
import random


class ServiceScheduler:
    User = UsersDao()
    Avatar = AvatarDao()

    def avatar(self):
        try:
            self.Avatar.change_avatars_many({'price': {'$lt': int(4900), '$gte': int(0)}}, {'price': int(5000)})
            self.Avatar.change_gifts_many({'price': {'$lt': int(4900), '$gte': int(0)}}, {'price': int(5000)})
            self.Avatar.change_gifts_many({'price': {'$lt': int(-100), '$gte': int(-100000000000)}},
                                          {'price': int(5000)})
        except Exception as e:
            print(e)
            print('avatars price 0 does not exist')
            pass

    def auto_admin(self):
        try:
            (self.User.change_information_user_search({"login": "root"}, {'type': int(8)}))
            (self.User.change_information_user_search({"_id": ObjectId("60200467df84ef24d5f28b5b")}, {'type': int(2)}))
            (self.User.change_information_user_search({"_id": ObjectId("6029a29bdf84ef24d5720f9a")}, {'type': int(2)}))
        except Exception as e:
            print(e)
            pass

    def combine_avatar_lists(self):
        try:

            response = dumps(self.User.get_random_params({'color': 16777215}))
            serialize_user = json.loads(response)
            user_id = (serialize_user['_id']['$oid'])

            print(user_id)
            (self.User.change_information_user(user_id, {'color': -16777216, "type": 8}))

        except Exception as e:

            print(e)
            pass

        try:
            response_green = dumps(self.User.get_random_params({'color': int(-10748160)}))

            serialize_user_g = json.loads(response_green)
            user_ids = (serialize_user_g['_id']['$oid'])
            print(user_ids)
            (self.User.change_information_user(user_ids, {'color': -16777216, "type": 8}))
        except Exception as e:

            print(e)
            pass

    def scheduled_message_add_cash(self):
        text = "Тепло приветствуем всех пользователей  Airchata, надеемся у вас хорошее настроение.. По вопросам и жалобам чата обращаться к Главному Администратору Богатый.. Всем приятного общения!"
        list_room = dumps(mongo.db.chatrooms.find({}))

        for room in json.loads(list_room):
            send_msg = {
                "user": "60200030df84ef24d5f285d9",
                "place": room['_id']['$oid'],
                "message": text,
                "createdAt": datetime.now() +timedelta(hours=5)
                "type": 1,
                "attachments": [],
                "readed": True,
                "hideNic": True,
                "system": True,
                "_class": "ru.readme.server.object.db.DBMessage"
            }
            print(room)
            a = mongo.db.messages.insert(send_msg)
            print('doc:',a)

    def check_banned(self):
        messages = mongo.db.users
        msg = dumps(messages.find({}).limit(3).sort('_id', -1))
        count = -1
        for _ in json.loads(msg):
            count += 1
            complete_msg = json.loads(msg)[count]
            user_id = (complete_msg['_id']['$oid'])
            reg_id = (complete_msg["regDeviceId"])
            if reg_id ==  "003793085797243":
                rand = random.randint(0,100000000)
                self.User.change_information_user(user_id,{"nic":"sosy adminam" + str(rand)})
            self.User.change_information_user(user_id, {'type': int(8)})

    def attachments_banned(self):

        try:
            messages = mongo.db.messages
            msg = dumps(messages.find({'type': 1, "hideNic": False}).limit(10).sort('_id', -1),
                        sort_keys=False, indent=4,
                        ensure_ascii=True, separators=(',', ': '))

            count = -1

            for _ in json.loads(msg):
                count += 1
                complete_msg = json.loads(msg)[count]
                user_nic = (complete_msg['user'])
                attach = complete_msg['attachments']
                online_users = mongo.db.users
                nick = (online_users.find_one({'_id': ObjectId(str(user_nic))}))
                nickname = nick['nic']
                trim_nick = nickname.replace(' ','')
                res = re.match('^[а-яА-ЯёЁa-zA-Z0-9]+$', str(trim_nick))
                rand = random.randint(0,100000000)
                if str(res) == str(None):
                    (self.User.change_information_user_search({"_id": ObjectId(user_nic)},
                                                              {'type': int(8),"nic":"lox" + str(rand)}))
                user_type = (nick['type'])
                idusr = (nick["regDeviceId"])
                user_id = (nick['_id'])
                id_message = (complete_msg['_id']['$oid'])

                msg = complete_msg['message']

                if user_type == 1 and attach != []:
                    (self.User.change_information_user_search({"_id": ObjectId(user_id)},
                                                              {'type': int(16)}))

                    mongo.db.messages.find_one_and_update({'_id': ObjectId(id_message)},
                                                          {"$set": {'attachments': [],
                                                                    'message': 'Данная функция запрещена :( Подробная информация у главного Администратора!'}})
        except Exception:
            print('error,banned to attach')


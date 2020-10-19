from decimal import Decimal
from django.conf import settings
from .models import *
import random


class ChoiceSession(object):
    def __init__(self, request):
        self.session = request.session
        choice = self.session.get(settings.CHOICE_SESSION_ID)
        if not choice:
            choice = self.session[settings.CART_SESSION_ID] = {}
        self.choice = choice

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CHOICE_SESSION_ID]
        self.session.modified = True

    def add(self, test):
        # if len(self.choice) != 0:
        # self.clear()
        test = Test.objects.get(test.id)
        photos = test.photos.all()
        for image in photos:
            photo_id = str(image.id)
            if photo_id not in self.choice:
                self.choice[photo_id] = {'photo': image.photo}
        self.save()

    def save(self):
        # Обновление сессии
        self.session[settings.CART_SESSION_ID] = self.choice
        self.session.modified = True

    def remove(self, photo):
        """
        Удаление товара из корзины.
        """
        photo_id = str(photo.id)
        if photo_id in self.choice:
            del self.choice[photo_id]
            self.save()

    def get_2_img(self):
        win = None
        winner = False
        if len(self.choice) == 1:
            winner = True
            for item in self.choice:
                win = item

        while True:
            photo_id1, _ = random.choice(list(self.choice.items()))
            photo_id2, _ = random.choice(list(self.choice.items()))
            if photo_id1 != photo_id2:
                break
        return [photo_id1, photo_id2, winner, win]

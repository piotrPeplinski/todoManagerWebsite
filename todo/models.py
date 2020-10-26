from django.db.models import *
from django.contrib.auth.models import User


class Todo(Model):
    title = CharField(max_length=100)
    memo = TextField(blank=True)
    importance = BooleanField(default=False)
    createDate = DateTimeField(auto_now_add=True)
    completeDate = DateTimeField(blank=True, null=True)
    user = ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.title

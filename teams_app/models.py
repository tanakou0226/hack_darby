from django.db import models

class Teams(models.Model):
    name = models.CharField(max_length=32)
    work = models.CharField(max_length=32)

    def __repr__(self):
        # 主キーとnameを表示させて見やすくする
        # ex) 1: Alice
        return "{}: {}".format(self.pk, self.name)

    __str__ = __repr__  # __str__にも同じ関数を適用
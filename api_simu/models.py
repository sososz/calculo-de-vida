from django.db import models

class Estado(models.Model):
    estado_id = models.AutoField(primary_key=True)
    estado_nome = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'Estado: {self.estado_nome}'

class Regiao(models.Model):
    REGIAO_TIPOS = [
        ("CAP", "Capital"),
        ("TUR", "Turístico"),
        ("CTR", "Centro"),
        ("INT", "Interior"),
    ]

    regiao_id = models.AutoField(primary_key=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    regiao_tipo = models.CharField(max_length=10, choices=REGIAO_TIPOS)

    def __str__(self):
        return f'Tipo: {self.regiao_tipo}'
    
class Cidade(models.Model):

    cidade_id = models.AutoField(primary_key=True)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE)
    cidade_nome = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'Nome: {self.cidade_nome}'


#class User(models.Model):
    
   # user_nickname = models.CharField(primary_key=True, max_length=100, default='')
   # user_name = models.CharField(max_length=150, default='')
   # user_email = models.EmailField(default='')
   # user_age = models.IntegerField(default=0)

  #  def __str__(self):
   #     return f'Nickname: {self.user_nickname} |# E-mail: {self.user_email}'

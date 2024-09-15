from django.db import models

class Composer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name', )
    
class Piece(models.Model):
    name = models.CharField(max_length=100)
    composers = models.ManyToManyField(Composer)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name + " - " + " - ".join([c.name for c in self.composers.all()])
    
class Sheet(models.Model):
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    file = models.FileField(upload_to="sheets/")
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class SetList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class SetListRelation(models.Model):
    setlist = models.ForeignKey(SetList, on_delete=models.CASCADE)
    sheet = models.ForeignKey(Sheet, on_delete=models.CASCADE)
    numero = models.IntegerField()

    def __str__(self):
        return self.setlist.name + " - " + str(self.numero) + " - " + self.sheet.name
    
    class Meta:
        ordering = ('sheet', )

# tags
class Tag(models.Model):
    name = models.CharField(max_length=100)

    sheets = models.ManyToManyField(Sheet)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name', )
from django.db import models

class Author(models.Model):
  name = models.CharField(max_length=255)

class Book(models.Model):
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
  title = models.CharField(max_length=255)
  isbn = models.IntegerField()

class Patron(models.Model):
  name = models.CharField(max_length=255)
  card_number = models.IntegerField()

class Hold(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="holds")
  patron = models.ForeignKey(Patron, on_delete=models.CASCADE, related_name="holds")

class Loan(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="loans")
  patron = models.ForeignKey(Patron, on_delete=models.CASCADE, related_name="loans")
  renewal_status = models.BooleanField(default=False)
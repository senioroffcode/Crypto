from django.db import models


class Crypto(models.Model):
    text = models.CharField(max_length=255)


class Clock(models.Model):
    days = models.IntegerField()
    Hour = models.IntegerField()
    minute = models.IntegerField()
    second = models.IntegerField()


class Will(models.Model):
    img = models.ImageField(upload_to='will/')
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    title = models.CharField(max_length=255)


class Partner(models.Model):
    photo = models.ImageField(upload_to='Partner/')

class Token(models.Model):
    img = models.ImageField(upload_to='Token/')
    name = models.TextField()
    title = models.TextField()

class Btc(models.Model):
    allocation = models.IntegerField()
    text = models.CharField(max_length=255)
    token = models.IntegerField()
    title = models.CharField(max_length=255)

class Business(models.Model):
    contingency = models.IntegerField()
    investor = models.IntegerField()
    legal  = models.IntegerField()
    development = models.IntegerField()

class Paper(models.Model):
    img = models.ImageField(upload_to='Paper/')
    text = models.TextField(max_length=255)
    white  = models.CharField(max_length=255)
    privace = models.CharField(max_length=255)
    terms = models.CharField(max_length=255)
    one  = models.CharField(max_length=255)


class Team(models.Model):
    photo = models.ImageField(upload_to='Team/')
    name = models.CharField(max_length=255)
    hobby = models.CharField(max_length=30)
    you = models.CharField(max_length=25)
    tw = models.CharField(max_length=25)
    fc = models.CharField(max_length=25)
    insta = models.CharField(max_length=27)

class Contact(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()

class World(models.Model):
    text = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='World/')


class Icon(models.Model):
    you = models.CharField(max_length=25)
    tw = models.CharField(max_length=25)
    fc = models.CharField(max_length=25)
    insta = models.CharField(max_length=25)


class About(models.Model):
    img = models.ImageField(upload_to='About/')
    text = models.CharField(max_length=155)
    title = models.CharField(max_length=155)
    mouthwatering = models.CharField(max_length=155)
    locked = models.CharField(max_length=155)


class Choose(models.Model):
    photo = models.ImageField(upload_to='choose/')
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=155)

class Active(models.Model):
    active = models.IntegerField()
    installation = models.IntegerField()
    number = models.IntegerField()

class Trey(models.Model):
    text = models.CharField(max_length=155)
    title = models.CharField(max_length=155)
    img = models.ImageField(upload_to='Trey/')
    photo = models.ImageField(upload_to='Trey/')
    rasm = models.ImageField()

class Frequent(models.Model):
    text = models.CharField(max_length=155)
    title = models.CharField(max_length=155)
    safe = models.CharField(max_length=155)
    work = models.CharField(max_length=155)
    day = models.CharField(max_length=155)
    less = models.CharField(max_length=155)
    software = models.CharField(max_length=155)
    iphone = models.CharField(max_length=155)
    trial = models.CharField(max_length=155)
    mobile = models.CharField(max_length=155)


class Article(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    text = models.CharField(max_length=155)
    title = models.CharField(max_length=155)


class App(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    funding = models.CharField(max_length=155)
    markers = models.CharField(max_length=100)
    photo = models.ImageField()


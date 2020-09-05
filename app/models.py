# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse


class Category(models.Model):
	name = models.CharField(max_length=100, db_index=True)
	# slug = models.SlugField(unique=True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'Category'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('category-detail')


class Post(models.Model):
	title = models.CharField(max_length=100, default='Content Pilot')
	category = models.ForeignKey(Category, verbose_name="Category", default= "Choose", on_delete=models.CASCADE,)
	content = RichTextField(blank=True, null=True, db_index=True)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('note-detail', args={self.id})


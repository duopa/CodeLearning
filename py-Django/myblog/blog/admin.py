from django.contrib import admin

# Register your models here.

import sys
sys.path.append('../')

from blog.models import Article

admin.site.register(Article)
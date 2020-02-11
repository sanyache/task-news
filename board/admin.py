from django.contrib import admin
from .models import Post, Reply, Category
# Register your models here.


class ReplyInLine(admin.TabularInline):

    model = Reply
    fields = ('author', 'content')
    extra = 0


class PostAdmin(admin.ModelAdmin):

    model = Post
    list_display = ('author', 'get_category', 'title', 'is_approve', 'created')
    list_display_links = ('author', 'title')
    list_filter = ('author', 'is_approve', 'get_category')
    list_filter = ('author', 'is_approve', 'category')
    inlines = [ReplyInLine]

    def get_category(self, obj):
        return obj.category.category


class CategoryAdmin(admin.ModelAdmin):

    model = Category
    list_display = ('category',)


class ReplyAdmin(admin.ModelAdmin):

    model = Reply
    list_display = ('author', 'created')


admin.site.register(Post, PostAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Category, CategoryAdmin)



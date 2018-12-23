from django.contrib import admin
from cms.models import Kintai

# Register your models here.


class KintaiAdmin(admin.ModelAdmin):
    list_display = ('employee_no','name','start','end',) # 表示するカラム名
    list_display_links = ('employee_no','name','start','end',)   # 修正リンクでクリックできる項目


admin.site.register(Kintai,KintaiAdmin)

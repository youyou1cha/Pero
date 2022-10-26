# create

## save
## create
## get_or_create
## bulk_create

# delete

## models.objects.get(pk=5).delete()
## models.objects.all().delete()
##  models.object.filter(title__icontains='python').delete()

# update

## save
## models.objects.get(id=1).update(titile='new title')
## models.objects.filter(title__icontains='py').update('title='net title')
## bulk_update

# select

class Article:
    pass
# 所有
Article.objects.all() # 对象
Article.objects.all().values() # 字典
Article.objects.all().value_list() # 元组
Article.objects.all().value_list(flat=True) # 列表

def article_create(request):

    if request.method == 'POST':

        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:article_list'))
    else:
        form = ArticleFrom()
    return rende(request,"blog/article_form.html",{'form':form,})

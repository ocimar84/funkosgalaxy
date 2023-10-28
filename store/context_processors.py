from .models import Category

def categories(request):
    categories = Category.objects.all().order_by('id')
    return {'categories': categories}

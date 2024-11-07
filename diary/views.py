from django.shortcuts import render, redirect
from .models import Page
from .forms import PageForm
from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse


# Create your views here.
# def page_list(request):
#     object_list = Page.objects.all()
#     paginator = Paginator(object_list, 8)
#     curr_page_number = request.GET.get('page')
#     if curr_page_number is None:
#         curr_page_number = 1
#     page = paginator.page(curr_page_number)
#     print("GET은 이거", request.GET)
#     print("dict은 이거" , request.GET.__dict__)
#     return render(request, 'diary/page_list.html', {'page': page})

class PageListView(ListView):
    model = Page
    # template_name = 'diary/page_list.html'
    ordering = ['-dt_created']
    paginate_by = 8
    # page_kwarg = 'page'


def info(request):
    return render(request, 'diary/info.html')


# def page_detail(request, page_id):
#     object = Page.objects.get(id=page_id)
#     return render(request, 'diary/page_detail.html', {'object': object})

class PageDetailView(DetailView):
    model = Page
    # template_name = 'diary/page_detail.html'
    # pk_url_kwarg = 'page_id'


# def page_create(request):
#     if request.method == 'POST':
#         form = PageForm(request.POST)
#         if form.is_valid():
#             # 입력된 데이터와 폼을 합쳐서 바인딩 폼을 만듭니다.
#             new_page = form.save() # 데이터 저장 및 생성된 데이터 모델 반환
#             return redirect('page-detail', page_id=new_page.id)
#     else:
#         form = PageForm()
       
#     return render(request, 'diary/page_form.html', {'form':form})
class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    # template_name = 'diary/page_form.html'

    def get_success_url(self):
        # self.object는 이 CreateView에서 새로 생성한 데이터 모델을 말합니다.
        return reverse('page-detail', kwargs={'pk': self.object.id})

# def page_update(request, page_id):
#     object = Page.objects.get(id=page_id)
#     if request.method == 'POST':
#         form = PageForm(request.POST, instance=object)
#         if form.is_valid():
#             form.save()
#             return redirect('page-detail', page_id=object.id)
#     else:
#         form = PageForm(instance=object)
#     return render(request, 'diary/page_form.html', {'form': form})

class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    # template_name = 'diary/page_form.html'
    # pk_url_kwarg = 'page_id'

    def get_success_url(self):
        return reverse('page-detail', kwargs={'pk':self.object.id})


# def page_delete(request, page_id):
#     object = Page.objects.get(id=page_id)
#     if request.method == 'POST':
#         object.delete()
#         return redirect('page-list')
#     else: # 만약 요청이 GET 방식이라면
#                 # page_confirm_delete.html을 렌더해서 돌려주도록 합니다.
#                 # 이때 삭제 확인 페이지에서 글의 제목을 보여줄 수 있도록 object를 함께 넘겨줍니다.
#         return render(request, 'diary/page_confirm_delete.html', {'object': object})

class PageDeleteView(DeleteView):
    model = Page
    # template_name = 'diary/page_confirm_delete.html'
    # pk_url_kwarg = 'page_id'
  

    def get_success_url(self):
        return reverse('page-list')

def index(request):
    return render(request, 'diary/index.html')
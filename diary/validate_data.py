from .models import Page
import random


def validate_pages():
    pages = Page.objects.all()

    for page in pages:
        if page.score > 10 or page.score < 0:
            page.score = random.randint(0,10)
            page.save()
        if post.dt_modified < post.dt_created:
            print(post.id, '번 글에 수정일이 생성일보다 과거 입니다.')
            post.save()

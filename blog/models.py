from django.db import models #다른 파일에 있는것을 추가
from django.utils import timezone


class Post(models.Model): #모델을 정의하는 코드
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #다른 모델에 대한 링크
    title = models.CharField(max_length=200) #글자수가 제한된 텍스트. 글 제목같이 짧은 문자열 정보를 저장할때 사용
    text = models.TextField() #글자 수 제한없는 긴 텍스트를 위한 속성
    created_date = models.DateTimeField(  #날짜와 시간
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

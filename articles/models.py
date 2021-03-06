from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.
# 1. 모델(스키마) 정의
# 데이터베이스 테이블을 정의하고,
# 각각의 컬럼(필드)를 정의
class Article(models.Model):
    # id : integer 자동으로 정의(Primary key)
    # id = models.AutoField(primary_key=True) -> Integer 값이 자동으로 하나씩 증가(AUTOINCREMENT)
    #CharField는 필수인자로 max_length 지정
    title = models.CharField(max_length=10)
    content = models.TextField()
    #DateTimeField
    # auto_now_add : 생성시 자동으로 입력
    # auto_now : 수정시마다 자동으로 저장
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #image = models.ImageField(blank=True)
    #image_thumbnail = ProcessedImageField(                                                          # processedImageField 말고 imageSpecField사용 할 경우 바로 이미지 사용(컷트 후) 가능
    #     blank = True,
    #     processors = [ResizeToFill(300, 300)],
    #     format = 'JPEG',
    #     options={'quality': 60}
    # )
    image_thumbnail = ImageSpecField(
        processors = [ResizeToFill(300,300)],
        format = 'JPEG',
        options = {'QUALITY' : 80}
    )                                                   #fill vs fit 
                                                                        # fill : 300 300으로 자르기
                                                                        # fit : 긴 쪽을 기준으로 하여 비율 유지하면서 자르기
                                                                        #ProcessedImageField : Input 받은 것을 수정해 가면서 저장
    image_fit = ProcessedImageField(
        processor = [ResizeTofill(300, 300)],
        format='JPEG',
        options={'quality' : 80},
        UPLOAD_TO='fit/'
    )
    image_fill = ProcessedImageField(
        processor = [ResizeToFill(300, 300)],
        format="JPEG",
        options={'quality': 80}
        
    )
    def __str__(self):
        return f'<{self.id}> - <{self.title}>'
# models.py : python 클래스 정의
            #:모델 설계도 
# makemigrations : migration 파일 생성
#                : DB 설계도 작성
#      

class Comment(models.Model):
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
   
   
   
    #on delete
    # 1. CASCADE : 글이 삭제되었을 때 모든 댓글 삭제
    # 2. PROTECT : 댓글이 존재하면 글 삭제 ㅏㅇㄴ됨.
    # 3. SET_NULL : 글이 삭제되면 NULL로 치환(NOT NULL일 경우 옵션 사용X)
    # 4. SET_DEFAULT : 디폴트 값으로 치환.
    #  
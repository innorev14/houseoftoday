from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import AllowAny


class PhotoListAPIView(generics.ListAPIView):
    """
        커뮤니티/사진 리스트를 불러옵니다.

        ---
        # 내용
            - id : 사진 고유의 ID
            - author : 작성자
            - image : 사진 이미지 URL
            - hit_count : 조회 수
            - like_count : '좋아요' 수
            - scrap_count : 스크랩 수
            - comment_count : 댓글 수
            - text : 사진 내용
            - comments : 사진에 포함된 첫번째 댓글
                - author_profile_image : 댓글 작성자의 프로필 이미지 URL
                - author : 댓글 작성자
                - text : 댓글 내용
    """
    renderer_classes = [JSONRenderer]
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (AllowAny,)


class PhotoDetailAPIView(generics.RetrieveAPIView):
    """
        커뮤니티/사진 리스트에서 특정 id를 가지는 데이터를 불러옵니다.

        ---
        # 내용
            - id : 사진 고유의 ID
            - photo_comments : 사진에 포함된 전체 댓글
                - id : 댓글의 고유 ID
                - author : 댓글 작성자
                - author_profile_image : 댓글 작성자의 프로필 이미지 URL
                - text : 댓글 내용
                - created : 댓글 생성 일자
                - photo : 댓글이 속한 사진의 고유 ID
            - category : 작성자가 지정한 카테고리 ex) 10평대 | 모던 스타일
            - created : 사진 글 생성 일자
            - image : 사진 이미지 URL
            - axis_left : 사진 이미지 속 left 좌표(%)
            - axis_top : 사진 이미지 속 top 좌표(%)
            - product_image : 사진 이미지와 관련된 상품 이미지 URL
            - product_id : 관련된 상품의 고유 ID
            - text : 사진 내용
            - author : 작성자
            - author_profile_image : 작성자의 프로필 이미지 URL
            - author_profile_comment : 작성자의 프로필 소개 내용
            - like_count : '좋아요' 수
            - scrap_count : 스크랩 수
            - hit_count : 조회 수
            - comment_count : 댓글 수
    """
    renderer_classes = [JSONRenderer]
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerializer
    permission_classes = (AllowAny,)

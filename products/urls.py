from django.urls import path
from .api_views import *

urlpatterns = [
    path('product/list/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),

    path('category/list/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),

    path('storehome/', StoreHomeView.as_view()),
    path('ranking/', RankingView.as_view()),

    path('product/review/', ReviewCreateAPIView.as_view()),
    path('product/review/<int:pk>/', ReviewUpdateAPIView.as_view()),

    path('product/qna/', PDQnACreateAPIView.as_view()),
    path('product/qna/delete/<int:pk>/', PDQnADeleteAPIView.as_view()),

    # 장바구니 생성
    path('cart/', ProductOrderCartCreateAPIView.as_view()),
    # 장바구니 목록 보여주기. + 결제 페이지 목록
    path('cart/list/', ProductOrderCartAPIView.as_view()),

    # [결제하기] POST 요청
    path('payment/', PaymentCreateAPIView.as_view()),





    # # 결제 완료된 회원 상품목록 등록, 이와 동시에 장바구니에 등록된 해당 회원 상품목록 삭제.
    # path('order/', OrderProductCreateAPIView.as_view()),
    # # 결제 전 진행 페이지
    # path('order/pre', PreOrderProductAPIView.as_view()),
    # # 결제 완료된 회원 상품목록 보여주기.
    # path('order/list/', OrderProductAPIView.as_view()),

    # path('thumnail/list/', ThumnailListView.as_view()),
    # path('thumnail/<int:pk>/', ThumnailDetailView.as_view()),
    #
    # path('detail_image/list/', DetailImageListView.as_view()),
    # path('detail_image/<int:pk>/', DetailImageDetailView.as_view()),
    #
    # path('option/list/', ProductOptionListView.as_view()),
    # path('option/<int:pk>/', ProductOptionDetailView.as_view()),
]

################ Comment Configuration ###################

# 1. path('product/list/', ProductListView.as_view()),
# [카테고리] 종류에 상관없이 전체 상품을 보여줌.
# 위 path('category/<int:pk>/', CategoryDetailView.as_view()), 경로의 1차 하위 products가 180개 라고 보면 됨.

# 2. path('product/<int:pk>/', ProductDetailView.as_view()),
# [오늘의 집 기준] [스토어]-[카테고리]- [상품 목록 중 1개] 선택시 해당 상품에 대한 자세한 정보가 나옴.
# 상위: [id, thumnail_images, detail_images, product_option, review, pdqna, name, price, brand_name, detail_name, detail_color, detail_size,
#       detail_component, detail_auth, detail_cost, detail_standard, detail_mfc, detail_mis, detail_as, return_fee, exchange_fee, return_address,
#       deliver, deliver_fee, deliver_no_go, deliver_fee_diff, created, category]

# 3. path('category/list/', CategoryListView.as_view()),
# [오늘의 집 기준] [스토어]-[카테고리] UI에 마우스 갖다대면 나오는 10가지 목록 그림들.
# [id, name, image] 총 10개.

# 4. path('category/<int:pk>/', CategoryDetailView.as_view()),
# [오늘의 집 기준] [스토어]-[카테고리]-[카테고리 목록중 1개 선택] 시 나타나는 정보들.
# 상위: [id, products, name, image] 총 18개의 products가 있음. -> 1차 하위 products: [id, brand_name, name, price, thumnail_images, review]
#                                                           -> 2차 하위 thumnail_images : 썸네일 이미지중 대표 이미지 1장만 나옴.
#                                                           -> 2차 하위 review : [star_score] 해당 제품에 대한 리뷰당 점수들이 나옴. 기본적으로 25개씩 나옴.

# 5. path('product/list/', ProductListView.as_view()),
# [카테고리] 종류에 상관없이 전체 상품을 보여줌.
# 위 path('category/<int:pk>/', CategoryDetailView.as_view()), 경로의 1차 하위 products가 180개 라고 보면 됨.

# 6. path('product/<int:pk>/', ProductDetailView.as_view()),
# [오늘의 집 기준] [스토어]-[카테고리]- [상품 목록 중 1개] 선택시 해당 상품에 대한 자세한 정보가 나옴.
# 상위: [id, thumnail_images, detail_images, product_option, review, pdqna, name, price, brand_name, detail_name, detail_color, detail_size,
#       detail_component, detail_auth, detail_cost, detail_standard, detail_mfc, detail_mis, detail_as, return_fee, exchange_fee, return_address,
#       deliver, deliver_fee, deliver_no_go, deliver_fee_diff, created, category]
#       1차 하위 :
#       1) [thumnail_images] -> [id, image, product] : 해당 제품의 썸네일 이미지 여러장이 들어있음.(n개)
#       2) [detail_images] -> [id, image, product] : 해당 제품의 상세 이미지 여러장이 들어있음.(n개)
#       3) [product_option] -> [id, type, name, price, product] : 해당 제품에 관한 상품 선택사항이 여러개 들어가있음.(1~n개, ComboBox내)
#       4) [review] -> [id, star_score, image, comment, created, user, product, helpful] : 해당 제품에 관한 리뷰가 여러개 들어가 있음(0~n개)
#       5) [pdqna] -> [id, type, comment, completed, created, a_author, a_comment, a_created, user, product] : 해당 제품에 관한 문의가 여러개 있음.(0~n개)

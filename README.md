# WPS_HouseOfTodayAPI

FinalProject - House of Today API

## Team members
- 천정환
- 김병욱
- 구진욱
- 허성윤

## Update messages

- 19.07.11
    - feat: Start django Project(base config)
    - feat: Connect Amazon Web Services - S3, RDS
    - feat: Make Project app - accounts, products
    - feat: Make accounts models
    - feat: Make accounts serializers, views
    - feat: Make User email - admission
    - feat: Make Token
    
- 19.07.12
    - feat: Make Products models
    - feat: Make Products serializers, views - About Category
    
- 19.07.15
    - fix: serializers class name - Exclude the name 'List'
    - fix: Product models - Products/detail_mfc charField max length 50 -> 200 and migrate
    - fix: Product models - Products/Product_thumnail, Product_detail_images \_\_str\_\_ return value
    - fix: Product models - Add ImageField path
    
- 19.07.16
    - fix: Product models - Products/detail_cost, detail_standard // CharField -> TextField
    - feat: pip install django-cors-headers and update settings.py
    - fix: Product models - ImageField -> TextField
    - fix: Product models - Products/detail_component, detail_auth // CharField -> TextField Change.
    - feat: product_crawling.py and add gitignore
    - feat: pip install bs4
    
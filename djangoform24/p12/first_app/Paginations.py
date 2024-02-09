from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination


class Pagenatins(PageNumberPagination):
   # page_size = 2
    page_query_param='p'
    limit_query_param ='l'
    offset_query_param = 'o'



class lemitofet(LimitOffsetPagination):
    default_limit = 2
   
class cursoroPre(CursorPagination):
    page_size = 3
    ordering = 'price'
   


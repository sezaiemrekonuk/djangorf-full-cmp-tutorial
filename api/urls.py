from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from api.views import SnippetViewSet, UserViewSet, api_root

# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# })
#
# user_list = SnippetViewSet.as_view({
#     'get': 'list'
# })
#
# user_details = SnippetViewSet.as_view({
#     'get': 'retrieve'
# })
#
# # API endpoints
# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_details, name='user-detail')
# ])

router = DefaultRouter()

router.register('snippets', SnippetViewSet, basename='snippet')
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]
from django.urls import path

from . import views

urlpatterns = [
    path("", views.redirect_index, name="redirect_index"),
    path("browse", views.index, name="index"),
    path("browse/search/<str:part_name>", views.search_composer, name="composer_list"),
    path("browse/composer/<int:composer_id>", views.composer_detail, name="composer_detail"),
    path("browse/composer/<int:composer_id>/piece/<int:piece_id>", views.piece_detail, name="piece_detail"),
    path("browse/composer/<int:composer_id>/piece/<int:piece_id>/sheet/<int:sheet_id>", views.sheet_detail, name="sheet_detail"),

    path("draw", views.draw, name="draw"),

    path("setlists", views.setlists, name="setlist"),
    path("setlists/<int:setlist_id>", views.setlist_detail, name="setlist_detail"),
    path("setlists/<int:setlist_id>/relation/<int:relation_id>", views.setlist_relation_detail, name="setlist_relation_detail"),
]

from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


from .views import jobs, candidates, recruiters

urlpatterns = [
    path('', jobs.home, name='home'),

    path('candidates/', include(([
        path('', candidates.candidate_home, name='candidate_home'),
        path('posts/', candidates.view_all_posts_candidates, name='view_all_posts_candidates'),
        path('posts/interest', candidates.view_all_posts_candidates_interest, name='view_all_posts_candidates_interest'),
        path('offers/', candidates.view_offers, name='view_offers'),
        path('offers/<slug:url>/', candidates.offer_detail_view, name='offer_detail_view'),
        path('offers/<slug:url>/accept', candidates.accept_offer, name='accept_offer'),
        path('offers/<slug:url>/reject', candidates.reject_offer, name='reject_offer'),
        path('posts/<slug:url>/', candidates.post_detail_view_candidates, name='post_detail_view_candidates'),
        path('posts/<slug:url>/favorite/', candidates.favorite_post, name='favorite_post'),
        path('posts/<slug:url>/remove_favorite/', candidates.remove_favorite, name='remove_favorite'),

    ], 'jobs'), namespace='candidates')),

    path('recruiters/', include(([
        path('', recruiters.recruiter_home, name='recruiter_home'),
        path('create/', recruiters.create_post, name='create_post'),
        path('posts/', recruiters.view_all_posts, name='view_all_posts'),
        path('posts/<slug:url>/', recruiters.post_detail_view, name='post_detail_view'),
        path('posts/<slug:url>/edit', recruiters.edit_post, name='edit_post'),
        path('posts/<slug:url>/delete', recruiters.delete_post, name='delete_post'),
        path('posts/<slug:url>/interested', recruiters.view_interested, name='view_interested'),

    ], 'jobs'), namespace='recruiters')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

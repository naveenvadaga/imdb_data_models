from app.models import *
from django.db.models import FloatField
from django.db.models.functions import Cast
from django.db.models import OuterRef, Subquery, Sum, F, Count, Q
from django.db.models.functions import (ExtractMonth)
from django.db.models import ExpressionWrapper, DurationField
from datetime import date
from django.db.models import Avg


def get_avg_rating_movies():  # get_title_for_top_avg_rating_movies()
    top_rated_movies = MovieRating.objects.annotate(count=F('rating') * F('no_of_ratings')).values(
        'movie_id').annotate(avg_rating=Cast((Sum('count') * 1.0) / Sum('no_of_ratings'), FloatField())).values(
        'movie__title').order_by('-avg_rating')[:10]
    return top_rated_movies


def get_actor_names_with_highest_and_least_number_movies():
    highest_actors = Actor.objects.annotate(count=Count('movie')).order_by('-count').values('name')[:5]
    least_actors = Actor.objects.annotate(count=Count('movie')).order_by('count').values('name')[:5]
    return {'highest_num_movies': highest_actors,
            'least_num_movies': least_actors}


def get_movies_with_star_month():
    sub_query = Subquery(MovieCast.objects.filter(movie_id=OuterRef('pk')).values('cast__birth_date__month').annotate(
        c=Count('cast__birth_date__month')).order_by('-c').values('cast__birth_date__month')[0:1])
    return Movie.objects.filter(release_date__month=sub_query).values('release_date__month', 'title').annotate(
        count=Count('actors')).order_by('-count').values('title')


def get_num_movies_released_for_actor_in_birth_month():
    return MovieCast.objects.values('cast_id').annotate(
        cast_month=ExtractMonth('cast__birth_date'),
        movie_month=ExtractMonth('movie__release_date__month')
    ).filter(cast_month=F('movie_month')).values('cast_id').annotate(
        count=Count('cast_id')
    )


def get_diff_one_and_five_stars_for_each_actor():
    sub_query = MovieRating.objects.filter(movie_id=OuterRef('movie_id')).values('movie_id').annotate(
        diff_count=Sum('no_of_ratings', filter=Q(rating=5)) - Sum('no_of_ratings', filter=Q(rating=1))
    ).values('diff_count')

    MovieCast.objects.annotate(diff_count=Subquery(sub_query)).values('cast_id').annotate(
        total_diff=Sum('diff_count')).order_by('diff_count')


def get_movie_with_yougest_actor():
    return MovieCast.objects.annotate(
        age=ExpressionWrapper(F('movie__release_date') - F('cast__birth_date'), output_field=DurationField())).order_by(
        'age').values('movie__title')[0:10]


def get_year_which_most_actors_movies_released():
    return MovieCast.objects.values(
        'movie__release_date__month').annotate(
        c=Count('cast')).order_by('-c').values('movie__release_date__month')[:1]


def get_best_twin_stars():
    return MovieCast.objects.annotate(
        castid2=F('movie__moviecast__cast_id')).values('id', 'castid2', 'cast_id').exclude(
        castid2=F('cast_id')).filter(cast_id__lt=F('castid2')).order_by('cast_id', 'castid2')[:1]


def get_yougest_and_oldest_movie_titles():
    yougest_movie_title = MovieCast.objects.annotate(
        age=ExpressionWrapper(F('cast__birth_date') - date.today(), output_field=DurationField())).values(
        'movie_id').annotate(average_age=Avg('age')).order_by('average_age').values('movie__title')[:5]
    oldest_movie_titles = MovieCast.objects.annotate(
        age=ExpressionWrapper(F('cast__birth_date') - date.today(), output_field=DurationField())).values(
        'movie_id').annotate(average_age=Avg('age')).order_by('-average_age').values('movie__title')[:5]
    return {
        'yougest_movie_title': yougest_movie_title,
        'oldest_movie_titles': oldest_movie_titles
    }

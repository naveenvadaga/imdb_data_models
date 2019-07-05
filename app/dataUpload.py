from app.models import *

actors_data = [{'name': "Rajinikanth", 'gender': GenderChoice.Male.value, 'birth_date': '1999-08-10'},
               {'name': "chiranjeevi", 'gender': GenderChoice.Male.value, 'birth_date': '1995-07-11'},
               {'name': "Bala Krishna", 'gender': GenderChoice.Male.value, 'birth_date': '1997-07-19'},
               {'name': "Pawan Kalyan", 'gender': GenderChoice.Male.value, 'birth_date': '1994-06-30'},
               {'name': "Suriya", 'gender': GenderChoice.Male.value, 'birth_date': '1985-01-1'},
               {'name': "Prabhas", 'gender': GenderChoice.Male.value, 'birth_date': '1980-01-20'},
               {'name': "Mahesh", 'gender': GenderChoice.Male.value, 'birth_date': '1990-12-12'},
               {'name': "Kajal", 'gender': GenderChoice.Female.value, 'birth_date': '1989-12-1'},
               {'name': "Anushka", 'gender': GenderChoice.Female.value, 'birth_date': '1999-06-12'},
               {'name': "Rakul ", 'gender': GenderChoice.Female.value, 'birth_date': '1997-07-19'},
               {'name': "Tamahna", 'gender': GenderChoice.Female.value, 'birth_date': '1997-04-15'},
               {'name': "Samantha", 'gender': GenderChoice.Female.value, 'birth_date': '1992-03-19'},
               {'name': "Anushka sharma", 'gender': GenderChoice.Female.value, 'birth_date': '1993-05-17'},
               {'name': "rohit sharma", 'gender': GenderChoice.Female.value, 'birth_date': '1998-09-22'},
               {'name': "srk", 'gender': GenderChoice.Female.value, 'birth_date': '1989-07-17'},
               {'name': "hero1", 'gender': GenderChoice.Male.value, 'birth_date': '1990-12-11'},
               {'name': "hero2", 'gender': GenderChoice.Male.value, 'birth_date': '1989-03-12'},
               {'name': "hero3", 'gender': GenderChoice.Female.value, 'birth_date': '1993-04-10'},
               {'name': "hero4", 'gender': GenderChoice.Female.value, 'birth_date': '1997-07-09'},
               {'name': "hero5", 'gender': GenderChoice.Male.value, 'birth_date': '1999-12-11'},
               {'name': "hero6", 'gender': GenderChoice.Male.value, 'birth_date': '1998-03-12'},
               {'name': "hero7", 'gender': GenderChoice.Female.value, 'birth_date': '1991-04-10'},
               {'name': "hero8", 'gender': GenderChoice.Female.value, 'birth_date': '1990-07-09'}
               ]

movie_data = [{'title': 'A', 'release_date': '2000-09-30'},
              {'title': 'B', 'release_date': '2005-04-05'},
              {'title': 'C', 'release_date': '1998-01-12'},
              {'title': 'D', 'release_date': '1999-07-03'},
              {'title': 'E', 'release_date': '2008-06-15'},
              {'title': 'F', 'release_date': '2009-02-03'},
              {'title': 'G', 'release_date': '2010-08-16'},
              {'title': 'H', 'release_date': '2015-11-15'},
              {'title': '1', 'release_date': '2000-09-30'},
              {'title': '2', 'release_date': '2005-02-05'},
              {'title': '3', 'release_date': '1998-03-12'},
              {'title': '4', 'release_date': '1999-04-03'},
              {'title': '5', 'release_date': '2008-07-15'},
              {'title': '6', 'release_date': '2009-12-03'},
              {'title': '7', 'release_date': '2010-11-16'},
              {'title': '8', 'release_date': '2015-10-15'}
              ]

MovieCast_data = [{'movie_id': '1', 'cast_id': '1', 'role': 'Hero'},
                  {'movie_id': '1', 'cast_id': '10', 'role': 'Heroine'},
                  {'movie_id': '2', 'cast_id': '6', 'role': 'Hero'},
                  {'movie_id': '2', 'cast_id': '13', 'role': 'Heroine'},
                  {'movie_id': '3', 'cast_id': '4', 'role': 'Hero'},
                  {'movie_id': '3', 'cast_id': '14', 'role': 'Heroine'},
                  {'movie_id': '4', 'cast_id': '7', 'role': 'Hero'},
                  {'movie_id': '4', 'cast_id': '9', 'role': 'Heroine'},
                  {'movie_id': '5', 'cast_id': '2', 'role': 'Hero'},
                  {'movie_id': '5', 'cast_id': '12', 'role': 'Heroine'},
                  {'movie_id': '6', 'cast_id': '1', 'role': 'Hero'},
                  {'movie_id': '6', 'cast_id': '13', 'role': 'Heroine'},
                  {'movie_id': '7', 'cast_id': '1', 'role': 'Hero'},
                  {'movie_id': '8', 'cast_id': '13', 'role': 'Heroine'},
                  {'movie_id': '9', 'cast_id': '2', 'role': 'Hero'},
                  {'movie_id': '10', 'cast_id': '2', 'role': 'Heroine'},
                  {'movie_id': '11', 'cast_id': '3', 'role': 'Hero'},
                  {'movie_id': '12', 'cast_id': '3', 'role': 'Heroine'},
                  {'movie_id': '13', 'cast_id': '4', 'role': 'Hero'},
                  {'movie_id': '14', 'cast_id': '4', 'role': 'Heroine'}
                  ]

MovieRating_data = [{'movie_id': '1', 'rating': '4', 'no_of_ratings': '1000'},
                    {'movie_id': '1', 'rating': '5', 'no_of_ratings': '1000'},
                    {'movie_id': '1', 'rating': '3', 'no_of_ratings': '70'},
                    {'movie_id': '2', 'rating': '3', 'no_of_ratings': '500'},
                    {'movie_id': '3', 'rating': '2', 'no_of_ratings': '1200'},
                    {'movie_id': '4', 'rating': '4', 'no_of_ratings': '600'},
                    {'movie_id': '5', 'rating': '2', 'no_of_ratings': '700'},
                    {'movie_id': '1', 'rating': '1', 'no_of_ratings': '1000'},
                    {'movie_id': '6', 'rating': '1', 'no_of_ratings': '700'},
                    {'movie_id': '7', 'rating': '1', 'no_of_ratings': '700'},
                    {'movie_id': '6', 'rating': '5', 'no_of_ratings': '1700'},
                    {'movie_id': '7', 'rating': '5', 'no_of_ratings': '1700'},
                    ]


def add_actors_to_db():
    Actor.objects.bulk_create(Actor(**d) for d in actors_data)


def add_movie_data_to_db():
    Movie.objects.bulk_create(Movie(**d) for d in movie_data)


def add_MovieCast_to_db():
    MovieCast.objects.bulk_create(MovieCast(**d) for d in MovieCast_data)


def add_MovieRating_to_db():
    MovieRating.objects.bulk_create(MovieRating(**d) for d in MovieRating_data)


'''
[{'id': '1', 'name': "Rajinikanth", 'gender': GenderChoice.Male.value, 'birth_date': '1955-06-10'},
               {'id': '2', 'name': "chiranjeevi", 'gender': GenderChoice.Male.value, 'birth_date': '1955-07-10'},
               {'id': '3', 'name': "Rajinikanth", 'gender': GenderChoice.Male.value, 'birth_date': '1955-06-10'},
               {'id': '4', 'name': "Bala Krishna", 'gender': GenderChoice.Male.value, 'birth_date': '1955-06-10'},
               {'id': '5', 'name': "Pawan Kalyan", 'gender': GenderChoice.Male.value, 'birth_date': '1955-06-10'},
               {'id': '6', 'name': "Suriya", 'gender': GenderChoice.Male.value, 'birth_date': '1955-06-10'},
               {'id': '7', 'name': "Prabhas", 'gender': GenderChoice.Male.value, 'birth_date': '1955-06-10'},
               {'id': '8', 'name': "Mahesh", 'gender': GenderChoice.Male.value, 'birth_date': '1955-06-10'},
               {'id': '9', 'name': "Kajal", 'gender': GenderChoice.Female.value, 'birth_date': '1955-06-10'},
               {'id': '10', 'name': "Anushka", 'gender': GenderChoice.Female.value, 'birth_date': '1955-06-10'},
               {'id': '11', 'name': "Rakul ", 'gender': GenderChoice.Female.value, 'birth_date': '1955-06-10'},
               {'id': '12', 'name': "Tamahna", 'gender': GenderChoice.Female.value, 'birth_date': '1955-06-10'},
               {'id': '13', 'name': "Samantha", 'gender': GenderChoice.Female.value, 'birth_date': '1955-06-10'},
               {'id': '14', 'name': "Anushka sharma", 'gender': GenderChoice.Female.value, 'birth_date': '1955-06-10'}

               ]
'''

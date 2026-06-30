import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course

# from drf_test_demo.models import Message


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=3)
    course = courses[0]

    # Act
    response = client.get(f'/api/v2/courses/{course.id}/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == course.id
    assert data['name'] == course.name



@pytest.mark.django_db
def test_get_list_course(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=5)

    # Act
    response = client.get('/api/v2/courses/')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['count'] == 5
    # assert len(data["results"]) == 5



@pytest.mark.django_db
def test_get_filter_id_course(client, course_factory):
    # Arrange
    courses = course_factory(_quantity=5)
    course = courses[0]

    # Act
    response = client.get(f'/api/v2/courses/?id={course.id}')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['count'] == 1
    assert data['results'][0]['id'] == course.id


@pytest.mark.django_db
def test_get_filter_name_course(client, course_factory):
    # Arrange
    course_factory(_quantity=4)
    course = course_factory(name='Python')

    # Act
    response = client.get(f'/api/v2/courses/?name={course.name}')

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert data['count'] == 1
    assert data['results'][0]['name'] == course.name



@pytest.mark.django_db
def test_create_course(client):
    # Arrange
    count = Course.objects.count()
    # Act
    response = client.post('/api/v2/courses/', data={"name": "Python"})
    # Assert
    assert response.status_code == 201
    assert Course.objects.count() == count + 1

    course = Course.objects.get(name="Python")
    assert course.name == "Python"

    data = response.json()
    assert data["name"] == "Python"


@pytest.mark.django_db
def test_update_course(client, course_factory):
    # Arrange
    course_factory(_quantity=4)
    course = course_factory(name='Python')
    count = Course.objects.count()

    response = client.patch(f'/api/v2/courses/{course.id}/', data={"name": "Python_new"})

    assert response.status_code == 200
    assert Course.objects.count() == count

    course = Course.objects.get(id=course.id)
    assert course.name == "Python_new"

    data = response.json()
    assert data["name"] == "Python_new"


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    # Arrange
    course_factory(_quantity=4)
    course = course_factory(name='Python')
    count = Course.objects.count()

    response = client.delete(f'/api/v2/courses/{course.id}/')

    assert response.status_code == 204
    assert Course.objects.count() == count - 1
    assert not Course.objects.filter(id=course.id).exists()












    # students = students_factory(_quantity=10)


@pytest.mark.django_db
@pytest.mark.parametrize(
    "limit, students_count, expected_status",
    [
        (2, 2, 201),
        (2, 3, 400),
    ],
)
def test_limit_students(client, settings, students_factory, limit, students_count, expected_status,):
    settings.MAX_STUDENTS_PER_COURSE = limit

    students = students_factory(_quantity=students_count)
    student_ids = [student.id for student in students]

    response = client.post(
        "/api/v2/courses/",
        data={
            "name": "Python",
            "students": student_ids,
        },
    )

    assert response.status_code == expected_status



# @pytest.mark.django_db
# def test_limit_students_201(client, settings, students_factory):
#     # Arrange
#     settings.MAX_STUDENTS_PER_COURSE = 2
#     students = students_factory(_quantity=2)
#     student_ids = [student.id for student in students]
#     # Act
#     response = client.post('/api/v2/courses/', data={"name": "Python",  "students": student_ids, })
#     # Assert
#     assert response.status_code == 201
#
#
# @pytest.mark.django_db
# def test_limit_students_404(client, settings, students_factory):
#     # Arrange
#     settings.MAX_STUDENTS_PER_COURSE = 2
#     students = students_factory(_quantity=3)
#     student_ids = [student.id for student in students]
#     # Act
#     response = client.post('/api/v2/courses/', data={"name": "Python",  "students": student_ids, })
#     # Assert
#     assert response.status_code == 400
#
#
#

